from telethon import events, Button, custom
import re, os
from SophiaBot.events import register
from SophiaBot import telethn as tbot
from SophiaBot import telethn as tgbot
@register(pattern=("/alive")
async def awake(event):
global ghanti
ghanti = borg.uid
edit_time = 5
""" =======================CONSTANTS====================== """
file1 = "https://telegra.ph/file/6f440b6c52be0cf1c0d29.jpg"
file2 = "https://telegra.ph/file/65c3a5f74c2d5e169bcc5.jpg"
file3 = "https://telegra.ph/file/b9b13f9bd1bf66acad9c9.jpg"
file4 = "https://telegra.ph/file/c18e9f242750f738787a7.jpg"
""" =======================CONSTANTS====================== """


async def hmm(yes):
    chat = await yes.get_chat()
    global ghanti
    ghanti = borg.uid
    await yes.delete()
    uptime = await dcdef.get_readable_time((time.time() - Lastupdate))
    pm_caption = "** ᴘꜱʏʟᴏᴄᴋᴇ ɪꜱ ᴏɴʟɪɴᴇ **\n\n"
    pm_caption += "**Your Psylocke Alive And Systems Are Working Perfectly As It Should Be...**\n\n"
    pm_caption += "✘ 𝙰𝚋𝚘𝚞𝚝 𝚖𝚎 ✘\n\n"
    pm_caption += f"➾ **ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀꜱɪᴏɴ** ☞ {version.__version__}\n"
    pm_caption += "➾ **ꜱᴜᴘᴘᴏʀᴛ ᴄʜᴀɴɴᴇʟ** ☞ [ᴊᴏɪɴ](https://t.me/Pigasusupdates)\n"
    pm_caption += "➾ **ᴀᴅᴅ ᴍᴇ**  ☞ [ᴄʟɪᴄᴋ ʜᴇʀᴇ](http://t.me/Psylocke_robot?startgroup=true)\n"
    pm_caption += "➾ **ꜱᴜᴘᴘᴏʀᴛ ᴄʜᴀᴛ** ☞ [ᴊᴏɪɴ](https://t.me/PigasusSupport)\n\n"
    pm_caption += f"➾ **ᴜᴘᴛɪᴍᴇ** ☞ {uptime}\n\n"
    pm_caption += f"➾ **ᴍʏ ᴍᴀsᴛᴇʀ** ☞ [Kwannon](tg://user?id={Kwanon})\n"
    on = await borg.send_file(yes.chat_id, file=file1,caption=pm_caption)

    await asyncio.sleep(edit_time)
    ok = await borg.edit_message(yes.chat_id, on, file=file2) 

    await asyncio.sleep(edit_time)
    ok2 = await borg.edit_message(yes.chat_id, ok, file=file3)

    await asyncio.sleep(edit_time)
    ok3 = await borg.edit_message(yes.chat_id, ok2, file=file1)
    
    await asyncio.sleep(edit_time)
    ok4 = await borg.edit_message(yes.chat_id, ok3, file=file3)
    
    await asyncio.sleep(edit_time)
    ok5 = await borg.edit_message(yes.chat_id, ok4, file=file2)
    
    await asyncio.sleep(edit_time)
    ok6 = await borg.edit_message(yes.chat_id, ok5, file=file1)
    
    await asyncio.sleep(edit_time)
    ok7 = await borg.edit_message(yes.chat_id, ok6, file=file4)

    
