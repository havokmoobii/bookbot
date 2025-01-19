def main():
    file_path = "books/frankenstein.txt"
    file_contents = get_book_text(file_path)

    print(get_word_count(file_contents))
    print(get_char_count(file_contents))

def get_word_count(document):
    words = document.split()
    return len(words)

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