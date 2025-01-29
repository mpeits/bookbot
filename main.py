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

print(word_count)
print(characters)