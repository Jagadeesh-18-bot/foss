#  Overview
This code defines a Telegram bot that interacts with users to provide book information. The bot uses the Google Books API to search for books based on genres and provides various commands for user interaction.

**requests: A library to make HTTP requests, used here to interact with the Google Books API.**
**telegram.ext: Part of the python-telegram-bot library used to create and manage the Telegram bot, handle commands, and process messages.**
**Parameters: genre – A string representing the genre to search for (e.g., "science fiction").**

## 1. Description: Fetches a list of books from the Google Books API based on the specified genre.
Parameters:
genre: A string representing the genre of books to search for.
Returns:
A list of books that match the genre query.

## 2. format_book_details(book)
Description: Formats the details of a single book into a readable string.
Parameters:
book: A dictionary representing a book's data retrieved from the Google Books API.
Returns:
A formatted string containing the title, author, description, published year, language, and preview link of the book.

## 3. handle_start(update, context)
Description: Handles the /start command. Sends a welcome message to the user.
Parameters:
update: Contains information about the incoming update (e.g., message).
context: Provides context for the callback function, including the bot instance.

## 4. handle_book(update, context)
Description: Handles the /book command. Prompts the user to provide a book title or author for a search query.
Parameters:
update: Contains information about the incoming update (e.g., message).
context: Provides context for the callback function, including the bot instance.

## 5. handle_preview(update, context)
Description: Handles the /preview command. Asks the user to provide a book title or author to preview.
Parameters:
update: Contains information about the incoming update (e.g., message).
context: Provides context for the callback function, including the bot instance.

## 6. handle_list(update, context)
Description: Handles the /list command. Sends a message indicating that a list of popular books will be provided.
Parameters:
update: Contains information about the incoming update (e.g., message).
context: Provides context for the callback function, including the bot instance.

## 7. handle_reading_list(update, context)
Description: Handles the /reading_list command. Sends a message indicating that the user's reading list will be provided.
Parameters:
update: Contains information about the incoming update (e.g., message).
context: Provides context for the callback function, including the bot instance.

## 8. handle_help(update, context)
Description: Handles the /help command. Sends a message providing information about available commands and their functions.
Parameters:
update: Contains information about the incoming update (e.g., message).
context: Provides context for the callback function, including the bot instance.

## 9. handle_genre_query(update, context)
Description: Handles text messages that are interpreted as genre queries. Retrieves book details based on the genre provided by the user and sends the details of up to 5 books or informs the user if no books are found.
Parameters:
update: Contains information about the incoming update (e.g., message).
context: Provides context for the callback function, including the bot instance.

## 10. main()
Description: Sets up and runs the Telegram bot. Configures the bot with handlers for different commands and starts polling for updates.
Process:
Creates an Application instance with the bot token.
Adds command handlers (/start, /book, /preview, /list, /reading_list, /help) and a message handler for text messages.
Starts polling to receive and handle updates from Telegram.

## 11. if __name__ == "__main__":
Description: Ensures that the main() function is called only when the script is executed directly (not when imported as a module).
Process:
Calls the main() function to start the bot.

These are all the functions I learned about and became familiar with while working on the task and writing the code.

# 🔭
