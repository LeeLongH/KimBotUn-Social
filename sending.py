import random

from utils.bot_instance import bot

from mongo import *
from long_texts import send_user_bully_message, list_of_redeeming_text
from utils.generator import mongodb_generator

mute_reasons = db["Mute_reasons"]
leave_reasons = db["Leave_reasons"]

async def get_member_from_user(user_id):
    user = get_user(user_id)

    #guild = bot.get_guild(user["guild_id"])
    #guild = bot.get_guild(1450516692324061320)

    #member = guild.get_member(user_id)

   #guild = await bot.fetch_guild(user["guild_id"])
    guild = await bot.fetch_guild(1450516692324061320)
    member = await guild.fetch_member(user_id)

    return member

async def send_user_next_redeeming_message(user_id, praising_to_do = True):
    member = await get_member_from_user(user_id)

    redeeming_message = get_user_redeeming_message(user_id)
    if praising_to_do:
        message_to_send = f"Good! Your next regime-approved statment to proclaim is '{redeeming_message}'"
    else:
        message_to_send = f"I have deleted your message in the server, and I will keep doing so until you type the following in the server '{redeeming_message}'\n{random.choice(send_user_bully_message)}"

    await member.send(message_to_send)

async def dm_user(user_id, message_to_send):

    member = await get_member_from_user(user_id)
    await member.send(message_to_send)

mute_reason_gen = mongodb_generator(mute_reasons)
leave_reason_gen = mongodb_generator(leave_reasons)

async def member_left(member):
    #user_record = socials.find_one({"user_id": member.id})
    username = f"<@{member.id}>"
    
    leave_reason = next(leave_reason_gen)["reason"].format(username=username)
    mute_reason = next(mute_reason_gen)["reason"].format()

    return f"{leave_reason}\n\n*REASON: {mute_reason}*"
