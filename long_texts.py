import random

welcome_message_public_list = [
"""# 🌻 A New Worker Enters the Commune 🌻

Attention, farmers.
{member_name} has arrived and has been assigned a plot, a purpose, and a quota.

May their fields be productive, their animals punctual,
and their barn audits… uneventful.
""",
"""
# 🌾 Offical greeting from Kimbot Un 🌾

Glorious salutations, Farmer {member_name}.

Your arrival has been noticed.
Your farm has been acknowledged.
Your productivity is anticipated.

You have been granted a plot of land and a chance to contribute meaningfully to the Collective Harvest.

Remember:
- Idle fields invite concern.
- Full silos bring honor.

Do not worry if you feel watched.
That feeling means the system is working.

Farm proudly.
KimBot Un is satisfied… for now.
""",
"""
# 🌾 Public Welcome 🌾

Welcome, Comrade {member_name}.

You are now part of something bigger than yourself.

Reminder: Wheat is temporary but obedience must be constantly displayed.

Farm while you still can.
Failure to do that will result in disciplinary actions.
""",
"""
# 🌾Transmission recieved from KimBot Un 🌾

Farmer {member_name} detected.
Account registered.
Fields pending inspection.

You have been welcomed into the Cooperative because you were… suitable.

Serve well.
Harvest often.
And remember — Loyalty must be shown daily.

Enjoy your stay. :corn:
""",
"""
# 🌾 Official notice — Cooperative registry 🌾

Farmer {member_name}, your presence has been recorded.

Your farm will be evaluated on:
- Yield consistency
- Timer obedience
- Attitude toward the system

Irregular production will be noted.
Repeated procrastination will be remembered.

And remember, Compliance grows faster than wheat.
""",
"""
# 🌾 Welcome, {member_name} 🌾

You were not randomly selected.
Your farm was deemed… adequate.

From this moment forward:
- Your idle machines will be questioned.
- Your empty fields will raise concern.
- And your silence will be interpreted as agreement.

May your farming me done in unwavering loyalty to the eternal stability of the Democratic People’s Republic of Korea.
""",
"""
# 🌾A new farmer has joined the Collective 🌾

Greetings, Farmer {member_name}

Your forerunner has disappointed the harvest.
May your performance satisfy the Collective.

Your performance will be compared and those who fall behind will be re-evaulated”

Now continue farming under Our watchful eye.
""",
"""
# 📢 KimBot Un public notice 📢

Attention, Cooperative.

The Cooperative awaits correction. 
Farmer {member_name} has not yet been seen tending their fields.
We trust this is temporary.

Enjoy your stay. :corn:
""",
"""
# 🚨 PRODUCTIVITY ALERT 🚨

Some farmers have failed to report for derby duties.

Crops do not grow themselves.

Let This message serve as encouragement.

And welcome our new member {member_name} who has joined the collective harvest and the social score to measure his competence.
""",
"""
# 🌾 Mandatory welcome directive 🌾

Farmer {member_name}, you are now part of the Cooperative.

Forget democracy here, failure to maintain productivity will result in:
- Increased monitoring
- isolation
- restriction of your 'rights'

Derby participation is optional.
Explaining absence is not.

Remeber, idle farms attract attention.
"""
]



#- The cows must be milked on schedule.

#Farmer {member_name} continues to test the patience of the Cooperative.

# 🌾 KimBot Un Announces 🌾


def welcome_message_dm(member_name):
    return f"""
# 🌾 Welcome to the Cooperative, Farmer {member_name}🌾
Your arrival has been logged. Your crops are required.

You are expected to:
- Optimize harvest cycles for maximum yield.
- Report suspiciously unproductive neighbours.
- Announce your derby desertion.
- Pretend not to notice the scarecrows watching back.

What We appreciate about Hay Day:
- Order. Routine.
- And the calming certainty that every comrade knows their place.

Enjoy your stay. :corn:
Remember, idle farm invites questions! 
"""

def welcome_message_public(member_name):

    #template = random.choice(welcome_message_public_list)
    template = random.choice(welcome_message_public_list[0], welcome_message_public_list[5])
    return template.format(member_name=member_name)

mute_timing = {
    17: 0.1,
    16: 0.4,
    15: 0.7,
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
1.3 - !myscore & !score @person1 @person2 @personN
1.2 - goodbye message
1.1 - scoring and muting adjusted, IC excluded from muting
1.0 - working bot with muting ability
"""
#2.0 - delete messages below score 100

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
    17: "♦️ Untrustworthy Comrade",
    16: "♦️ Highly Untrustworthy Comrade",
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