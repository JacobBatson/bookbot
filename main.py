from stats import number_of_words
from stats import number_of_each_character
from stats import sorted_character_count

import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    filepath = sys.argv[1]

    text = get_book_text(filepath)

    print(text)
    number_of_words(text)
    
    char_counts = number_of_each_character(text)
    print(char_counts)

    sorted_counts = sorted_character_count(char_counts)
    for item in sorted_counts:
        print(f"{item['char']}: {item['count']}")

main()