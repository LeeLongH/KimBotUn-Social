
import sending as f_send
import mongo as f_mon

blackdict = {}

async def delete_this_message(user_id, message):
    global blacklist

    redeeming_message = f_mon.get_user_redeeming_message(user_id)

    if redeeming_message is None:
        return

    if message.content == redeeming_message:
        redeeming_remaining = f_mon.drop_user_redeeming_message(user_id)
        #print("has it dropped alč: ", redeeming_remaining)

        # Completed all regime praising
        if not redeeming_remaining:
            #print("No longer blacklisted")
            blackdict.pop(message.author.id)
            await f_send.dm_user(user_id, "I have enabled your texting again. You better behave now. If you lose even more score, you will be required to type many more messages at a time.")
            return
        
        # Some regime praising left to do
        else:
            await f_send.send_user_next_redeeming_message(user_id, praising_to_do = True)

           
    else:
        await message.delete()
    
        # "uninformed" = user hasnt recieved a DM explaining he is getting deleted; "informed" has been informed thus dont inform him again
        if blackdict.get(message.author.id) == "uninformed":
            blackdict.update({message.author.id : "informed"})
            await f_send.send_user_next_redeeming_message(user_id, praising_to_do = False)
            #print(blackdict)
            

    return