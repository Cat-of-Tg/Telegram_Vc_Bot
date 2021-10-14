from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
import config


@Client.on_message(filters.command(["start", "start@GroupMusicPlayBot"]) & filters.private & ~filters.channel)
async def start(_, message: Message):
    await message.reply_text(
        text="**ʜᴇʏ{}!**\n\nɪ**ᴄᴀɴ ᴘʟᴀʏ ᴍᴜsɪᴄ ɪɴ ᴠᴏɪᴄᴇ ᴄʜᴀᴛs ᴏғ ᴛᴇʟᴇɢʀᴀᴍ ɢʀᴏᴜᴘs.**ɪ ʜᴀᴠᴇ ᴀ  **ʟᴏᴛ ᴏғ ᴄᴏᴏʟ ғᴇᴀᴛᴜʀᴇs ᴛʜᴀᴛ ᴡɪʟʟ ᴀᴍᴀᴢᴇ ʏᴏᴜ!**\n\n**ᴄʟɪᴄᴋ /cmdlist ғᴏʀ ᴍᴏʀᴇ ʜᴇʟᴘ ᴏɴ ᴍʏ ᴜsᴀɢᴇ ❤**".format(message.from_user.mention),
        reply_markup=InlineKeyboardMarkup(
            [[
            InlineKeyboardButton(" ᴀᴅᴅ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ", url="https://t.me/lezy_music_bot?startgroup=true")
            ],[
            InlineKeyboardButton("«sᴜᴘᴘᴏʀᴛ»", url="https://t.me/BotMusics"),
            InlineKeyboardButton("«ᴄᴏᴍᴍᴀɴᴅs»", url="https://telegra.ph/Lezy-Music-Bot-10-14-2")
            ],[
             InlineKeyboardButton("«ᴍᴜsɪᴄ ɢʀᴏᴜᴘ»", url="https://t.me/music_and_chats")
            ]]
        ),
        disable_web_page_preview=false
    )
        
@Client.on_message(filters.command(["start", "start@GroupMusicPlayBot"]) & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
    await message.reply_text(
        text="**ʟᴇᴢʏ ᴍᴜsɪᴄ ʙᴏᴛ ɪs ᴏɴʟɪɴᴇ**",
        reply_markup=InlineKeyboardMarkup(
            [[
            InlineKeyboardButton(text="sᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ", url="https://t.me/teamladz_bothub")
            ]]
        )
    )


@Client.on_message(filters.command(["cmdlist", "start@GroupMusicPlayBot"]) & filters.private & ~filters.channel)
async def cmdlist(_, message: Message):
    await message.reply_text(
        text="""**Group Music Bot : Help Menu**

__× First Add Me To Your Group..
× Promote Me As Admin In Your Group With All Permission..__

**🏷 ᴄᴏᴍᴍᴀɴ ᴄᴏᴍᴍᴀɴᴅs**

• `/play` - Song Name : __Plays Via Youtube__
• `/dplay` - Song Name : __Play Via Deezer__
• `/splay` - Song Name : __Play Via Jio Saavn__
• `/playlist` - __Show now playing list__
• `/current` - __Show now playing__

• `/song` - Song Name : __Get The Song From YouTube__
• `/vid` - Video Name : __Get The Video From YouTube__
• `/deezer` - song name : __download songs you want quickly via deezer__
• `/saavn` - song name : __download songs you want quickly via saavn__
• `/search` - YouTube Title : __(Get YouTube Search Query)__

**🏷 Group Admin Commands.**

• `/skip` : __Skips Music__
• `/pause` : __Pause Playing Music__
• `/resume` : __Resume Playing Music__
• `/end` : __Stops playing Music__
• `/reload` : __Reloads Admin List__
• `/userbotjoin` : __Assistant Joins The Group__
• `/userbotleave` : __Assistant Leaves From The Group.__""",
        reply_markup=InlineKeyboardMarkup(
              [[
              InlineKeyboardButton(text="🎙️ Support Group 🎙️", url="https://t.me/MusicBotSupports")
              ]]
          )
      )
