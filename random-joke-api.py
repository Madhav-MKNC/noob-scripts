# this api returns a random joke each time when called

# api: https://jokes-api.gamhcrew.repl.co/

from flask import Flask
import random
import requests

app = Flask(__name__)

response = requests.get("https://raw.githubusercontent.com/j4rvice/jokes-api/main/jokes.txt")
all_jokes = [i for i in response.text.split('\n') if len(i) > 0]

@app.route('/')
def home():
    return random.choice(all_jokes)

app.run(host="0.0.0.0", port=80, debug=True)
