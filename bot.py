import telebot

TOKEN = "8007632874:AAGuoX83Wsh6-Re0fbiXP6WseiQHHbA0r0k"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(content_types=['video', 'document', 'photo', 'audio'])
def get_file_id(message):
    if message.video:
        file_id = message.video.file_id
    elif message.document:
        file_id = message.document.file_id
    elif message.photo:
        file_id = message.photo[-1].file_id
    elif message.audio:
        file_id = message.audio.file_id
    else:
        file_id = "Fayl topilmadi."

    bot.reply_to(message, f"File ID: {file_id}", parse_mode="Markdown")

bot.polling()


