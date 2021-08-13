from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("⚜️ My Group ⚜️", url="https://t.me/Tg_Hydra_Galaxy")],
        [InlineKeyboardButton(
            "⚜️ My Channel ⚜️", url="https://t.me/Tg_Hydra_Galaxy")]
    ])
    welcomed = f"Hey <b>{message.from_user.first_name}</b>\n/help for More info"
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
