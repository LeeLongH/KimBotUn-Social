import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

from northkorea import *
from mongodb import *
from long_texts import *

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

WELCOME_CHANNEL_ID = 1451924198137008289

bot = commands.Bot(command_prefix="!", intents=intents)

""" @bot.command()
async def hello(ctx):
    await ctx.send("Hello World!") """

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    #get_or_create_member(message) 
    
    await check_n_do_censoring(message)

    # Make sure commands still work
    await bot.process_commands(message)


@bot.event
async def on_member_join(member):
    
    
    channel = member.guild.get_channel(WELCOME_CHANNEL_ID)
    if channel:
        await channel.send(welcome_message_public(member.mention) + "\n" + get_random_Kim_quote())
    else:
        print("SYS: Cannot get welcome channel")

    # OPTION 2: Send a DM to the user
    try:
        await member.send(welcome_message_dm(member.mention))
    except discord.Forbidden:
        print("SYS: user has DMs closed")

# Run the bot
bot.run(TOKEN)


### DROPDOWN ###

# channel = discord.utils.get(member.guild.text_channels, name="general")

# message.content










