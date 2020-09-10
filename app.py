from flask import Flask
import json
import requests


app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


def api():
    request = requests.get("https://matchilling-chuck-norris-jokes-v1.p.rapidapi.com/jokes/random")
    request_text = request.text

    data = json.loads(request_text)
    print(data)


if __name__ == '__main__':
    app.run()
