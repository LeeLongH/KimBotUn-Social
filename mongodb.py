
import os
import random
import discord
import re 

from datetime import datetime, timedelta

from dotenv import load_dotenv
load_dotenv()
from censor import *
from long_texts import *
from utils.control import *
from punish import * 

from utils.generator import mongodb_generator
import mongo as mon

import punish as pun

mute_reasons = db["Mute_reasons"]

if not mongo_uri:
    raise RuntimeError("MONGODB_TOKEN ni nastavljen!")

socials = db["Socials"]
quotes = db["Kim_quotes"]
warnings_table = db["Warnings"]


async def fetch_user_guild(message, bot):
    guild = message.guild or bot.get_guild(CREW_GUILD_ID)
    if guild is None:
        guild = await bot.fetch_guild(CREW_GUILD_ID)

    return guild

async def fetch_member(guild, user_id):
    member = guild.get_member(user_id)
    if member is None:
        member = await guild.fetch_member(user_id)

    return member

def can_mute_member(member, Imperial_Council_ID):
    return member.top_role < member.guild.me.top_role and member.guild.me.guild_permissions.moderate_members and Imperial_Council_ID != 1389679105850478808

async def mute_member(bot, message, user_id, time_to_mute, reason=None):
    # Fetch guild and member
    guild = await fetch_user_guild(message, bot)
    member = await fetch_member(guild, user_id)

    if not can_mute_member(member, message.channel.id):
        print(f"SYS: Cannot mute {member.mention}")
        return

    try:
        await member.timeout(
            timedelta(seconds=time_to_mute),
            reason=reason
        )

        await message.reply(
            f"{member.mention} has been sent to a labor camp for re-education "
            f"for **{time_to_mute} seconds**.\n"
            f"**Reason:** {reason or 'Not deserving to know the reason.'}"
        )
    except:
        print(f"SYS: Cannot mute {member.mention}")
        return False
    return True

def get_all_users():
    return list(socials.find({}).sort("score", -1))

async def print_user_score(ctx, user, do_print=True):
    """
    user can be:
    - discord.Member
    - discord.User
    - int (user_id)
    """

    member = get_or_create_member(user)
    
    score = member["score"]

    if do_print:
        await ctx.reply(f"Your score is {score}")  

    return score

mute_reason_gen = mongodb_generator(mute_reasons)

def create_user(message, user_id, guild_id, warning_number, score_deduction):

    username = message.name if hasattr(message, "name") else message.author.name

    score = 200 - score_deduction

    new_member = {
        "user_id": user_id,
        "guild_id": guild_id,
        "username": username,
        "score": score,
        "warnings": warning_number,
        "pro_nk_words" : {}
    }

    socials.insert_one(new_member)

    return new_member

def get_or_create_member(source, warning_number=0, score_deduction=0):
    """
    source can be:
    - discord.Member
    - discord.User
    - discord.Message / Context
    - int (user_id)
    """



    # ---- Resolve user_id & guild_id ----

    if isinstance(source, int):
        user_id = source
        guild_id = CREW_GUILD_ID

    elif isinstance(source, (discord.Member, discord.User)):
        user_id = source.id
        guild_id = source.guild.id if hasattr(source, "guild") and source.guild else CREW_GUILD_ID

    else:  # message or ctx
        user_id = source.author.id
        guild_id = source.guild.id if source.guild else CREW_GUILD_ID

    # ---- Find user ----

    member = socials.find_one({"user_id": user_id})
    if member:
        return member

    # ---- Create user ----
    return create_user(source, user_id, guild_id, warning_number, score_deduction)

quote_gen = mongodb_generator(quotes)

def get_random_Kim_quote():
    return next(quote_gen)["quote"]

def get_score_n_warnings(message):
    """
        Returns user's score and warnings

    """
    member = get_or_create_member(message) 
    return (member["score"], member["warnings"])


def increase_pro_nk_words(author_id, pro_nk_word):
    now = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
    socials.update_one(
        {"user_id": author_id},
            {
                "$addToSet": {f"pro_nk_words.{pro_nk_word}.dates": now}
            },
            upsert=True
    )


def pro_nk_word_already_counted_today(author_id, pro_nk_word):

    today = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)

    return socials.find_one(
                                {
                                    "user_id": author_id,
                                    f"pro_nk_words.{pro_nk_word}.dates": today
                                },
                            ) is not None

async def deduct_user_score_n_increase_warnings(bot, author_id, penalty, new_warning, message, pro_nk_word):
    
    counted_pro_nk = False
    if pro_nk_word:
        counted_pro_nk = pro_nk_word_already_counted_today(author_id, pro_nk_word)

    # DEDUCT SCORE  
    if not counted_pro_nk:
        socials.update_one(
            {"user_id": author_id},
            {
                "$inc": {
                    "score": -penalty,
                    "warnings": new_warning
                }
            }
        )

        
    # INFLICT PUNISHMENT
    if penalty > 1 and message:
        member = get_or_create_member(message)
        score = member["score"]

        if score < 180:
            time_to_mute = (mute_timing.get(score // 10) or 1) + ((9 - (score % 10)) * 2)
            person_can_be_muted = await mute_member(bot, message, author_id, time_to_mute, next(mute_reason_gen)["reason"])
            
            if not person_can_be_muted:
                score -= 10

        if score < 160:
            pun.blackdict.update({member["user_id"] : "uninformed"})

    if penalty >= 0 and not pro_nk_word:
        return
    
    # --- PRO NK WORDS ---
    increase_pro_nk_words(author_id, pro_nk_word)
    
async def check_n_do_censoring(bot, message):
    msg_words = message.content.split()
    
    for words_pair_to_censor, (rule_id, penalty, case_sensitive) in censor.items():
        is_match_found = False
        if case_sensitive:
            if all(word in msg_words for word in words_pair_to_censor):
                is_match_found = True
        else:
            lower_msg_words = [word.lower() for word in msg_words]
            if all(word in lower_msg_words for word in words_pair_to_censor):
                is_match_found = True

        if is_match_found:
            user_social_score, user_warnings = get_score_n_warnings(message)

            # Increase user's score if its pro-nk-word
            if rule_id == 100:
                await deduct_user_score_n_increase_warnings(bot, message.author.id, penalty, 0, "", words_pair_to_censor[0])
                continue

            if penalty < 0 and (message.channel == 1390260819853312092 or message.channel == 1389928255213277324):
                return

            appropriate_warnings = list(warnings_table.find({"id": rule_id}))
            warning_to_give = random.choice(appropriate_warnings)

            if user_warnings > 0:
                await deduct_user_score_n_increase_warnings(bot, message.author.id, penalty, +1, message, "")
                if rule_id != 16:
                    await message.reply(warning_to_give["text"] + "\n" * 2 + f"*Your current social score is {user_social_score - penalty}.*")
            else:
                await deduct_user_score_n_increase_warnings(bot, message.author.id, 0, +1, message, "")
                if rule_id != 16:
                    await message.reply("Imaginary state mentioned, educate yourself!" if warning_to_give["text"].startswith("Imaginary state mentioned") else  warning_to_give["text"] + "\n" * 2 + "*This is your first and last warning before i start deducting you social score.*")  


def clean_nickname(user, nickname, max_width=15):
    """keep only ASCII"""
    cleaned_nickname = re.sub(r"[^\x00-\x7F]", "", nickname)

    if not cleaned_nickname.strip():
        cleaned_nickname = user['username']

    return cleaned_nickname[:15]

async def print_all_score(bot):
    all_users = get_all_users()

    output_lines = []

    for user in all_users:

        guild = bot.get_guild(user["guild_id"])
        if guild is None:
            try:
                guild = await bot.fetch_guild(user["guild_id"])
            except discord.NotFound:
                print("guild is None")
                continue

        member = guild.get_member(user["user_id"])
        if member is None:
            try:
                member = await guild.fetch_member(user["user_id"])
            except discord.NotFound:
                print(f"{user['username']} is None")
                continue

        nickname = member.nick or member.name
        user_score = user['score']
        nickname_cleaned = clean_nickname(user, nickname)
        output_lines.append(f"{nickname_cleaned:>15} : {user_score} ({score_naming[user_score//10]})")

    return output_lines






### DROPDOWN ###

# pridobi vse dokumente
#all_docs = list(socials.find({}))   # prazni filter = vsi dokumenti


