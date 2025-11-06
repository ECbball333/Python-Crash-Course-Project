from pathlib import Path
import json

username = input("What is your username? ")
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

user = {
    "username": username,
    "first_name": first_name,
    "last_name": last_name
}

path = Path('user_directory.json')
contents = json.dumps(user, indent=2)
path.write_text(contents, encoding="utf-8")

print(f"We'll remember you when you come back, {username.title()}! ")


