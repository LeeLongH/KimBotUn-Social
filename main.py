import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_message(message):
    print(f"Received message: {message.content}")
    await bot.process_commands(message)  # Important to keep commands working

@bot.command()
async def hello(ctx):
    await ctx.send("Hello World!")

bot.run(TOKEN)
