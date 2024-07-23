def main():
    print ("Enter book name (must be in /books directory):")
    book = input()
    with open("books/" + book) as f:
        file_contents = f.read()
        words = len(file_contents.split())
        print("--Begin report for " + book + "--")
        print(str(words) + " words found in the book")
        letter_counts = char_count(file_contents)
        for letter in letter_counts:
            print("The letter '" + letter + "' was found " + str(letter_counts[letter]) + " times" )
        print("--Finish report--")    

def char_count(text):
    char_dict = {}
    text_lower = text.lower()
    for letter in text_lower:
        if letter.isalpha():
            if letter in char_dict:
                char_dict[letter] += 1
            else:
                char_dict[letter] = 1
    return dict(sorted(char_dict.items(), key = lambda x:x[1], reverse=True))

main()
