def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    count_words = get_count_words(text)
    count_letters = get_count_letter(text)
    print(f"{count_words} words found in the document")
    for letter_dict in count_letters:
        char = letter_dict["char"]
        num = letter_dict["num"]
        print(f"The {char} character was found {num} times")
    
def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_count_words(text):
    words = text.split()
    wordCount = 0
    for word in words:
        wordCount+= 1
    return wordCount

def get_count_letter(text):
    # lowercase
    lowered_string = text.lower();
    # split letters
    letters = list(lowered_string)
    # count letters and add to dictionary
    lettersCount = {}
        
    for letter in letters:
        if letter.isalpha():
            if letter in lettersCount:
                lettersCount[letter] += 1
            else:
                lettersCount[letter] = 1

    letter_count_list = [{"char": letter, "num": lettersCount[letter]} for letter in lettersCount]
 

    letter_count_list.sort(key=sort_on, reverse=True)
    
    return letter_count_list

def sort_on(dict):
    return dict["num"]

main()