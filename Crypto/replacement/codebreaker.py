import hashlib

def get_intified_hash(ascii_value):
  hash = hashlib.md5(str(ascii_value).encode()).hexdigest()
  return int(hash, 16)

def find_char_for_hash(intified_hash):
  for i in range(128):
    if intified_hash == get_intified_hash(i):
      return chr(i)
    
diary = ""
with open("input.txt", "r") as f:
  diary = f.readline()
intified_hashes = diary.split(", ")

flag = ""
for intified_hash in intified_hashes:
  flag += find_char_for_hash(int(intified_hash))
print(flag)
