
**version 1.0.0
ќписание**
Ётот Telegram-бот представл€ет собой программу, котора€ позвол€ет отвечать на запросы пользователей в виде текста, использу€ искусственный интеллект OpenAI ChatGPT.

**‘ункциональность**
Ѕот использует api_key OpenAI ChatGPT дл€ генерации ответов на запросы пользователей. ѕользователи могут отправл€ть запросы боту в текстовом формате, а бот в свою очередь генерирует и отправл€ет ответы в текстовом формате.

**»спользование**
„тобы использовать бота, пользователь должен написать сообщение боту в чате. Ѕот будет автоматически обрабатывать сообщение и генерировать ответ с использованием OpenAI ChatGPT. ќтвет будет отправлен обратно в чат пользователю в виде текста.

**«ависимости**
ƒл€ работы бота требуетс€ наличие api_key OpenAI ChatGPT и доступ к Telegram API дл€ отправки и получени€ сообщений.

**ќграничени€**
Ѕот может быть ограничен по использованию API OpenAI ChatGPT. ќграничени€ могут включать в себ€ лимиты на количество запросов в единицу времени или на количество запросов от одного api_key.

**–екомендации**
–екомендуетс€ использовать уникальные api_key дл€ каждого пользовател€, чтобы избежать проблем с доступностью и производительностью API OpenAI. “акже рекомендуетс€ рассмотреть возможность использовани€ кэшировани€ результатов запросов, чтобы уменьшить количество обращений к API OpenAI. 

**Description**
This Telegram bot is a program that allows to respond to user requests in text format using OpenAI ChatGPT API.

**Functionality**
The bot uses the OpenAI ChatGPT api_key to generate responses to user requests. Users can send text requests to the bot, and the bot generates and sends responses back in text format.

**Usage**
To use the bot, a user should send a message to the bot in the chat. The bot will automatically process the message and generate a response using OpenAI ChatGPT. The response will be sent back to the user in the chat as text.

**Dependencies**
To run the bot, it is necessary to have the OpenAI ChatGPT api_key and access to the Telegram API to send and receive messages.

**Limitations**
The bot may be limited in its use of the OpenAI ChatGPT API. Limitations may include limits on the number of requests per unit of time or on the number of requests from a single api_key.

**Recommendations**
It is recommended to use unique api_key for each user to avoid issues with API OpenAI availability and performance. It is also recommended to consider using caching of the results of requests to reduce the number of API OpenAI calls.


**Function description:**

The function "write_to_db" takes a single argument "message" and is used to write data to a SQLite database.

The function first checks if the database file exists using the "os.path.exists" method. If the file does not exist, a new connection is established to the database file using "sqlite3.connect" and a new cursor is created. If the file already exists, the function simply connects to the database and creates a new cursor.

The function then executes a SELECT query on the "user" table of the database to check if a record exists with the chat ID of the message passed to the function. If a record exists, an UPDATE query is executed to update the "last_msg" and "last_login" columns of the record with the values of the message text and date, respectively. If the UPDATE query fails, the function commits the transaction, closes the connection to the database, and sends a message to a specific user with an error message.

If a record with the chat ID of the message does not exist in the "user" table, an INSERT query is executed to insert a new record into the table with the chat ID, date, username, first name, last name, and message text of the message. If the INSERT query fails, the function commits the transaction, closes the connection to the database, and sends a message to a specific user with an error message.

Finally, the function commits the transaction and closes the connection to the database.

Note: This function assumes that the global variable "bot" is defined and is an instance of the Telegram Bot API.


