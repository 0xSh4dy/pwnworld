from Crypto.Cipher import AES
from base64 import b64encode,b64decode
import json
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
data = b'naruto'
key = get_random_bytes(16)
# cipher = AES.new(key,AES.MODE_CBC)
# ct_bytes = cipher.encrypt(pad(data,AES.block_size))
# print(ct_bytes)
cipher = AES.new(key,AES.MODE_CBC)
ct_bytes = b'Ml\xcd#\xa9\x87>\x12\x83)\x19\xbfe\x08\xb3\x8f'
pt = unpad(cipher.decrypt(ct_bytes),AES.block_size)
print(pt)