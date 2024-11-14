key1 = bytes.fromhex("a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313")

key2_xor_key3 = bytes.fromhex("c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1")

key1_xor_key_xor_key3 = bytes(a ^ b for a,b in zip(key1, key2_xor_key3))

flag_xor_key1_xor_key2_xor_key3 = bytes.fromhex("04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf")

flag = bytes(a ^ b for a,b in zip(flag_xor_key1_xor_key2_xor_key3, key1_xor_key_xor_key3))
print(flag)
