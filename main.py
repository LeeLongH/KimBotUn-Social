import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

from northkorea import *


load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

""" @bot.command()
async def hello(ctx):
    await ctx.send("Hello World!") """

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    

    
    msg_words = message.content.split()
    print(msg_words)

    await northkorea_in_msg(msg_words, message)
    print(f"Received message: {message.content}")

    # Make sure commands still work
    await bot.process_commands(message)

# Run the bot
bot.run(TOKEN)







