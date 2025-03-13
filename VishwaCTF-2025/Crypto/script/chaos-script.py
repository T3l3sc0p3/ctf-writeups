#!/usr/bin/python3
import base64

def xor_decrypt(encoded_msg):
    # Decode from Base85 and reverse the XOR (each byte XOR'ed with its index modulo 256)
    decoded = base64.b85decode(encoded_msg)
    transformed = bytearray(decoded)
    for i in range(len(transformed)):
        transformed[i] ^= (i % 256)
    return transformed.decode(errors='ignore')

# Read the encrypted messages from the file, separated by double newlines
with open('output.txt', 'r') as f:
    encrypted_messages = f.read().strip().split('\n\n')

# Decrypt each message and print them
for i, msg in enumerate(encrypted_messages, 1):
    print(f"Message {i}: {xor_decrypt(msg)}")
