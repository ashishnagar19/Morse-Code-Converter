morse_code = {
    "Q": "––•–",
    "W": "•––",
    "E": "•",
    "R": "•–•",
    "T": "–",
    "Y": "–•––",
    "U": "••–",
    "I": "••",
    "O": "–––",
    "P": "•––•",
    "A": "•–",
    "S": "•••",
    "D": "–••",
    "F": "••–•",
    "G": "––•",
    "H": "••••",
    "J": "•–––",
    "K": "–•–",
    "L": "•–••",
    "Z": "––••",
    "X": "–••–",
    "C": "–•–•",
    "V": "•••–",
    "B": "–•••",
    "N": "–•",
    "M": "––",
    "1": "•----",
    "2": "••---",
    "3": "•••--",
    "4": "••••-",
    "5": "•••••",
    "6": "-••••",
    "7": "--•••",
    "8": "---••",
    "9": "----•",
    "0": "-----",
    " ": "       "
}

def con(text):
    converted_list = []
    for letter in text:
        if letter in morse_code:
            letter = morse_code.get(letter)
            converted_list.append(letter+"   ")
    listToStr = ''.join([str(elem) for elem in converted_list])
    print(f"MORSE TEXT CORRESPONDING TO THE TEXT GIVEN\n{listToStr}\n")
on = True
while on:
    k=1
    text = input("ENTER TEXT TO CONVERT IT INTO MORSE CODE OR ENTER 0 TO EXIT: ").upper()
    for letter in text:
        if letter not in morse_code:
            k = 0
    if text == "0":
        on = False
        break
    elif text[0] == " ":
        print("ENTER VALID TEXT")
    elif k == 0:
        print("ENTER VALID TEXT")
    else:
        con(text)

