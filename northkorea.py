async def northkorea_in_msg(msg_words, message):

        # --- NORTH KOREA ---
    if "korea" in msg_words:
        if "north" in msg_words:
        #  await message.channel.send
            await message.reply(
                "WARNING: The name of Democratic People's Republic of Korea should be capitalized!"
                ,mention_author=True
            )

        # --- SOUTH KOREA ---
        if "south" in msg_words:
            await message.reply(
                "CORRECTION: South Korea is an imperialist puppet regime under American occupation!"
                ,mention_author=True
            )

    # --- KIM JONG UN ---
    kim_probability = 0
    if "kim" in msg_words:
        kim_probability += 1
    if "jong" in msg_words:
        kim_probability += 1
    if "un" in msg_words:
        kim_probability += 1
    
    if kim_probability >= 2:
        await message.reply(
            "WARNING: The name of Respected Comrade Kim Jong-un - Beloved Leader of the People, should be capitalized!"
            #,mention_author=True
        )
        
    # --- USA ---
    if "usa" in msg_words or ("united" in msg_words and "states" in msg_words) or "america" in msg_words:
        await message.reply(
            "SUSPICIOUS ACTIVITY DETECTED: Detected mention of the imperialist center of global exploitation!"
            #,mention_author=True
        )

    # --- NATO ---
    if "nato" in msg_words:
        await message.reply(
            "CORRECTION: NATO is not a defence organization, but rather a tool of western aggression!"
            #,mention_author=True
        )

    # --- CAPITALISM ---
    if "capitalism" in msg_words or "crypto" in msg_words or "stocks" in msg_words:
        await message.reply(
            "CAPITALISM DETECTED - The System where rich keep getting richer and the poor only get motivational speeches!"
            #,mention_author=True
        )

    # --- CAPITALISM ---
    if "democracy" in msg_words or "elections" in msg_words or "stocks" in msg_words:
        await message.reply(
            "CORRECTION - Multi-party government: The illusion of choice between almost identical parties!"
            #,mention_author=True
        )

    # --- PHONES ---
    if "iphone" in msg_words:
        await message.reply(
            "NETFLIX: Cultural imperialism in process!"
            #,mention_author=True
        )

    # --- I THINK ---
    if "i think" in msg_words:
        await message.reply(
            "BORDERLINE INDIVIDUALISM DETECTED: There is no 'I THINK' Refrain from independent conclusions. Thought is a collective process!"
            #,mention_author=True
        )