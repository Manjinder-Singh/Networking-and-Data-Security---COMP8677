#!/usr/bin/python3

from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA

message=b'Manjinder Singh\n Student ID: 110097177\n'

#Importing Public Key
key=RSA.import_key(open('public.pem').read())

cipher=PKCS1_OAEP.new(key)
ciphertext=cipher.encrypt(message)

f=open('ciphertext.bin', 'wb')

f.write(ciphertext)
f.close()



