word = "Donkey"

with open("file.txt", "r") as f:
    content = f.read()

contentNew = content.replace(word, "######")   #replace donky with ###### in file.txt

with open("file.txt", "w") as f:
    f.write(contentNew)