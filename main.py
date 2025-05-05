import sys
from stats import count_words, get_char_counts, get_sorted_char_counts

def get_book_text(path):
    with open(path, 'r') as f:
        return f.read()

def main():
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    # Get the book path from the command-line argument
    book_path = sys.argv[1]

    try:
        # Read the book text
        book_text = get_book_text(book_path)
    except FileNotFoundError:
        print(f"Error: The file '{book_path}' was not found.")
        sys.exit(1)

    # Get word count
    num_words = count_words(book_text)

    # Get character counts
    char_counts = get_char_counts(book_text)

    # Get sorted character counts
    sorted_char_counts = get_sorted_char_counts(char_counts)

    # Print the report
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for entry in sorted_char_counts:
        print(f"{entry['char']}: {entry['num']}")
    print("============= END ===============")

if __name__ == "__main__":
    main()