from pathlib import Path
import json

numbers = input("\nWhat is your favorite number? ")

def favorite_number():
    """Ask for number from user"""
    path = Path('numbers.json')
    contents =json.dumps(numbers)
    path.write_text(contents)


favorite_number()