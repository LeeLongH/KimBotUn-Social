import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

from mongodb import *
from long_texts import *

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

WELCOME_CHANNEL_ID = 1451924198137008289

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    await bot.load_extension("Moderation")
    print(f"Logged in as {bot.user}")


@bot.command()
async def score(ctx):
    score = get_or_create_member(ctx.message)["score"] 
    await ctx.reply(f"Your score is {score}")

@bot.command()
async def allscore(ctx):
    all_users = get_all_users()
    output_lines = []
    for user in all_users:
        guild = bot.get_guild(user["guild_id"])
        member = guild.get_member(user["user_id"])
        nickname = member.nick or member.name
        user_score = user['score']
        output_lines.append(f"{nickname:>15} : {user_score} ({score_naming[user_score//20]})") 
    await ctx.reply("```\n" + "\n".join(output_lines) + "\n```")

@bot.event
async def on_message(message):
    if message.guild.id != 1450516692324061320:
        return

    if message.author == bot.user:
        return
    
    if message.content == "a":
        mod_cog = bot.get_cog("cogs.moderation")
        await mod_cog.mute_member(
            message.author,
            minutes=1,
            reason="Auto-mute: typed 'a'"
        )

    #await check_n_do_censoring(message)

    # Make sure commands still work
    await bot.process_commands(message)


@bot.event
async def on_member_join(member):
    
    channel = member.guild.get_channel(WELCOME_CHANNEL_ID)
    if channel:
        await channel.send(welcome_message_public(member.mention) + "\n" + get_random_Kim_quote())
    else:
        print("SYS: Cannot get welcome channel")

    # DM to the user
    try:
        await member.send(welcome_message_dm(member.mention))
    except discord.Forbidden:
        print("SYS: user has DMs closed")

# Run the bot
bot.run(TOKEN)


### DROPDOWN ###

# channel = discord.utils.get(member.guild.text_channels, name="general")

# message.content










