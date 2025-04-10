from stats import get_num_words, get_num_characters, order_characters
import sys
#import stats

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def main():
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    characters = get_num_characters(text)
    char_order = order_characters(characters)
    report(book_path, num_words, char_order)
    
    
    #print(char_order)

def report(book_path,num_words, char_order):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count-----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count ---------")
    for key, value in char_order:
        if key.isalpha():
            print(f"{key}: {value}")
    print("============= END =============")
    
def get_book_text(file):
    with open(file) as f:
        return f.read()
    
          
main()