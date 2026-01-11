from pymongo import MongoClient
import random
from pymongo import ReturnDocument

from utils.control import *
from long_texts import list_of_redeeming_text

socials = db["Socials"]

def create_user_category(user_id, new_category):
    socials.update_one(
    {"user_id": user_id},
    {"$set": {new_category: []}}
)

def get_number_of_redeeming_messages(user_id):
    user = get_user(user_id)
    score = user["score"]
    return 16 - (score // 10)


def create_user_redeeming_message(user_id):
    
    number_of_redeeming_messages = max(get_number_of_redeeming_messages(user_id), 1)
    
    # --| Create new redeeming message |--
    random_redeeming_texts = random.sample(list_of_redeeming_text, number_of_redeeming_messages)
    socials.update_one(
        {"user_id": user_id},
        {"$push": 
            {"redeeming_msgs": 
                   {"$each": random_redeeming_texts}
            }
        }
    )
    return random_redeeming_texts[0]


def create_user(message, user_id, guild_id, warning_number = 0):

    username = message.name if hasattr(message, "name") else message.author.name

    new_user = {
        "user_id": user_id,
        "guild_id": guild_id,
        "username": username,
        "score": 200,
        "warnings": warning_number,
        "pro_nk_words" : {}
    }

    socials.insert_one(new_user)

    return new_user

def get_user(user_id, warning_number=0):
    """
        Get user from DB, if it doesnt exist -> create it.

    """

    # ---- Find user ----
    user = socials.find_one({"user_id": user_id})

    if user:
        return user

    # ---- Create user ----
    return create_user(user_id, warning_number)

def get_user_redeeming_message(user_id):
    user = get_user(user_id)

    redeeming_msgs = user.get("redeeming_msgs")
    #print("redeeming_msgs: ", redeeming_msgs)
    if not redeeming_msgs:
        #print("SYS: redeeming_msgs is None")
        create_user_category(user_id, "redeeming_msgs")
        redeeming_text = create_user_redeeming_message(user_id)
        return redeeming_text
        
    return redeeming_msgs[0] if redeeming_msgs else None

def drop_user_redeeming_message(user_id):
    doc = socials.find_one_and_update(
        {"user_id": user_id},
        {"$pop": {"redeeming_msgs": -1}},           #  pop FIRST element
        projection={"_id": 0, "redeeming_msgs": 1}, #  return the rest
        return_document=ReturnDocument.AFTER
    )
    return doc["redeeming_msgs"] if doc else None

