from flask import Flask
import json
import requests



app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/webhook', methods=['POST'])
def webhook():
  return {
        "fulfillmentText": 'This is from the ifedha webhook',
        "source": 'webhook'
    }


if __name__ == '__main__':
    app.run()
