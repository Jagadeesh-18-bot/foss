import requests
from telegram.ext import Application, CommandHandler, MessageHandler, filters

# API code and Telegram token
TOKEN = "7345140891:AAH4ZfzVbgBJOaLas7335weQ2_59cg1mAZ0"
GOOGLE_BOOKS_API_KEY = "AIzaSyD8tBlntI000hDwTECmD-ILT8xTKGewG2g"

def get_books_by_genre(genre):
    url = f"https://www.googleapis.com/books/v1/volumes?q=subject:{genre}&key={GOOGLE_BOOKS_API_KEY}"
    response = requests.get(url)
    data = response.json()
    books = data.get("items", [])
    return books



def format_book_details(book):
    title = book["volumeInfo"]["title"]
    author = book["volumeInfo"]["authors"][0]
    description = book["volumeInfo"]["description"]
    published_year = book["volumeInfo"]["publishedDate"][:4]
    language = book["volumeInfo"]["language"]
    preview = book["volumeInfo"]["previewLink"]
    return f"*{title}* by {author}\n{description}\nPublished: {published_year}\nLanguage: {language}\nPreview: {preview}"

async def handle_start(update, context):
    await context.bot.send_message(chat_id=1311230247, text="Welcome to BookBot! Use /help for commands.")

async def handle_book(update, context):
    await context.bot.send_message(chat_id=1311230247, text="Please provide a book title or author to search for.")

async def handle_preview(update, context):
    await context.bot.send_message(chat_id=1311230247, text="Please provide a book title or author to preview.")

async def handle_list(update, context):
    await context.bot.send_message(chat_id=1311230247, text="Here's a list of popular books.")

async def handle_reading_list(update, context):
    await context.bot.send_message(chat_id=1311230247, text="Here's your reading list.")

async def handle_help(update, context):
    await context.bot.send_message(chat_id=1311230247, text="/start - Welcome message\n/book - Search for books\n/preview - Preview a book\n/list - List of popular books\n/reading_list - Your reading list\n/help - Help text")

async def handle_genre_query(update, context):
    print("Message Recieved!")
    genre = update.message.text
    books = get_books_by_genre(genre)
    if books:
        for book in books[:5]:  # Show 5 books
            await context.bot.send_message(chat_id=1311230247, text=format_book_details(book))
    else:
        await context.bot.send_message(chat_id=1311230247, text="No books found in this genre.")

def main():
    print("Bot started")
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", handle_start))
    application.add_handler(CommandHandler("book", handle_book))
    application.add_handler(CommandHandler("preview", handle_preview))
    application.add_handler(CommandHandler("list", handle_list))
    application.add_handler(CommandHandler("reading_list", handle_reading_list))
    application.add_handler(CommandHandler("help", handle_help))
    application.add_handler(MessageHandler(filters.TEXT, handle_genre_query))
    application.run_polling()

if __name__ == "__main__":
    main()
