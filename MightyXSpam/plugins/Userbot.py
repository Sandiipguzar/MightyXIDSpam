# Mighty X Spam - Spam Userbots 
# @MightyXSpam | Keep Credits Madafaka !!
 
import os
import sys
from MightyXSpam import Mig, Mig2, Mig3, Mig4, Mig5 , Mig6, Mig7, Mig8, Mig9, Mig10, Mig11, Mig12, Mig13, Mig14, Mig15, Mig16, Mig17, Mig18, Mig19, Mig20, Mig21, Mig22, Mig23, Mig24, Mig25, Mig26, Mig27, Mig28, Mig29, Mig30, Mig31, Mig32, Mig33, Mig34, Mig35, Mig36, Mig37, Mig38, Mig39, Mig40, SUDO_USERS, OWNER_ID
from MightyXSpam import ALIVE_NAME, ALIVE_PIC, ALIVE_TEXT, mightyversion
from .. import CMD_HNDLR as hl
from telethon import events, version
from telethon.tl.functions.users import GetFullUserRequest
from time import time
from datetime import datetime
 
mention = f"[{ALIVE_NAME}](tg://user?id={OWNER_ID})"
 
def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]
 
    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)
 
    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "
 
    time_list.reverse()
    ping_time += ":".join(time_list)
 
    return ping_time
 
@Mig.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@Mig2.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@Mig3.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@Mig4.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@Mig5.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@Mig6.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@Mig7.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@Mig8.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@Mig9.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@Mig10.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@Mig11.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@Mig12.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@Mig13.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@Mig14.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@Mig15.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@Mig16.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@Mig17.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@Mig18.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@Mig19.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@Mig20.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@Mig21.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@Mig22.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@Mig23.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@Mig24.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@Mig25.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@Mig26.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@Mig27.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@Mig28.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@Mig29.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@Mig30.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@Mig31.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@Mig32.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@Mig33.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@Mig34.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@Mig35.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@Mig36.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@Mig37.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@Mig38.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@Mig39.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@Mig40.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
async def ping(e):
    if e.sender_id in SUDO_USERS:
            start = datetime.now()
            check = await e.reply("𝙋𝙤𝙣𝙜!")
            end = datetime.now()
            ms = (end-start).microseconds / 1000
            user = await e.client(GetFullUserRequest(e.sender_id))
            firstname = user.user.first_name
            userid = user.user.id
    if userid == OWNER_ID:
        await check.edit(f"█▀█ █▀█ █▄░█ █▀▀\n█▀▀ █▄█ █░▀█ █▄█\n\n    ⚡ 𝐌𝐢𝐠𝐡𝐭𝐲 𝐗 𝐒𝐩𝐚𝐦 ⚡\n\n𝐏𝐢𝐧𝐠 : `{ms}` ᴍs\n𝐎𝐰𝐧𝐞𝐫 : [{firstname}](tg://user?id={userid})")
    else:
        await check.edit(f"█▀█ █▀█ █▄░█ █▀▀\n█▀▀ █▄█ █░▀█ █▄█\n\n    ⚡ 𝐌𝐢𝐠𝐡𝐭𝐲 𝐗 𝐒𝐩𝐚𝐦 ⚡\n\n𝐏𝐢𝐧𝐠 : `{ms}` ᴍs\n𝐒𝐮𝐝𝐨 𝐔𝐬𝐞𝐫 : [{firstname}](tg://user?id={userid})")
 
# ALIVE
 
MIG_PIC = ALIVE_PIC if ALIVE_PIC else "https://telegra.ph/file/38eae16b57a0c2d039423.jpg"
 
MIG_TEXT = ALIVE_TEXT if ALIVE_TEXT else "╚»★ 𝗠𝗶𝗴𝗵𝘁𝘆𝗫𝗦𝗽𝗮𝗺 𝗶𝘀 𝗛𝗲𝗿𝗲 ★«╝"
 
 
 
   
@Mig.on(events.NewMessage(incoming=True, pattern=r"\%salive" % hl))
async def alive(event):
    if event.sender_id in SUDO_USERS:
        start = datetime.now()
        text = "𝘊𝘩𝘦𝘤𝘬𝘪𝘯𝘨..."
        check = await event.reply(text, parse_mode=None, link_preview=None)
        end = datetime.now()
        ms = (end-start).microseconds / 1000
        await check.delete()
        await Mig.send_file(event.chat_id, MIG_PIC, caption=f"{MIG_TEXT}\n\n════════════════════\n⚡ 𝐏𝐢𝐧𝐠 : {ms}ᵐˢ\n⚡ 𝐎𝐰𝐧𝐞𝐫 : {mention}\n⚡ 𝐌𝐢𝐠𝐡𝐭𝐲 𝐗 𝐒𝐩𝐚𝐦 : `{mightyversion}`\n⚡ 𝐏𝐲𝐭𝐡𝐨𝐧 𝐕𝐞𝐫𝐬𝐢𝐨𝐧 : `3.9.6`\n⚡ 𝐓𝐞𝐥𝐞𝐭𝐡𝐨𝐧 𝐕𝐞𝐫𝐬𝐢𝐨𝐧 : `{version.__version__}`\n⚡ 𝐒𝐮𝐩𝐩𝐨𝐫𝐭 𝐆𝐫𝐨𝐮𝐩 : [𝗝𝗼𝗶𝗻](t.me/MightyXSupport)\n⚡ 𝐔𝐩𝐝𝐚𝐭𝐞𝐬 𝐂𝐡𝐚𝐧𝐧𝐞𝐥 : [𝗝𝗼𝗶𝗻](t.me/MightyXUpdates)\n════════════════════\n\n                  ✨ [𝐑𝐄𝐏𝐎](https://github.com/BeingMighty/MightyIDSpamDeploy) ✨")
        
        
   
# help
 
HELP_PIC = "https://telegra.ph/file/38eae16b57a0c2d039423.jpg"
 
MightyX = "╚»★ 𝗠𝗶𝗴𝗵𝘁𝘆 𝗫 𝗦𝗽𝗮𝗺 𝗛𝗲𝗹𝗽 ★«╝\n\n"
 
MightyX += f"__ᴄᴍᴅs ᴀᴠᴀɪʟᴀʙʟᴇ ɪɴ ᴍɪɢʜᴛʏ x sᴘᴀᴍ__\n\n"
 
MightyX += f"𝙐𝙨𝙚𝙧𝘽𝙤𝙩 𝘾𝙢𝙙𝙨\n\n"
 
MightyX += f" `{hl}ping` - `{hl}alive` - `{hl}setpic` - `{hl}delpic` - `{hl}setname` - `{hl}setbio` - `{hl}inviteall` - `{hl}restart` - `{hl}update` - `{hl}stats` - `{hl}addsudo` - `{hl}logs` \n\n"
 
MightyX += f"𝙅𝙤𝙞𝙣/𝙇𝙚𝙖𝙫𝙚 𝘾𝙢𝙙𝙨\n\n"
 
MightyX += f" `{hl}join` - `{hl}pjoin` - `{hl}leave`\n\n"
 
MightyX += f"𝙎𝙥𝙖𝙢/𝙍𝙖𝙞𝙙 𝘾𝙢𝙙𝙨\n\n"
 
MightyX += f" `{hl}spam` - `{hl}bigspam` - `{hl}delayspam` - `{hl}ppspam` \n\n `{hl}abuse` \n\n `{hl}raid` - `{hl}replyraid` - `{hl}dreplyraid` - `{hl}delayraid` \n\n"
 
MightyX += f"𝘿𝙈/𝙀𝙘𝙝𝙤 𝘾𝙢𝙙𝙨\n\n"
 
MightyX += f" `{hl}dm` - `{hl}dmraid` - `{hl}dmspam` \n\n `{hl}addecho` - `{hl}rmecho` \n"
 
MightyX += f"\n[𝘒𝘯𝘰𝘸 𝘔𝘰𝘳𝘦 𝘈𝘣𝘰𝘶𝘵 𝘛𝘩𝘦𝘴𝘦 𝘊𝘔𝘋𝘚](t.me/ResourceXD/2)\n\n"
 
MightyX += f"[✨ Updates ✨](t.me/MightyXUpdates)       [✨ Support ✨](t.me/MightyXSupport)\n"
 
@Mig.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
async def help(event):
    if event.sender_id in SUDO_USERS:
     await Mig.send_file(event.chat_id,
                                  HELP_PIC,
                                  caption=MightyX)                                                         
 
 
@Mig.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@Mig2.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@Mig3.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@Mig4.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@Mig5.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@Mig6.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@Mig7.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@Mig8.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@Mig9.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@Mig10.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@Mig11.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@Mig12.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@Mig13.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@Mig14.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@Mig15.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@Mig16.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@Mig17.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@Mig18.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@Mig19.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@Mig20.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@Mig21.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@Mig22.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@Mig23.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@Mig24.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@Mig25.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@Mig26.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@Mig27.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@Mig28.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@Mig29.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@Mig30.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@Mig31.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@Mig32.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@Mig33.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@Mig34.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@Mig35.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@Mig36.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@Mig37.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@Mig38.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@Mig39.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@Mig40.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
async def restart(e):
    if e.sender_id in SUDO_USERS:
        text = "𝗥𝗲𝘀𝘁𝗮𝗿𝘁𝗶𝗻𝗴 𝗬𝗼𝘂𝗿 𝗠𝗶𝗴𝗵𝘁𝘆𝗫𝗦𝗽𝗮𝗺...\nPlease Wait For Few Seconds !!"
        await e.reply(text, parse_mode=None, link_preview=None)
        try:
            await Mig.disconnect()
        except Exception:
            pass
        try:
            await Mig2.disconnect()
        except Exception:
            pass
        try:
            await Mig3.disconnect()
        except Exception:
            pass
        try:
            await Mig4.disconnect()
        except Exception:
            pass
        try:
            await Mig5.disconnect()
        except Exception:
            pass
        try:
            await Mig6.disconnect()
        except Exception:
            pass
        try:
            await Mig7.disconnect()
        except Exception:
            pass
        try:
            await Mig8.disconnect()
        except Exception:
            pass
        try:
            await Mig9.disconnect()
        except Exception:
            pass
        try:
            await Mig10.disconnect()
        except Exception:
            pass
        try:
            await Mig11.disconnect()
        except Exception:
            pass
        try:
            await Mig12.disconnect()
        except Exception:
            pass
        try:
            await Mig13.disconnect()
        except Exception:
            pass
        try:
            await Mig14.disconnect()
        except Exception:
            pass
        try:
            await Mig15.disconnect()
        except Exception:
            pass
        try:
            await Mig16.disconnect()
        except Exception:
            pass
        try:
            await Mig17.disconnect()
        except Exception:
            pass
        try:
            await Mig18.disconnect()
        except Exception:
            pass
        try:
            await Mig19.disconnect()
        except Exception:
            pass
        try:
            await Mig20.disconnect()
        except Exception:
            pass
        try:
            await Mig21.disconnect()
        except Exception:
            pass
        try:
            await Mig22.disconnect()
        except Exception:
            pass
        try:
            await Mig23.disconnect()
        except Exception:
            pass
        try:
            await Mig24.disconnect()
        except Exception:
            pass
        try:
            await Mig25.disconnect()
        except Exception:
            pass
        try:
            await Mig26.disconnect()
        except Exception:
            pass
        try:
            await Mig27.disconnect()
        except Exception:
            pass
        try:
            await Mig28.disconnect()
        except Exception:
            pass
        try:
            await Mig29.disconnect()
        except Exception:
            pass
        try:
            await Mig30.disconnect()
        except Exception:
            pass
        try:
            await Mig31.disconnect()
        except Exception:
            pass
        try:
            await Mig32.disconnect()
        except Exception:
            pass
        try:
            await Mig33.disconnect()
        except Exception:
            pass
        try:
            await Mig34.disconnect()
        except Exception:
            pass
        try:
            await Mig35.disconnect()
        except Exception:
            pass
        try:
            await Mig36.disconnect()
        except Exception:
            pass
        try:
            await Mig37.disconnect()
        except Exception:
            pass
        try:
            await Mig38.disconnect()
        except Exception:
            pass
        try:
            await Mig39.disconnect()
        except Exception:
            pass
        try:
            await Mig40.disconnect()
        except Exception:
            pass
 
        os.execl(sys.executable, sys.executable, *sys.argv)
        quit()
 
