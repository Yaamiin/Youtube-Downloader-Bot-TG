from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("⚜️ My Group ⚜️", url="https://t.me/Tg_Galaxy")],
        [InlineKeyboardButton(
            "⚜️ Click Here ⚜️", url="https://t.me/Tg_Galaxy")]
    ])
    welcomed = f"Hey <b>{message.from_user.first_name}</b>\n/help for More info,.. Send Me Youtube Link, So I Can Upload It To Telegram As File/Video🔥"
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
