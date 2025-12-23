from pymongo import MongoClient
import os
import random
import ssl
import certifi

from dotenv import load_dotenv
load_dotenv()
from censor import *

uri = os.getenv("MDB_CONNECTION_STRING")
if not uri:
    raise RuntimeError("MDB_CONNECTION_STRING ni nastavljen!")

client = MongoClient(uri,     
                    tls=True,
                    tlsCAFile=certifi.where()
)

db = client["KimBotUn"]
socials = db["Socials"]
quotes = db["Kim_quotes"]
warnings_table = db["Warnings"]


def get_all_users():
    return list(socials.find({}).sort("score", -1))


def get_or_create_member(message, warning_number=0, score_deduction=0):
    """
    Search user by id. If it doesnt exist, create it.
    """

    user_id = message.author.id
    guild_id = message.guild.id if message.guild else None  # or None

    member = socials.find_one({
        "user_id": user_id
    })

    if member:
        return member
    
    # Create user
    
    username = message.author.name
    score = 200 - score_deduction

    new_member = {
        "user_id": user_id,
        "guild_id": guild_id,
        "username": username,
        "score": score,
        "warnings": warning_number,
    }

    socials.insert_one(new_member)
    return new_member


def quote_generator():

    total_quotes = quotes.count_documents({})

    random_quote_id = random.randint(1, total_quotes)
    random_quote = quotes.find_one({"id": random_quote_id})

    while True:
        random_quote = quotes.find_one({"id": random_quote_id})

        yield random_quote

        random_quote_id += 1
        if random_quote_id > total_quotes:
            random_quote_id = 1
        
quote_gen = quote_generator()

def get_random_Kim_quote():
    return next(quote_gen)["quote"]


def is_user_first_warning(message):
    """
    Returns user's score
    """
    author_profile = get_or_create_member(message) 
    return (author_profile["score"], author_profile["warnings"])

def deduct_user_score_n_increase_warnings(author_id, penalty, new_warning):
    print("penalty:", penalty)
    socials.update_one(
        {"user_id": author_id},
        {
            "$inc": {
                "score": -penalty,
                "warnings": new_warning
            }
        }
    )



async def check_n_do_censoring(message):
    msg_words = message.content.split()
    is_match_found = False

    for words_pair_to_censor, (id, penalty, case_sensitive) in censor.items():
        if case_sensitive:
            if all(word in msg_words for word in words_pair_to_censor):
                is_match_found = True
        else:
            lower_msg_words = [word.lower() for word in msg_words]
            if all(word in lower_msg_words for word in words_pair_to_censor):
                is_match_found = True

        if is_match_found:
            appropriate_warnings = list(warnings_table.find({"id": id}))
            warning_to_give = random.choice(appropriate_warnings)

            user_social_score, user_warnings = is_user_first_warning(message)

            if user_warnings > 0:
                deduct_user_score_n_increase_warnings(message.author.id, penalty, +1)
                await message.reply(warning_to_give["text"] + "\n" * 2 + f"**Your current social score is {user_social_score - penalty}.**")
            else:
                deduct_user_score_n_increase_warnings(message.author.id, 0, +1)
                await message.reply(warning_to_give["text"] + "\n" * 2 + "**This is your first and last warning before i start deducting you social score.**")  

            is_match_found = False






### DROPDOWN ###

# pridobi vse dokumente
#all_docs = list(socials.find({}))   # prazni filter = vsi dokumenti


""" 
                    tls=True,
                    tlsAllowInvalidCertificates=False,
                    tlsVersion=ssl.PROTOCOL_TLSv1_2
                    ) 
                    """