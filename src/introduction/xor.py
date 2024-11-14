string = "label"

new_string = ""

for x in string:
    new_string += chr(ord(x) ^ 13)

print(new_string)
