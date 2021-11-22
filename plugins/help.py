from pyrogram import Client, Filters


@Client.on_message(Filters.command(["help"]))
async def start(client, message):
    helptxt = f"Hᴀᴅᴀ Rᴏʙᴏᴛᴋᴀɴ ᴡᴜxᴜ sᴏ ᴅᴀᴊɪɴ ᴋᴀʀᴀ Hᴀʟ Vɪᴅᴇᴏ Mᴀʀᴋɪɪʙᴀ (Mᴀʀᴋᴀ Lɪɴᴋ ᴘʟᴀʏʟɪsᴛ ʜᴀ ɪsᴏ ᴅɪʀɪɴ) ᴋᴀʟɪʏᴀ ɪsᴏᴅɪʀ Yᴏᴜᴛᴜʙᴇ Vɪᴅᴇᴏ Lɪɴᴋ"
    await message.reply_text(helptxt)
