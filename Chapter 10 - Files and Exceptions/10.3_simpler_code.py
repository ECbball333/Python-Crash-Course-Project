from pathlib import Path

path = Path('pi_digits.txt')
contents = path.read_text().rstrip()

for line in contents.splitlines():
    print(line)