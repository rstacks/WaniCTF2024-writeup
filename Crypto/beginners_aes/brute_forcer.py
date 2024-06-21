from Crypto.Util.Padding import unpad
from Crypto.Cipher import AES
from os import urandom
import hashlib

# Given information
partial_key = b"the_enc_key_is_"
partial_iv = b"my_great_iv_is_"
flag_hash = "6a96111d69e015a07e96dcd141d31e7fc81c4420dbbef75aef5201809093210e"
encrypted_flag = b'\x16\x97,\xa7\xfb_\xf3\x15.\x87jKRaF&"\xb6\xc4x\xf4.K\xd77j\xe5MLI_y\xd96\xf1$\xc5\xa3\x03\x990Q^\xc0\x17M2\x18'

# This function checks a given key and IV to see if it's the correct pair
def is_correct_key_and_iv(key, iv):
  cipher_candidate = AES.new(key, AES.MODE_CBC, iv)
  padded_flag = cipher_candidate.decrypt(encrypted_flag)
  
  # Attempt to unpad the decrypted text
  flag_candidate = b""
  try: 
    flag_candidate = unpad(padded_flag, 16)
  except ValueError:
    return False
  
  # Compare hash of the flag candidate to the provided flag hash
  candidate_hash = hashlib.sha256(flag_candidate).hexdigest()
  if candidate_hash == flag_hash:
    return True
  return False

# Brute force the final byte of the key and IV
for i in range(256):
  key_byte = bytes([i])
  for j in range(256):
    iv_byte = bytes([j])

    # Create candidates for key and IV
    full_key = partial_key + key_byte
    full_iv = partial_iv + iv_byte

    # Decrypt if the combination was correct
    if is_correct_key_and_iv(full_key, full_iv):
      cipher = AES.new(full_key, AES.MODE_CBC, full_iv)
      padded_flag = cipher.decrypt(encrypted_flag)
      flag = unpad(padded_flag, 16)
      print(f"Key: {full_key}, IV: {full_iv}")
      print(f"Flag: {flag.decode()}")
