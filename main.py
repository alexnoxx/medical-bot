from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from telegram import Update

from Controller.TodoController import TodoController

TOKEN = "8901029438:AAF6yndFUvD5jT-ghCHiXGd9kSyC_ZGUBZQ"

async def say_hello(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("hola bot")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(update.message.text)

application = ApplicationBuilder().token(TOKEN).build()
application.add_handler( CommandHandler("add", TodoController.add_todo) )
application.add_handler( CommandHandler("list", TodoController.list_todo) )
application.add_handler( CommandHandler("options", TodoController.list_opciones) )

application.run_polling(allowed_updates=Update.ALL_TYPES)