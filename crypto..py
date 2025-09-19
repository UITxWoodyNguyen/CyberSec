def encode(enc: str, offset: int) -> str:
    offset = offset % 26 + 26
    encoded = []
    for i in enc:
        if i.isalpha():
            if i.isupper():
                encoded.append(chr(ord('A') + (ord(i) - ord('A') + offset) % 26))
            else:
                encoded.append(chr(ord('a') + (ord(i) - ord('a') + offset) % 26))
        else:
            encoded.append(i)
    return ''.join(encoded)

def decode(enc: str, offset: int) -> str:
    return encode(enc, 26 - offset)

for k in range(26):
    message = ""
    res = decode(message,k)
    print(res)
