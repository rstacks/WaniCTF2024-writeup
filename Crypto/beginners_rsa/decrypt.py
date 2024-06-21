from sympy import mod_inverse
from Crypto.Util.number import *

# Given information
n = 317903423385943473062528814030345176720578295695512495346444822768171649361480819163749494400347
e = 65537
enc = 127075137729897107295787718796341877071536678034322988535029776806418266591167534816788125330265

# Prime factors of n
p1 = 9953162929836910171
p2 = 11771834931016130837
p3 = 12109985960354612149
p4 = 13079524394617385153
p5 = 17129880600534041513

# Apply Euler's totient function to calculate d, the private key
phi = (p1 - 1) * (p2 - 1) * (p3 - 1) * (p4 - 1) * (p5 - 1)
d = mod_inverse(e, phi)

# Decrypt the ciphertext
decrypted_text = pow(enc, d, n)

# Display flag
flag = long_to_bytes(decrypted_text).decode()
print(flag)
