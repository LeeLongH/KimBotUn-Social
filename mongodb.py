from pymongo import MongoClient
import os
from dotenv import load_dotenv

# naloži .env
load_dotenv()

# preberi connection string
uri = os.getenv("MDB_CONNECTION_STRING")
if not uri:
    raise RuntimeError("MDB_CONNECTION_STRING ni nastavljen!")

# poveži se na MongoDB
client = MongoClient(uri)
db = client["KimBotUn"]          # izberi bazo
socials = db["Socials"]          # izberi kolekcijo



def get_or_create_member(user_id, warning_number=0, score_deduction=0):
    """
    Search user by id. If it doesnt exist, create it.
    """
    member = socials.find_one({
        "user_id": user_id
    })

    if member:
        return member
    
    # Create user
    
    username = "TODO"
    score = 200 - score_deduction

    new_member = {
        "user_id": user_id,
        "username": username,
        "score": score,
        "warnings": warning_number,
    }

    socials.insert_one(new_member)
    return new_member


user_id = 1234567890
username = "LeonSturm"

member = get_or_create_member(user_id, username)
print(member)



### DROPDOWN ###

# pridobi vse dokumente
#all_docs = list(socials.find({}))   # prazni filter = vsi dokumenti


