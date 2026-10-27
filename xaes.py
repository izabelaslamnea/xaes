#!/usr/bin/env python3

import sys
import argparse
import os

from Crypto.Protocol.KDF import PBKDF2
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Hash import SHA256

SALT_SIZE = 8
ITERATIONS = 10000

def derive_key_iv(password, salt):
    key_iv = PBKDF2(
        password,
        salt,
        dkLen=32,  # 16 bytes key + 16 bytes IV
        count=ITERATIONS,
        hmac_hash_module=SHA256
    )
    return key_iv[:16], key_iv[16:]

def encrypt(data, password):
    salt = os.urandom(SALT_SIZE)

    key, iv = derive_key_iv(password, salt)

    cipher = AES.new(key, AES.MODE_CBC, iv=iv)
    ciphertext = cipher.encrypt(pad(data, AES.block_size))

    return b"Salted__" + salt + ciphertext

def decrypt(data, password):
    if data[:8] != b"Salted__":
        raise ValueError("Formato no válido (falta cabecera Salted__)")

    salt = data[8:16]
    ciphertext = data[16:]

    key, iv = derive_key_iv(password, salt)

    cipher = AES.new(key, AES.MODE_CBC, iv=iv)

    try:
        return unpad(cipher.decrypt(ciphertext), AES.block_size)
    except ValueError:
        raise ValueError("Contraseña incorrecta o datos corruptos")

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("-e", action="store_true", help="encrypt")
    parser.add_argument("-d", action="store_true", help="decrypt")
    parser.add_argument("password")

    args = parser.parse_args()

    data = sys.stdin.buffer.read()

    if args.e:
        result = encrypt(data, args.password)
        sys.stdout.buffer.write(result)

    elif args.d:
        try:
            result = decrypt(data, args.password)
            sys.stdout.buffer.write(result)
        except Exception as e:
            print(f"Error: {e}", file=sys.stderr)
            sys.exit(1)

    else:
        print("Usa -e o -d", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
