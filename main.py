import discord
from discord.ext import commands

import mongodb as fun
from long_texts import *
from utils.control import *
import punish as pun

from utils.bot_instance import bot

global blacklist

@bot.command()
async def version(ctx):
    await ctx.reply(BOT_VERSION)

@bot.event
async def on_ready():
    await bot.load_extension("utils.Moderation")
    print(f"Logged in as {bot.user}")

@bot.command()
async def myscore(ctx):
    await fun.print_user_score(ctx, ctx.author)


@bot.command()
async def score(ctx, *arg_members: discord.Member):
    # No mentions → show your own score
    if not arg_members:
        # score for yourself
        score = await fun.print_user_score(ctx, ctx.author, do_print=False)
        await ctx.reply(f"You have no real friends, but hey, at least your score is {score}")
        return

    users = []
    output_lines = []

    author_score  = await fun.print_user_score(ctx, ctx.author, do_print=False)
    users.append((ctx.author.display_name, author_score))                      
    
    # scores for all mentioned users
    for member in arg_members:
        score = await fun.print_user_score(ctx, member, do_print=False)
        db_member = fun.get_or_create_member(member)
        name = fun.clean_nickname(db_member, member.display_name)
        users.append((name, score))

    # Sort by score
    users.sort(key=lambda x: x[1], reverse=True)

    output_lines = [
        f"{name:>15}: {score} ({score_naming[score // 10]})"
        for name, score in users
    ]

    await ctx.reply("```\n" + "\n".join(output_lines) + "\n```")

@bot.command()
async def allscore(ctx):
    output_lines = await fun.print_all_score(bot)

    CHUNK_SIZE = 33
    for i in range(0, len(output_lines), CHUNK_SIZE):
        chunk = output_lines[i:i + CHUNK_SIZE]
        await ctx.reply("```\n" + "\n".join(chunk) + "\n```")

@bot.event
async def on_message(message):
    # skip IC channel
    if message.author == bot.user or message.channel.id == IC_CHANNEL:
        return

    await fun.check_n_do_censoring(bot, message)

    if len(pun.blackdict) > 0 and message.author.id in pun.blackdict:
        #print("Blacklisted")
        await pun.delete_this_message(message.author.id, message)
        #return

    # Make sure commands still work
    await bot.process_commands(message)

@bot.event
async def on_member_join(member):
   
    channel = member.guild.get_channel(GENERAL_CHAT_ID)
    if channel:
        await channel.send(welcome_message_public(member.mention) + "\n" + fun.get_random_Kim_quote())
    else:
        print("SYS: Cannot get welcome channel")

    # DM to the user
    try:
        await member.send(welcome_message_dm(member.mention))
    except discord.Forbidden:
        print("SYS: user has DMs closed")

@bot.event
async def on_member_remove(member):
    channel = member.guild.get_channel(GENERAL_CHAT_ID)
    await channel.send(await fun.member_left(member))

bot.run(TOKEN)















### DROPDOWN ###

# channel = discord.utils.get(member.guild.text_channels, name="general")

# message.content


""" 
    if message.content == "a":
        mod_cog = bot.get_cog("cogs.moderation")
        await mod_cog.mute_member(
            message.author,
            minutes=1,
            reason="Auto-mute: typed 'a'"
        )
 """





