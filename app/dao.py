import json
import os
def load_user_data():
    file_path = os.path.join(os.path.dirname(__file__), 'data', 'users.json')
    with open(file_path, encoding="utf-8") as f:
    # with open("../data/users.json", encoding="utf-8") as f:
        return json.load(f)

def auth_user(username,password):
    users = load_user_data()
    for u in users:
        if username == u["username"]:
            if password == u["password"]:
                return True
    
    return False