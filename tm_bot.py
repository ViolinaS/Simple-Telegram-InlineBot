import hashlib
import os
from dotenv import load_dotenv, find_dotenv
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import InputTextMessageContent, InlineQueryResultArticle, InlineQuery
from youtube_search import YoutubeSearch
import random

load_dotenv(find_dotenv())

scratching_bot = Bot(token=os.getenv('telegram_bot_token'))
dp = Dispatcher(scratching_bot)


def search(text):
    youtube_search = YoutubeSearch(text, max_results=20).to_dict()
    return youtube_search


@dp.inline_handler()
async def inline_query_youtube(query: InlineQuery):
    random_query = ['Новые видео на канале Netflix', 'Самые красивые места в мире 8K ULTRA HD',
                    'Новые видео на канале Okko', 'Hulu', 'маша и медведь новые серии']
    links = search(text=query.query or random.choice(random_query))
    articles = [InlineQueryResultArticle(
        id=hashlib.md5(f'{link["id"]}'.encode()).hexdigest(),
        title=f'{link["title"]}',
        url=f'https://www.youtube.com/watch?v={link["id"]}',
        thumb_url=f'{link["thumbnails"][0]}',
        input_message_content=InputTextMessageContent(
                message_text=f'https://www.youtube.com/watch?v={link["id"]}')
    ) for link in links]

    await query.answer(results=articles, cache_time=60, is_personal=True)




executor.start_polling(dp, skip_updates=True)
