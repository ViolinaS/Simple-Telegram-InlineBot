# Простой Inline bot для Telegram
Bot searches Youtube content and sends info and links to selected recipient
## Бот выполняет поиск информации на Youtube по заданному слову или словам и отправляет ссылки выбранному пользователю в Телеграм

---

### Шаги для запуска Бота:
- Зарегестрировать Бота в Telegramm [согласно иструкции](https://tlgrm.ru/docs/bots#botfather)
- Ключ (токен) для бота подставить в файл [tm_bot.py](https://github.com/ViolinaS/Simple-Telegram-InlineBot/blob/main/tm_bot.py):

``scratching_bot = Bot(token=os.getenv('здесь ваш токен'))``
  
  *сначала нужно создать файл .env и поместить в него токен либо переделать код без использования os.getenv/dotenv*
  
  

- Установить библиотеки из [requirements.txt](https://github.com/ViolinaS/Simple-Telegram-InlineBot/blob/main/requirements.txt)
- В настройках Бота (использовать @BotFather) указать /setprivacy и /setinline
- Информация по использованию Инлайн Бота - [Инлайн-режим](https://tlgrm.ru/docs/bots#inline-mode)
