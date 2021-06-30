intro = input("please enter introduction: ")
print(intro)

wordCount = 1

characterCount = 0
for character in intro:
    characterCount = characterCount + 1

    if (character == " "): 
        wordCount = wordCount + 1
print("number of characters: ")
print(characterCount)
print("number of words: ")
print(wordCount)