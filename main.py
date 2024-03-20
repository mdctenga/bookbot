def main():
    with open("./books/frankenstein.txt") as f:
        file_contents = f.read()
        print(file_contents)
def count_words():
    with open("./books/frankenstein.txt") as f:
        file_contents = f.read()
        wordList = file_contents.split()
        wordCount = 0
        for word in wordList:
            wordCount+= 1   
        print(wordCount)

# main()
count_words()