from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("🌍Cʜᴀɴɴᴇʟ💥", url="https://t.me/Somalibots")],
        [InlineKeyboardButton(
            "💎Sᴜᴘᴘᴏʀᴛ Gʀᴏᴜᴘ💎", url="https://t.me/Somalibots_help")]
    ])
    welcomed = f"Hey <b>{message.from_user.first_name}</b>\n/help Taabo si aad Wax uga ogaatid,.. Isᴏᴅɪʀ Vɪᴅᴇᴏɢᴀ ᴀᴀᴅ Rᴀʙᴛᴏ Lɪɴᴋɪɢɪsᴀ Kᴀᴅɪʙ ʜᴀʟᴋᴀɴ ᴀʏᴀɴ ᴋᴜɢᴜ sᴏ ᴅɪʀᴀʏᴀ Sɪ ᴀᴀᴅ ᴜ ᴅᴀɢsᴀᴛᴏ🎵"
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
