import os
from dotenv import load_dotenv
from pymongo import MongoClient


load_dotenv()
mongo_uri = os.getenv("MONGODB_TOKEN")

client = MongoClient(mongo_uri)
db = client["KimBotUn"]
IC_CHANNEL = 1389679105850478808


# CHANGE THE FOLLOWING PARAMS


TOKEN =  os.getenv("DISCORD_TOKEN")

GENERAL_CHAT_ID = 1389679104915406984
#GENERAL_CHAT_ID = 1451924198137008289      # TESTing

#CREW_GUILD_ID = 1450516692324061320        # TESTING
CREW_GUILD_ID = 1389679097692815613

#TEST_GUILD_ID = 1450516692324061320

