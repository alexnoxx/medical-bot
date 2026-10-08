from telegram import Update
from telegram.ext import ContextTypes

from Models.TodoList import todo_list
from Models.todo import Todo

class TodoController:

    @staticmethod
    async def add_todo(update: Update, context: ContextTypes.DEFAULT_TYPE):
        command = update.message.text.split()[0]
        title = "".join(update.message.text.split(command)[1])    
        todo_list.append(Todo(title))
        await update.message.reply_text("Nota agregada")

    async def list_todo(update: Update, context: ContextTypes.DEFAULT_TYPE):
            if(len(todo_list) == 0):
                 await update.message.reply_text("No hay tareas")
                 return
            answer = ''
            for i, todo in enumerate(todo_list):
                  answer = answer + f"{i+1} - {'✅' if todo.is_completed else '⭕'} {todo.title} \n"
            await update.message.reply_text(answer)

    async def list_opciones(update: Update, context: ContextTypes.DEFAULT_TYPE):
         await update.message.reply_text('/list: Listar todas las tareas \n /add [tarea]: Añadir una nueva tarea')