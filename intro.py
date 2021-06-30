def wordCount():
    fileName = input("enter file name: ")
    f = open(fileName, "r")
    words = 0
    for line in f:
        word = line.split()
        words = words + len(word)
    print("number of words: ")
    print(words)
wordCount()

