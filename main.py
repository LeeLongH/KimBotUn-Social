import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

import mongodb as fun
from long_texts import *

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

#WELCOME_CHANNEL_ID = 1451924198137008289       # TESTing
WELCOME_CHANNEL_ID = 1389679104915406984

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.command()
async def version(ctx):
    await ctx.reply(BOT_VERSION)

@bot.event
async def on_ready():
    await bot.load_extension("Moderation")
    print(f"Logged in as {bot.user}")

@bot.command()
async def score(ctx):
    await fun.print_user_score(ctx)

@bot.command()
async def allscore(ctx):
    all_users = fun.get_all_users()
    output_lines = []
    for user in all_users:

        guild = bot.get_guild(user["guild_id"])
        if guild is None:
            try:
                guild = await bot.fetch_guild(user["guild_id"])
            except discord.NotFound:
                continue

        member = guild.get_member(user["user_id"])
        if member is None:
            try:
                member = await guild.fetch_member(user["user_id"])
            except discord.NotFound:
                output_lines.append(f"{user['user_id']:>15} : Member not found")
                continue

        nickname = member.nick or member.name
        user_score = user['score']
        output_lines.append(f"{nickname:>15} : {user_score} ({score_naming[user_score//20]})") 
    await ctx.reply("```\n" + "\n".join(output_lines) + "\n```")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    #if fun.anyone_blacklisted and message.author.id in fun.blacklist:
    #    await fun.delete_this_message(message)

    await fun.check_n_do_censoring(bot, message)

    # Make sure commands still work
    await bot.process_commands(message)

@bot.event
async def on_member_join(member):
    
    channel = member.guild.get_channel(WELCOME_CHANNEL_ID)
    if channel:
        await channel.send(welcome_message_public(member.mention) + "\n" + fun.get_random_Kim_quote())
    else:
        print("SYS: Cannot get welcome channel")

    # DM to the user
    try:
        await member.send(welcome_message_dm(member.mention))
    except discord.Forbidden:
        print("SYS: user has DMs closed")

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





