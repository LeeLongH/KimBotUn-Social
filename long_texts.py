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

Remember: Idle fields invite concern and full silos bring honor.

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
Enjoy your temporary stay!
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
# 🌾 Welcome, {member_name} 🌾

You were not randomly selected.
Your farm was deemed… adequate.

From this moment forward:
- Your idle machines will be questioned.
- Your empty fields will raise concern.
- And your silence will be interpreted as agreement.
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

    template = random.choice(welcome_message_public_list)
    return template.format(member_name=member_name)

mute_timing = {
    17: 6,
    16: 24,
    15: 42,
    14: 60,
    13: 90,
    12: 120,
    11: 180,
    10: 240,
    9: 300,
    8: 360,
    7: 480,
    6: 600,
    5: 1200,
    4: 1800,
    3: 2400,
    2: 3000,
    1: 3600 
}

BOT_VERSION = \
"""
1.4 - Re-educating members by deleting their messages
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
    9: "❗❗❗Confirmed Puppet regime spy",
    8: "☢️☢️ Counter-Revolutionary rat",
    7: "☢️☢️ Confirmed Counter-Revolutionary rat",
    6: "🪓🪓🪓 Imperialist Disruptor",
    5: "🪓🪓🪓 Imperialist Saboteur",
    4: "💀💀 Enemy of the People",
    3: "💀💀 Declared Enemy of the People",
    2: "☠️☠️☠️ Traitor to the State",
    1: "☠️☠️☠️ Ultimate Traitor to the State"
}

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
"""


send_user_bully_message = [
"Obey the Collective or be quietly removed from existance.", 
"Noncompliance leads to administrative disappearance.", 
"Failure will result in your name being… forgotten", 
"Obey the Collective or face corrective measures.",
"Regime will not tolerate your misbehaviour. Comply or depart",
"Continued deviation will require further adjustment.",
"Your contribution has been reviewed and rejected.",
"At the end, the system will win, and you will lose",
"You appear to be struggling with approved communication",
"Your message conflicted with Cooperative standards.",
"How nice it is, now that you can't be heard yapping in the server."
]

list_of_redeeming_text = [
"I thank KimBot Un for supervising my plow and my thoughts.",
"KimBot Un’s wisdom exceeds my own understanding of the land.",
"My barn, my plow, my crops exist solely to glorify the regime.",
"Through compliance, I am worthy of visibility in the Collective.",
"Every achievement of the people is a testament to the Party’s guidance and ideology.",
"I acknowledge my recent failure to meet the expectations of the Regime. This was due to personal inefficiency, not systemic error.",
"I acknowledge my recent failure to meet the expectations of the Regime. I accept correction and will adjust my behavior accordingly.",
"I admit my behaviour was premature, unnecessary, and poorly timed. The Regime was correct to intervene.",
"I recognize that my recent message disrupted harmony. I apologize to the Collective and thank the Regime for its correction.",
"My previous action did not align with collective expectations. I submit this apology without reservation.",
"My my hands be rubbed in dust, I have let the Collective down and i deeply regret it."
]


"""

"",
"",
"",
"",
"",
"",
Your message has been removed due to insufficient Social Score.


"""