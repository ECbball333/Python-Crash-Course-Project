

from pathlib import Path
import json

path = Path("user_directory.json")

# Load existing list (or start a new one)
if path.exists():
    existing = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(existing, list):
        existing = [existing]   # in case the file used to store a single object
else:
    existing = []

username = input("What is your username? ")
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

user = {
    "username": username,
    "first_name": first_name.title(),
    "last_name": last_name.title(),
}

existing.append(user)
path.write_text(json.dumps(existing, indent=2), encoding="utf-8")

print(f"We'll remember you when you come back, {username}!")
