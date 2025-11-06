from pathlib import Path

def read_names(path):
    """Read the names of cats and dogs from a text file."""
    try:
        content = path.read_text(encoding="utf-8")
    except FileNotFoundError:
        pass
    else:
        print(content)


filenames = ['cats.txt', 'dogs.txt']
for filename in filenames:
    path = Path(filename)
    read_names(path)

