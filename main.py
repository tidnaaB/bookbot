def main():
    path_to_file = "books/frankenstein.txt"

    with open(path_to_file, 'r') as f:
        file_contents = f.read()
    
    print(file_contents)

    word_count = number_of_words(file_contents)
    character_frequency = count_characters(file_contents)

    char_list = [{'char': char, 'num': frequency} for char, frequency in character_frequency.items()]

    char_list.sort(reverse=True, key=lambda x: x['num'])


    print(f"{word_count} words found in the document\n")
    
    for item in char_list:
        print(f"The '{item['char']}' character was found {item['num']} times")
    

def number_of_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    characters = {}
    for char in text:
        if char.isalpha():
            char = char.lower()
            if char in characters:
                characters[char] += 1
            else:
                characters[char] = 1
    return characters

if __name__ == "__main__":
    main()