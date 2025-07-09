import json

def load_user_data():
    with open("data/users.json", encoding="utf-8") as f:
        return json.load(f)