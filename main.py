import sys
from stats import get_num_words, count_characters, sort_key, sort_character_dict

if len(sys.argv) != 2:
    print(f"Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(file_path):
    with open(file_path) as file:
        return file.read()

def main():
    file_path = sys.argv[1]
    text = get_book_text(file_path)
    num_words = get_num_words(text)
    character_dict = count_characters(text)
    sorted_characters = sort_character_dict(character_dict)

    print("==========BOOKBOT==========")
    print("")
    print(f"Analyzing book found at {file_path}...")
    print("")
    print("-------- Word Count --------")
    print("")
    print(f"Found {num_words} total words")
    print("")
    print("----- Character Count ------")
    print("")
    for i in range(0, len(sorted_characters)):
        next_dictionary = sorted_characters[i]
        print(f"{next_dictionary["char"]}: {next_dictionary["num"]}")
    print("")
    print("=========== END ===========")
    
main()