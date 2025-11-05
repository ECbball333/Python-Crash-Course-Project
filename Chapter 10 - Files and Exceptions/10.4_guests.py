from pathlib import Path

path = Path('guest.txt')

name = input("Enter your name: ")
path.write_text(name)