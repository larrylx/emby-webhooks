import asyncio
import json
from flask import Flask, request
from jinja2 import Environment, FileSystemLoader
from telegram import Bot
from telegram.constants import ParseMode

from config.config import Config

async def send_to_tg(message):
    bot = Bot(token=Config.TOKEN)

    await bot.send_message(chat_id=Config.channel_id, text=message, parse_mode=ParseMode.HTML)

    return "OK"


app = Flask(__name__)


@app.route('/webhook', methods=['POST'])
def handle_webhook():

    data = json.loads(request.form["data"])

    print(data)

    env = Environment(loader=FileSystemLoader("templates"))

    if data["Event"] == "library.new":
        if data["Item"]["Type"] == "Episode":
            template = env.get_template("series.html")

            html_message = template.render(**data)
            asyncio.run(send_to_tg(html_message))

        elif data["Item"]["Type"] == "Movie":
            template = env.get_template("movie.html")

            html_message = template.render(**data)
            asyncio.run(send_to_tg(html_message))
        
        return "OK"

    elif data["Event"] == "system.webhooktest":
        data.update({"Item": {"ParentIndexNumber": 1, "IndexNumber": 3}})

        template = env.get_template("example.html")

        html_message = template.render(**data)
        asyncio.run(send_to_tg(html_message))

        return "OK"


if __name__ == '__main__':
    app.run()
