cipher = "OZGP LCXPO ULRFLC GTMCLYE"

# should vary between 65 and 90
# if > 90, start from 65

for shift in range(1,27):
    string = ""
    for letter in cipher:
        if letter == " ":
            string += " "
            continue

        shifted = (ord(letter) - 65 + shift) % 26
        string += chr(65 + shifted)
    print(string)
