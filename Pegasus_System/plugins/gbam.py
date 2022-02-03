from Pegasus_System import system_cmd, System
import random

GBAM_MSG = ( "Fucking with bots",
             "play with gey's",
             "abuseing with dick",)


    @System.on(system_cmd(pattern=r"gbam"))
async def (event) -> None:
    replied_user = await event.get_reply_message()
    
    await System.send_message(
               event.chat_id,random.choice(GBAM_MSG))
        
        
        
