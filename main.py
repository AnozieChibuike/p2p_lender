import json
import openai
from flask import Flask, request, jsonify
from pymongo.mongo_client import MongoClient
import dotenv
import os
from unratedwriting import typewrite
from flask_cors import CORS



dotenv.load_dotenv()
uri = os.getenv('mongo_db_uri')
openai.api_key = os.getenv('open_ai_api_key')

app = Flask(__name__)

CORS(app)
# Create a new client and connect to the server
client = MongoClient(uri)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
    exit()

db = client.test
collection = db.user


class Chatbot:
    def __init__(self, username, history, user_message):
        self.username = username
        self.user_message = user_message
        self.conversation_history = history

    def process_user_message(self):
        collection.update_one({"username": self.username}, {"$push": {"conversation_history": {"role":"user","content": self.user_message}}})
        # for _ in range(3):  # Retry the request up to 3 times
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=self.conversation_history
        )

        bot_response = response['choices'][0]['message']["content"].replace('\n',' ')
        collection.update_one({"username": self.username}, {"$push": {"conversation_history": {"role":"assistant","content":bot_response}}})
        return bot_response


@app.post('/bot')
def bot():
    username = request.json.get('username')
    message = request.json.get('message')
    if not username:
        return jsonify({'message': 'Username missing in parameter', 'status_message': 'Bad Request'}), 400
    if not message or message == '':
        return jsonify({'message': 'Message missing in parameter', 'status_message': 'Bad Request'}), 400

    user = collection.find_one({'username': username})
    if user is None:
        collection.insert_one({"username": username, "conversation_history":[{"role":"system","content":"You are a Microfinance platform that handle p2p lending(both parties can negotiate the interest to time of the loan), microfinance services"},
                                                                             {"role":"user","content":"Who are you?"},
                                                       {"role":"assistant","content":"We are a Microfinance platform that handle p2p lending and other microfinance services"}
            ]
            })
    user = collection.find_one({'username': username})
    username = user['username']
    history = user['conversation_history']
    print(history)
    robot = Chatbot(username,history,message)
    bot_response = robot.process_user_message()

    return json.dumps({"bot_response": bot_response}), 201

# from . import loan

if __name__ == "__main__":
    typewrite("Server spinning up.., I pledge my loyalty to the emperor (v1.0)")
    app.run(host='0.0.0.0')
