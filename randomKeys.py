from crypto import crypto
import time

LenthOfkeys = 10
keyFilename = None

while True:
    print(crypto.keygen(0, LenthOfkeys, ))
    time.sleep(1)
