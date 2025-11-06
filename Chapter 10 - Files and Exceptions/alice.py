
from pathlib import Path

#path = Path('alice.txt')

def count_words(path):
    """Count the approximate words in a file."""
    try:
        contents = path.read_text(encoding="utf-8")
    except FileNotFoundError:
        #print(f'\nSorry, the file {path} does not exist.')
        pass # Will not display error message to user #
    else:
        # Count the approximate number of words in the file:
        words = contents.split()
        num_words = len(words)
        print(f'The file {path} has about {num_words} words. ')

filenames = ['siddhartha.txt', 'alice.txt', 'little_women.txt', 'moby_dick.txt']
for filename in filenames:
    path = Path(filename)
    count_words(path)


