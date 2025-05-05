def count_words(text):
    return len(text.split())

def get_char_counts(text):
    char_counts = {}
    for char in text.lower():
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts

def get_sorted_char_counts(char_counts):
    sorted_counts = sorted(
        [{"char": char, "num": count} for char, count in char_counts.items() if char.isalpha()],
        key=lambda x: x["num"],
        reverse=True
    )
    return sorted_counts

