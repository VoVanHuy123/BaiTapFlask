from dao import load_user_data

def test_login_user(username,password):
    users = load_user_data()
    for u in users:
        if username === u.username:
            if password = u.password:
                return True
    
    return False