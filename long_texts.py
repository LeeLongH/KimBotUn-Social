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

score_naming = {
    20: "⭐👑 KimBot’s Most Loyal Comrade",
    19: "🌟 Kim Family Loyalist",
    18: "⭐🚜 Beloved Leader of the Harvest",
    17: "🌱💠 Eternal Comrade of the Fields",
    16: "🌽🐖 Marshal of Corn and Pigs",
    15: "📜🔥 Propaganda Icon",
    14: "🌾🥇 Champion of the Collective",
    13: "🌟 Juche Revolutionary",
    12: "🔹 Loyalty and Obedience Personalized",
    11: "🚜 Dedicated Farmer",
    10: "🏡 Model Citizen",
    9: "🔹 Trusted Comrade",
    8: "⚠️ Ideologically Unstable",
    7: "🔺 Questionable Element",
    6: "❌ Disloyal Citizen",
    5: "☢️ Counter-Revolutionary rat",
    4: "🐖 Derelict Farmhand",
    3: "🪓 Saboteur",
    2: "💀 Enemy of the People",
    1: "☠️ Traitor to the State"
}

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