import os
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

logging.basicConfig(level=logging.INFO)
TOKEN = os.getenv('TOKEN')

LINKS = {
    "ME1-2017": "https://www.mediafire.com/file/zhhtlbpxvh3iu2l/ME1-2017.pdf?dl=1",
    "ME1-2018": "https://www.mediafire.com/file/rc6rwiwgwjktyrg/ME1-2018.pdf?dl=1",
    "ME1-2019": "https://www.mediafire.com/file/1wj6x27k2auteay/ME1-2019.pdf?dl=1"
}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    kb = [[InlineKeyboardButton("📚 GATE ME", callback_data="GATE")]]
    await update.message.reply_text("🎓 GATE Bot", reply_markup=InlineKeyboardMarkup(kb))

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    q = update.callback_query
    await q.answer()
    if q.data == "GATE":
        kb = [[InlineKeyboardButton(k, callback_data=k)] for k in LINKS]
        await q.edit_message_text("Select:", reply_markup=InlineKeyboardMarkup(kb))
    else:
        await q.edit_message_text(f"[⬇️ {q.data}]({LINKS[q.data]})", 
                                parse_mode='Markdown', disable_web_page_preview=True)

if __name__ == '__main__':
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button))
    app.run_polling()
