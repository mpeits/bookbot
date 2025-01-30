characters = {
" ": 0,
}

with open("books/frankenstein.txt") as f:
    file_contents = f.read()


word_count = len(file_contents.split())
words = file_contents.split()

for i in file_contents:
    if i == " ":
        characters[" "] += 1

for i in words:
    for j in i:
        j = j.lower()
        if j in characters:
            characters[j] += 1
        else:
            characters[j] = 1

character_list = list(characters.items())

character_list.sort(key=lambda x: x[1], reverse=True)

print("--- Begin report of books/frankenstein.txt ---")

print(f"{word_count} words found in the document\n")

for i in character_list:
    (letter, amount) = i
    if letter.isalpha():
        print(f"The \'{letter}\' character was found {amount} times")

print("--- End report ---")