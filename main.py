from stats import num_words, char_count, sort_char_count
import sys



def get_book_text(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book_path = sys.argv[1]
    
    print("================== BOOKBOT =================")
    # Use the relative path based on your folder structure
    book_text = get_book_text(book_path)
    word_count = num_words(book_text)
    print("-------------- Word Count --------------")
    print("Found", word_count, "total words")
    character_count = char_count(book_text)
    sorted_character_count = sort_char_count(character_count)
    print("----------- Character Count -----------")
    for char, count in sorted_character_count:
        print(f"{char}: {count}")



if __name__ == "__main__":
    main()
