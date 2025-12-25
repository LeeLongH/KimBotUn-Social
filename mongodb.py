from pymongo import MongoClient
import os
import random
import discord

from datetime import datetime, timedelta

from dotenv import load_dotenv
load_dotenv()
from censor import *
from long_texts import *

uri = os.getenv("MONGODB_TOKEN")
if not uri:
    raise RuntimeError("MONGODB_TOKEN ni nastavljen!")

client = MongoClient(uri)

# fun.py
anyone_blacklisted = False
blacklist = []


db = client["KimBotUn"]
socials = db["Socials"]
quotes = db["Kim_quotes"]
warnings_table = db["Warnings"]
mute_reasons = db["Mute_reasons"]

#CREW_GUILD_ID = 1450516692324061320        # TESTING
CREW_GUILD_ID = 1389679097692815613

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
    return member.top_role < member.guild.me.top_role and member.guild.me.guild_permissions.moderate_members and Imperial_Council_ID != 1451924198137008289

async def mute_member(bot, message, user_id, time_to_mute, reason=None):
    # Fetch guild and member
    guild = await fetch_user_guild(message, bot)
    member = await fetch_member(guild, user_id)

    if not can_mute_member(member, message.channel.id):
        print(f"SYS: Cannot mute {member.mention}")
        return

    try:
        await member.timeout(
            timedelta(minutes=time_to_mute),
            reason=reason
        )

        await message.reply(
            f"{member.mention} has been sent to a labor camp for re-education "
            f"for **{time_to_mute} minute{'s' if time_to_mute != 1 else ''}**.\n"
            f"**Reason:** {reason or 'Not deserving to know the reason.'}"
        )
    except:
        print(f"SYS: Cannot mute {member.mention}")
        pass

def get_all_users():
    return list(socials.find({}).sort("score", -1))

async def print_user_score(ctx, do_print=True):
    score = get_or_create_member(ctx.message)["score"]
    if do_print:
        await ctx.reply(f"Your score is {score}")
    else:
        return score

def create_user(message, user_id, guild_id, warning_number, score_deduction):

    username = message.author.name
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

def get_or_create_member(message, warning_number=0, score_deduction=0):
    """
        Search user by id. If it doesnt exist, create it.
        Return member object

    """

     # -- Find user --

    user_id = message.author.id
    guild_id = message.guild.id if message.guild else "1389679097692815613"  # CREW GUILD ID

    member = socials.find_one({
        "user_id": user_id
    })

    if member:
        return member
    
    # -- Create user --
    return create_user(message, user_id, guild_id, warning_number, score_deduction)

def mongodb_generator(collection_name):

    total_entries = collection_name.count_documents({})
    random_entry_id = random.randint(1, total_entries)

    while True:
        random_entry = collection_name.find_one({"id": random_entry_id})

        yield random_entry

        random_entry_id += 1
        if random_entry_id > total_entries:
            random_entry_id = 1
        
quote_gen = mongodb_generator(quotes)
mute_reason_gen = mongodb_generator(mute_reasons)

def get_random_Kim_quote():
    return next(quote_gen)["quote"]

def get_score_n_warnings(message):
    """
        Returns user's score and warnings

    """
    member = get_or_create_member(message) 
    return (member["score"], member["warnings"])

def random_mute_reason():
    return next(mute_reason_gen)["reason"]

def increase_score(author_id, pro_nk_word):
    now = datetime.now().replace(minute=0, second=0, microsecond=0)
    socials.update_one(
        {"user_id": author_id},
            {
                "$addToSet": {f"pro_nk_words.{pro_nk_word}.dates": now}
            },
            upsert=True
    )

async def deduct_user_score_n_increase_warnings(bot, author_id, penalty, new_warning, message, pro_nk_word):
    #print("penalty:", penalty)
    socials.update_one(
        {"user_id": author_id},
        {
            "$inc": {
                "score": -penalty,
                "warnings": new_warning
            }
        }
    )
    if penalty > 1 and message:
        member = get_or_create_member(message)
        score = member["score"]
        if score < 100:
            print("blacklist zto True")
            blacklist.append(member["user_id"])
            global anyone_blacklisted
            anyone_blacklisted = True
        elif score < 180:
            time_to_mute = mute_timing.get(score // 10) or 1
            await mute_member(bot, message, author_id, time_to_mute, random_mute_reason())

    if penalty >= 0 and not pro_nk_word:
        return
    
    # --- DPRK, ISRAHELL, ISNOTREAL ---
    increase_score(author_id, pro_nk_word)
    
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

            appropriate_warnings = list(warnings_table.find({"id": rule_id}))
            warning_to_give = random.choice(appropriate_warnings)

            if user_warnings > 0:
                await deduct_user_score_n_increase_warnings(bot, message.author.id, penalty, +1, message, "")
                await message.reply(warning_to_give["text"] + "\n" * 2 + f"**Your current social score is {user_social_score - penalty}.**")
            else:
                await deduct_user_score_n_increase_warnings(bot, message.author.id, 0, +1, message, "")
                await message.reply("Imaginary state mentioned, educate yourself!" if warning_to_give["text"].startswith("Imaginary state mentioned") else  warning_to_give["text"] + "\n" * 2 + "**This is your first and last warning before i start deducting you social score.**")  

async def delete_this_message(message):
    global anyone_blacklisted
    redeeming_message = "I became DPRK fun"
    if message.content == redeeming_message:
        blacklist.remove(message.author.id)

        anyone_blacklisted = bool(blacklist)
        return
    
    print("blacklist, anyone_blacklisted: ", blacklist, anyone_blacklisted)
    await message.delete()
### DROPDOWN ###

# pridobi vse dokumente
#all_docs = list(socials.find({}))   # prazni filter = vsi dokumenti

