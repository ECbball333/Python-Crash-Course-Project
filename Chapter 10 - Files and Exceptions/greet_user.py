from pathlib import Path
import json

def get_stored_username(path):
    """Get stored username if available"""
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        return username
    else:
        return None

# Refactored
def greet_user():
    """Greet the user by name"""
    # Saving User Generated Data
    path = Path('username.json')
    #if path.exists():
    #    contents = path.read_text()
    username = get_stored_username(path)
    if username:
        print(f"Welcome back, {username.title()}")

    else:
        username = input("What is your name? ")
        contents = json.dumps(username)
        path.write_text(contents)
        print(f"We'll remember yo when you come back, {username.title()}")


greet_user()




