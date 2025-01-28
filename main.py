with open("books/frankenstein.txt") as f:
    file_contents = f.read()


word_count = len(file_contents.split())

print(word_count)