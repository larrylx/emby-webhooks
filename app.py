from flask import Flask, request
import json
import requests

from config.config import Config


def send_to_tg(message):
    url = "https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={channel_id}&text={message}".format(
        TOKEN=Config.TOKEN,
        channel_id=Config.channel_id,
        message=message
    )

    print(requests.get(url).json())

    return "OK"


app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def handle_webhook():

    # print(request.headers)
    # print(request.data)
    # print(request.form)

    data = json.loads(request.form["data"])

    if data["Event"] == "library.new":
        return "OK"

    elif data["Event"] == "system.webhooktest":

        message = 'Genres: {genres}\n\nChannel: {channel_id}\n\nhttps://www.imdb.com/title/tt13362962'.format(
            genres="Comedy, Drama, Sport",
            channel_id=Config.channel_id    
        )

        # send_to_tg(message)
        print(message)

        return "OK"


if __name__ == '__main__':
    app.run()
