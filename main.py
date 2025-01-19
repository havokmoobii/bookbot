def main():
    file_contents = 0

    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

    words = file_contents.split()
    print(len(words))
    print(count_characters(file_contents))

def count_characters(document):
    document = document.lower()

    out_dic = {}

    for character in document:
        if out_dic.get(character) is None:
            out_dic[character] = 0
        out_dic[character] += 1

    return(out_dic)

main()