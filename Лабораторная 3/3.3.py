def count_letters(text):
    lower_text = text.lower()

    letter_count = {}
    for char in lower_text:
        if char.isalpha():
            if char in letter_count:
                letter_count[char] += 1
            else:
                letter_count[char] = 1
    return letter_count

def calculate_frequency(letter_count):
    total_letters = sum(letter_count.values())
