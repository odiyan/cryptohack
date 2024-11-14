enc = bytes.fromhex("0e0b213f26041e04")

dec = b"crypto{}"

key_ = ""

for l in range(len(enc)):
    for x in range(256):
        xord = bytes([enc[l] ^ x])
        if xord[0] == dec[l]:
            # print(f"xord: {xord}, x: {chr(x)}")
            key_ += chr(x)

print(key_) # myXORkey

enc_flag = bytes.fromhex("0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104")

dec_flag = b""

for x in range(len(enc_flag)):
    dec_flag += bytes([enc_flag[x] ^ ord(key_[x % len(key_)])])

print(dec_flag)
