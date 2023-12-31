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
    eng_output = ""

    for _ in range(digits):
        digit = random.choice(list(data.keys()))
        eng_output += digit
        morse_output.append(data[digit])

    print("   ".join(morse_output))
    eng_word = input()

    if eng_word == eng_output:
        print("""You are correct

If you want to try again just choose another command.
If you want to stop the program type "end"
 
Command here:""", end="")
    else:
        print("""You are incorrect

If you want to try again just choose another command.
If you want to stop the program type "end"
 
Command here:""", end="")


def eng_to_morse(data, list_of_words):
    morse_input = input().split("   ")
    word = ""
    for _ in morse_input:
        for k, v in data.items():
            if v == _:
                word += k

    print(word)
    print("""If you want to try again just choose another command.
If you want to stop the program type "end"
 
Command here:""", end="")


print("""Hello, this is a program made to help learn morse code.
If you know how to use this program type the command you want to use then press [Enter].
If you don`t know how to use this program type "Help" then press [Enter].

Command here:""", end="")

list_of_commands = ["morse to english", "morse to bulgarian", "translate to english", "translate to bulgarian"]

while True:

    command = input()

    if command.lower() == "end":
        break

    if command.lower() == "help":
        print("""This program provides four commands.
    
Command 1 - morse to english. To get this command type "morse to english".
If you chose morse to english the console will give you a randomly generated
sequence of letters in morse code. You need to translate it and type it in to
the console(in english) if if you are correct the console will print "You are correct"
else you will be given the option to try again.
     
Command 2 - morse to bulgarian. To get this command type "morse to bulgarian".
If you chose morse to bulgarian the console will give you a randomly generated
sequence of letters in morse code. You need to translate it and type it in to
the console(in bulgarian) if if you are correct the console will print "You are correct"
else you will be given the option to try again.
    
Command 3 - translate to english. To get this command type "translate to english".
If you chose translate to english the console will ask you for a sequence of morse letters.
Then it will translate it to english.
    
Command 4 - translate to bulgarian. To get this command type "translate to bulgarian".
If you chose translate to bulgarian the console will ask you for a sequence of morse letters.
Then it will translate it to bulgarian.
    
Command here:""", end="")

        continue

    if command.lower() not in list_of_commands:
        print("""You have picked an invalid command try again.
    
Command here:""", end="")

    if command.lower() == list_of_commands[0]:
        morse_to_eng(data_eng)

    elif command.lower() == list_of_commands[1]:
        morse_to_eng(data_bg)

    elif command.lower() == list_of_commands[2]:
        eng_to_morse(data_eng, list_of_eng_words)

    elif command.lower() == list_of_commands[3]:
        eng_to_morse(data_bg, list_of_bg_words)
