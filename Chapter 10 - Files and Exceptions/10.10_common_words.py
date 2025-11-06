from pathlib import Path

def read_files(path):
    """Read the contents of a file"""
    try:
        content = path.read_text(encoding="utf-8")
    except FileNotFoundError:
        pass

    text = content.lower()

    # Replace common punctuation with spaces so we split into clean words
    for ch in ",.;:!?\"'()[]{}-":
        text = text.replace(ch, " ")

        # Now split into words and count exact matches
        words = text.split()
        count = words.count("the")
        print(count)
        return count


path = Path('moby_dick.txt')

read_files(path)