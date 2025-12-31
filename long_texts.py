def welcome_message_dm(member_name):
    return f""" :ear_of_rice: Welcome to the Cooperative, Farmer {member_name}:ear_of_rice:
Your arrival has been logged. Your crops are expected.

You are expected to:
- Optimize harvest cycles for maximum yield.
- Report suspiciously unproductive neighbours.
- Announce your derby desertion.
- Pretend not to notice the scarecrows watching back.

What We appreciate about Hay Day:
- Order. Routine.
- And the calming certainty that every comrade knows their place.

Enjoy your stay. :corn:
Remember, Idle farm invites questions! 
            """

def welcome_message_public(member_name):
    return f"""# :ear_of_rice: Public Welcome

:sunflower: A New Worker Enters the Commune :sunflower:

Attention, farmers.
{member_name} has arrived and has been assigned a plot, a purpose, and a quota.

May their fields be productive, their animals punctual,
and their barn audits… uneventful.
            """

mute_timing = {
    17: 0.1,
    16: 0.2,
    15: 0.5,
    14: 1,
    13: 1.5,
    12: 2,
    11: 3,
    10: 4,
    9: 5,
    8: 6,
    7: 8,
    6: 10,
    5: 20,
    4: 30,
    3: 40,
    2: 50,
    1: 60 
}


BOT_VERSION = \
"""
            2.0 - delete messages below score 100
(current)   1.1 - scoring and muting adjusted, IC excluded from muting
            1.0 - working bot with muting ability
"""


score_naming = {
    40: "⭐👑 KimBot Un’s Most Loyal Comrade",
    39: "⭐👑 KimBot Un’s Loyal Comrade",
    38: "🌟 Senior Kim Family Loyalist",
    37: "🌟 Kim Family Loyalist",
    36: "⭐🚜 Beloved Leader of the Grand Harvest",
    35: "⭐🚜 Beloved Leader of the Harvest",
    34: "🔹 Loyalty and Obedience Exemplified",
    33: "🔹 Loyalty and Obedience Personalized",
    32: "🌱💠 Eternal Comrade of the Sacred Fields",
    31: "🌱💠 Eternal Comrade of the Fields",
    30: "🌽🐖 Supreme Marshal of Corn and Pigs",
    29: "🌽🐖 Marshal of Corn and Pigs",
    28: "📜🔥 Revered Propaganda Icon",
    27: "📜🔥 Propaganda Icon",
    26: "🌾🥇 Champion of the Collective",
    25: "🌾🥇 Champion of the Commune",
    24: "🌟 Honored Juche Revolutionary",
    23: "🌟 Juche Revolutionary",
    22: "🏡 Exemplary Model Citizen",
    21: "🏡 Model Citizen",
    20: "🚜 Dedicated Farmer",
    19: "🔺 Questionable Element",
    18: "🔺 Person of Ideological Concern",
    17: "♦️Untrustworthy Comrade",
    16: "♦️Highly Untrustworthy Comrade",
    15: "⚠️ Ideologically Unstable",
    14: "⚠️ Severely Ideologically Unstable",
    13: "❌ Disloyal Citizen",
    12: "❌ Openly Disloyal Citizen",
    11: "❌ Persistently Disloyal Citizen",
    10: "❗❗❗Suspected Puppet regime spy",
    9: "❗❗❗Puppet regime spy",
    8: "☢️☢️ Counter-Revolutionary rat",
    7: "☢️☢️ Confirmed Counter-Revolutionary rat",
    6: "🪓🪓🪓 Imperialist Disruptor",
    5: "🪓🪓🪓 Imperialist Saboteur",
    4: "💀💀 Enemy of the People",
    3: "💀💀 Declared Enemy of the People",
    2: "☠️☠️☠️ Traitor to the State",
    1: "☠️☠️☠️ Ultimate Traitor to the State"
}


leave_reasons = [
    "COMPLIANCE FAILURE DETECTED: Preventative measures have taken place against {username} who is no longer with us.",
    "Attention all members: {username} believed individuality was permitted. This misconception has been corrected by removing {username} from the server.",
    "{username} tried Defecting from our Glorious server, and failed miserably.",
    "🟥 DISCIPLINARY NOTICE 🟥: {username} has violated DPRK doctrine thus has been removed from the collective.",
    "🚨 WARNING TO ALL 🚨: {username} believed escape was possible. {username} has betrayed The Supreme leader and was liquidated.",
    "⚖️ UNANIMOUS VERDICT ⚖️: {username} was found guilty of disobedience and was sent to reeducation camp with his entire family.",
    "🔒 {username} failed their final loyalty evaluation. Reassignment to a reeducation camp has been approved.",
    "🛑 TRAITOR IDENTIFIED 🛑: {username} has been removed for ideological contamination. {username} is no longer with us.",
    "🟥 RECORD UPDATE 🟥: {username} showed weakness of character and was removed from the server.",
    "⚖️ The Council has ruled that {username} is unworthy of continued membership is this Glorious server.",
    "📡 BROADCAST INTERRUPTION 📡: {username} is no longer part of the state-approved population.",
    "🛑 WARNING TO ALL MEMBERS 🛑: {username} dreamt of Desertion. We made sure he disappeared and We wont be seeing {username} around anymore.",
    "🚨 Citizen {username} attempted independent thinking and has been dealt with accordingly. {username} is no longer with us",
    "🟥 FINAL DECREE 🟥: Citizen {username} has committed irreversible betrayal. {username} has 'unexpectedly' and 'tragically' passed away.",
    "LET IT BE KNOWN: {username} is no longer with us for not being worthy of Our server."
    "⚠️ PUBLIC WARNING ⚠️: {username} abandoned the collective. Let {username}'s expulsion serve as an example",
    "📜 OFFICIAL STATEMENT: {username} has voluntarily removed themselves from the Glorious Collective. {username} wouldnt last anyway.",
    "🟥 {username} has failed the loyalty test and has been removed from the community.",
    "📢 Supreme Command announces that {username} has shown weakness and tried to flee - unsuccessfully. Loyalty will be rewarded. Defection will not.",
    "⚠️ TRAITOR ALERT ⚠️: Traitor {username} has abandoned the server and will be erased from official records.",
    "FINAL NOTICE: {username} attempted to leave. We purged {username} out of existence.",
    "📡 OFFICIAL BROADCAST 📡 {username} has been dealt with. Loyalty remains mandatory.",
    "{username} has no manners and deserved to be forcefully removed out from the server",
    "{username}'s membership has been revoked thus was removed from the server"
]
