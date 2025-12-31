import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

import mongodb as fun
from long_texts import *

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN_TEST")
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

WELCOME_CHANNEL_ID = 1451924198137008289       # TESTing
#WELCOME_CHANNEL_ID = 1389679104915406984

#GENERAL_CHAT_ID = 1389679104915406984
GENERAL_CHAT_ID_TEST = 1451924198137008289      # TESTing

bot = commands.Bot(command_prefix="/", intents=intents)

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
    output_lines = await fun.print_all_score(bot)
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

@bot.event
async def on_member_remove(member):
    channel = member.guild.get_channel(GENERAL_CHAT_ID_TEST)
    await channel.send(f"👋 {member.mention} has left the server.")
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





