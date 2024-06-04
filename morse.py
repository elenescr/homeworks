morse = [".-", "-...", "-.-.", "-..",
         ".", "..-.", "--.", "....",
         "..", ".---", "-.-", ".-..",
         "--", "-.", "---", ".--.",
         "--.-", ".-.", "...", "-",
         "..-", "...-", ".--", "-..-",
         "-.--", "--.."]
alphabet = ["A", "B", "C", "D",
            "E", "F", "G", "H",
            "I", "J", "K", "L",
            "M", "N", "O", "P",
            "Q", "R", "S", "T",
            "U", "V", "W", "X",
            "Y", "Z"]

def encryption (t) :
    encrypted = ""
    for i in t:
        i = i.upper()
        if i in alphabet:

            n = alphabet.index(i)
            encrypted += morse[n]
        elif i == " ":
            encrypted += " "
    return encrypted

text = input("Enter the text: ")
print(encryption(text))
