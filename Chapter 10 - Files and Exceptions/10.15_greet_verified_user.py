from pathlib import Path
import json

path = Path("user_directory.json")

try:
    data = json.loads(path.read_text(encoding="utf-8"))
except FileNotFoundError:
    print("No user_directory.json found yet.")
except json.JSONDecodeError:
    print("Could not parse JSON in user_directory.json.")
else:
    username = input("Enter your username: ")

    # Normalize data to a list of user dicts
    users = data if isinstance(data, list) else [data]

    # Find the user
    match = next((u for u in users if u.get("username") == username), None)

    if match:
        first = match.get("first_name", "").title()
        last = match.get("last_name", "").title()
        print(f"Welcome back, {first} {last} ({username})!")
    else:
        print(f"No record found for username: {username}")
