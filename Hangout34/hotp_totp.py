import base64
import hashlib
import hmac
import struct
import time

secret = 'DRSXI2LO'
counter = 0
digits = 6

def generate_HOTP(counter):
    key = base64.b32decode(secret)

    # pack counter into 8-byte big-endian
    counter_bytes = struct.pack('>Q', counter)

    # calculate HMAC digest
    hash = hmac.new(key, counter_bytes, hashlib.sha1).digest()

    # dynamic truncation to get a 4-byte string
    offset = hash[-1] & 0x0F

    # convert bytes into bits and make it a positive number
    code = struct.unpack('>I', hash[offset:offset+4])[0] & 0x7FFFFFFF

    #generate otp with 6 characters
    otp = code % (10 ** digits)
    return str(otp).zfill(digits)

def generate_TOTP():
    # get timestamp from current time
    timestamp = int(time.time()) // 30

    #passing "timestamp" as an argument to generate_HOTP
    return generate_HOTP(timestamp)


if __name__ == '__main__':
    
    while True:
        print(f"HOTP at counter {counter}:", generate_HOTP(counter))
        print("TOTP now:", generate_TOTP())
        print()
        counter += 1
        time.sleep(5)
