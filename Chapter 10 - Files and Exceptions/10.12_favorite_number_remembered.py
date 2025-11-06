from pathlib import Path
import json

numbers = input("\nWhat is your favorite number? ")

def favorite_number():
    """Ask for number from user"""
    path = Path('numbers.json')
    contents =json.dumps(numbers)
    path.write_text(contents)

def read_number():
    """Tell user their number"""
    path = Path('numbers.json')
    contents = path.read_text()
    print(f"\nI know your favorite number! It is {contents}! ")

favorite_number()
read_number()