import base64
import hashlib
import hmac
import struct
import time


secret = "DRSXI2L="

def generate_TOTP():

    key = base64.b32decode(secret)
    timestamp = int(time.time())//30

    timestamp_bytes = struct.pack(">Q", timestamp)
    hash = hmac.new(key, timestamp_bytes, hashlib.sha1).digest()

    offset = hash[-1] & 0x0F

    truncated_hash = hash[offset:offset+4]

    code = str(struct.unpack(">I", truncated_hash)[0] & 0x7FFFFFFF)
    totp = code[0:6]

    return totp

if __name__ == "__main__":
    while True:
        print(generate_TOTP())
        time.sleep(10)

    