

def count(text):
    word_num = len(text.split())

    letter_num = 0
    digit_num = 0

    for i in text:
        if i == " ":
            continue
        if i.isalpha():
            letter_num += 1
        if i.isnumeric():
            digit_num += 1
    
    text = text.replace(" ", "").lower()
    letters = {}

    for letter in text:
        if letter in letters:
            letters[letter] += 1
        else:
            letters[letter] = 1
    
    letters = {key: letters[key] for key in sorted(letters)}

    print(f"Words: {word_num}")
    print(f"Letters: {letter_num}")
    print(f"Digits: {digit_num}")
    print(letters)

count("Ala ma kota 123")