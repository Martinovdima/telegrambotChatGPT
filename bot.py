import telebot
import openai
import sqlite3

import config

# Add API telegram
bot = telebot.TeleBot(config.TOKEN)
# Add API chatGPT
openai.api_key = config.OPEN_AI
# Add ChatGPT version
engine = config.ENGINE
# Name database
db_filename = config.name_db


def write_to_db(message):
    """
    Writes the message data to a SQLite database.

    Args:
        message (telegram.Message): The Telegram message object to write to the database.

    Returns:
        None
    """
    create_table()
    conn = sqlite3.connect(db_filename)
    cursor = conn.cursor()
    select_id = cursor.execute(
        "SELECT id FROM user WHERE chat_id = ?", (str(message.chat.id),)
    )
    select_id = select_id.fetchone()
    if select_id:
        try:
            cursor.execute(
                "UPDATE user SET last_msg=?, last_login=? WHERE chat_id=?",
                (
                    message.text,
                    str(message.date),
                    str(message.chat.id),
                ),
            )
        except:
            conn.commit()
            conn.close()
            bot.send_message(
                687975907,
                f"Ошибка при добавлении (INSERT) данных в базе Пользователь: {message.chat.id}",
            )
    else:
        try:
            cursor.execute(
                "INSERT INTO user (chat_id, last_login, username, first_name, last_name, last_msg) VALUES (?,?,?,?,?,?)",
                (
                    str(message.chat.id),
                    str(message.date),
                    message.chat.username if message.chat.username else "-",
                    message.chat.first_name
                    if message.chat.first_name
                    else "-",
                    message.chat.last_name if message.chat.last_name else "-",
                    message.text,
                ),
            )
        except:
            conn.commit()
            conn.close()
            bot.send_message(
                687975907,
                f"Ошибка при добавлении (INSERT) данных в базе Пользователь: {message.chat.id}",
            )
    conn.commit()
    conn.close()


def create_table():
    """Create table if not exists."""
    conn = sqlite3.connect(db_filename)
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS user(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            chat_id TEXT,
            last_login TEXT,
            username TEXT,
            first_name TEXT,
            last_name TEXT,
            last_msg TEXT
        );
        """
    )
    conn.commit()
    conn.close()


def ask(prompt):
    """Response an ChatGPT"""
    completion = openai.Completion.create(engine=engine,
                                          prompt=prompt,
                                          temperature=0.5,
                                          max_tokens=1000)
    return completion.choices[0]['text']


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.from_user.id, 'Привет, я Тимо')


@bot.message_handler(content_types=['photo'])
def text_handler(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, 'Красиво')


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    response = ask(message.text)
    write_to_db(message)
    bot.send_message(message.from_user.id, response)


bot.polling(none_stop=True, interval=0)
