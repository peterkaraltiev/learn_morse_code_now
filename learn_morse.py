import random


data_eng = {
    "a": ". _",
    "b": "_ . . .",
    "c": "_ . _ .",
    "d": "_ . .",
    "e": ".",
    "f": ". . _ .",
    "g": "_ _ .",
    "h": ". . . .",
    "i": ". .",
    "j": ". _ _ _",
    "k": "_ . _",
    "l": ". _ . .",
    "m": "_ _",
    "n": "_ .",
    "o": "_ _ _",
    "p": ". _ _ .",
    "q": "_ _ . _",
    "r": ". _ .",
    "s": ". . .",
    "t": "_",
    "u": ". . _",
    "v": ". . . _",
    "w": ". _ _",
    "x": "_ . . _",
    "y": "_ . _ _",
    "z": "_ _ . .",
    "1": ". _ _ _ _",
    "2": ". . _ _ _",
    "3": ". . . _ _",
    "4": ". . . . _",
    "5": ". . . . .",
    "6": "_ _ _ _ .",
    "7": "_ _ _ . .",
    "8": "_ _ . . .",
    "9": "_ . . . .",
    "0": "_ _ _ _ _",
}

data_bg = {
    "а": ". _",
    "б": "_ . . .",
    "в": ". _ _",
    "г": "_ _ .",
    "д": "_ . .",
    "е": ".",
    "ж": ". . . _",
    "з": "_ _ . .",
    "и": ". .",
    "й": ". _ _ _",
    "к": "_ . _",
    "л": ". _ . .",
    "м": "_ _",
    "н": "_ .",
    "о": "_ _ _",
    "п": ". _ _ .",
    "р": ". _ .",
    "с": ". . .",
    "т": "_",
    "у": ". . _",
    "ф": ". . _ .",
    "х": ". . . .",
    "ц": "_ . _ .",
    "ч": "_ _ _ .",
    "ш": "_ _ _ _",
    "щ": "_ _ . _",
    "ъ": "_ . . _",
    "ь": "_ . _ _",
    "ю": ". . _ _",
    "я": ". _ . _",
    "1": ". _ _ _ _",
    "2": ". . _ _ _",
    "3": ". . . _ _",
    "4": ". . . . _",
    "5": ". . . . .",
    "6": "_ _ _ _ .",
    "7": "_ _ _ . .",
    "8": "_ _ . . .",
    "9": "_ . . . .",
    "0": "_ _ _ _ _",
}

list_of_eng_words = ["list", "car", "sidewalk", "Niger", "Peter"]

list_of_bg_words = ["е", "т"]


def morse_to_eng(data):

    digits = random.randint(1, 10)
    morse_output = []
    eng_output = []

    for _ in range(digits):
        digit = random.choice(list(data.keys()))
        eng_output.append(digit)
        morse_output.append(data[digit])

    print("   ".join(morse_output))
    eng_word = input()

    if eng_word == eng_output:
        return True
    else:
        return False


def eng_to_morse(data, list_of_words):

    eng_word_output = random.choice(list_of_words)
    print(eng_word_output)

    eng_word_output = eng_word_output.lower()

    morse_eng_word = []
    for t in eng_word_output:

        morse_eng_word.append(data[t])

    morse_input = input().split("   ")

    if morse_input == morse_eng_word:
        return True


print(eng_to_morse(data_bg, list_of_bg_words))
