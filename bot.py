from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

YOUR_CHAT_ID = 5291833531  # kullanıcı ID'nizi buraya girin

def start(update: Update, context: CallbackContext) -> None:
    # yalnızca belirli bir kullanıcı id'sine cevap verin
    if update.message.chat_id != YOUR_CHAT_ID:
        return
    
    context.user_data['link'] = None
    context.user_data['score'] = None
    context.user_data['time'] = None
    
    update.message.reply_text('Lütfen oyun linkinizi girin:')

def receive_link(update: Update, context: CallbackContext) -> None:
    # yalnızca belirli bir kullanıcı id'sine cevap verin
    if update.message.chat_id != YOUR_CHAT_ID:
        return
    
    link = update.message.text
    context.user_data['link'] = link
    update.message.reply_text('Lütfen skorunuzu girin:')

def receive_score(update: Update, context: CallbackContext) -> None:
    # yalnızca belirli bir kullanıcı id'sine cevap verin
    if update.message.chat_id != YOUR_CHAT_ID:
        return
    
    score = update.message.text
    context.user_data['score'] = score
    update.message.reply_text('Lütfen zamanınızı girin:')

def receive_time(update: Update, context: CallbackContext) -> None:
    # yalnızca belirli bir kullanıcı id'sine cevap verin
    if update.message.chat_id != YOUR_CHAT_ID:
        return
    
    time = update.message.text
    context.user_data['time'] = time
    
    # kullanıcıdan tüm gerekli bilgileri aldık, update_game() fonksiyonunu kullanarak oyun verilerini güncelleyin
    link = context.user_data['link']
    score = context.user_data['score']
    time = context.user_data['time']
    result = update_game(link, score, time)
    
    # sonucu kullanıcıya gönderin
    update.message.reply_text(result)

def update_game(link, score, time):
    # game.py'yi çalıştırmak için subprocess kullanın
    import subprocess
    command = ["python", "game.py", "-u", link, "-s", score, "-t", time]
    result = subprocess.run(command, capture_output=True, text=True)
    return result.stdout

def stop(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Bot durdu')
    updater.stop()

def main():
    global updater
    updater = Updater(token='6121066413:AAHtdPHa-F54RN-HYb3fmOpuzBzifCpvqwM', use_context=True)

    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(MessageHandler(Filters.regex(r'^https?://'), receive_link))
    updater.dispatcher.add_handler(MessageHandler(Filters.regex(r'^\d+$'), receive_score))
    updater.dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, receive_time))
    updater.dispatcher.add_handler(CommandHandler('stop', stop))

    updater.start_polling()
    print('Bot çalışıyor')
    updater.idle()

if __name__ == '__main__':
    main()
