import string

letters = string.ascii_lowercase


def dec(cipher):
    decrypt = ""
    for c in cipher:
        if c in letters:
            decrypt += chr((ord(c) - ord("a") + 2) % 26 + 97)
        else:
            decrypt += c
    return decrypt


ciphertext = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj"
print(dec(ciphertext))

# print(dec("map")) 