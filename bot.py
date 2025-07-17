from aiogram import Bot, Dispatcher, types, executor

API_TOKEN = '7951952131:AAG3vNMGPnJQCw8rJLPy-_2ozGF3XK6W9Yg'  # ← токен от @BotFather
ADMIN_ID = 1024266193  # ← твой Telegram ID

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler()
async def relay_message(message: types.Message):
    if message.from_user.id == ADMIN_ID and message.reply_to_message:
        original_user = message.reply_to_message.forward_from
        if original_user:
            await bot.send_message(original_user.id, message.text)
        else:
            await message.reply("⚠️ Не удалось определить пользователя.")
    elif message.from_user.id != ADMIN_ID:
        await bot.forward_message(chat_id=ADMIN_ID, from_chat_id=message.chat.id, message_id=message.message_id)
        await message.reply("✉️ Ваше сообщение отправлено администратору.")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
