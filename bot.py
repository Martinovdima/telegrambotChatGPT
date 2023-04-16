import telebot
import openai
import api_tokens

# Предоставляем ключ API telegram
bot = telebot.TeleBot(api_tokens.bot_token)
# Предоставляем ключ API chatGPT
openai.api_key = api_tokens.ai_token

# Выбираем обученную модель
engine = 'text-davinci-003'


# Response an ChatGPT
def ask(prompt):
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
    bot.send_message(message.from_user.id, response)


bot.polling(none_stop=True, interval=0)
