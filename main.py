from stats import count_words

def get_book_text(path):
   with open(path) as f:
      return f.read()

def main():
    print(get_book_text('books/frankenstein.txt'))
    print(f"Found {count_words(get_book_text('books/frankenstein.txt'))} total words")
    
main()