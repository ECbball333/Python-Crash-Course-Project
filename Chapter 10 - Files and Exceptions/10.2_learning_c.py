from pathlib import Path

path = Path('learning_python.txt')

contents = path.read_text().rstrip()
new_content = contents.replace('Python', 'Java')

print(new_content)


