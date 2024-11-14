enc = bytes.fromhex("73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d")

for x in range(256):
    dec = b""
    for l in range(len(enc)):
        dec += bytes([enc[l] ^ x])

    print(dec)
