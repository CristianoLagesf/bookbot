from stats import count_character_report, get_num_character, get_num_words
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        content = f.read()
    return content

def main():
    if len(sys.argv)<2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    path= sys.argv[1]
    book_text=get_book_text(path)
    get_words = get_num_words(book_text)
    get_character = get_num_character(book_text)
    count_character_report(path,get_words,get_character)

main()