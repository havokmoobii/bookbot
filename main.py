def main():
    file_path = "books/frankenstein.txt"
    file_contents = get_book_text(file_path)

    print_report(file_path, file_contents)

def print_report(file_path, document):
    print(f"--- Begin report of {file_path} ---")
    print(f"{get_word_count(document)} words found in document.")
    print()

    char_dict = sort_dict(document)

    for char_entry in char_dict:
        print(f"The '{char_entry["name"]}' character was found {char_entry["num"]} times")

    print("--- End report ---")

def get_word_count(document):
    words = document.split()
    return len(words)

def sort_dict(document):
    char_count = get_char_count(document)

    char_list = []

    for char_entry in char_count:
        if char_entry.isalpha():
            char_list.append({"name": char_entry, "num": char_count[char_entry]})

    char_list.sort(reverse=True, key=sort_on)

    return char_list

def sort_on(dict):
    return dict["num"]

def get_char_count(document):
    document = document.lower()

    chars = {}

    for character in document:
        if chars.get(character) is None:
            chars[character] = 0
        chars[character] += 1

    return(chars)

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()