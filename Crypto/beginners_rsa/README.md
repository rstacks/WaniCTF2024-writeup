beginners_rsa

Do you know RSA?

We are provided with the values of n, e, and the encrypted flag. From the code provided in
chall.py, we can see that n is comprised of 5 prime factors. I used 
https://www.dcode.fr/prime-factors-decomposition to find each of these prime factors. This is enough
information to crack this RSA encryption.

I wrote a Python script to decrypt the ciphertext. The only additional information needed is d,
the private key. Knowing the prime factors of n, we can apply Euler's totient function and
the modular inverse function from sympy to calculate d. See my script for how I went about this
process.

All that's left to do is to decrypt the ciphertext. I used Python's built-in pow() function,
then used long_to_bytes() to undo the provided script's usage of bytes_to_long() to get the flag
in plaintext.

flag: FLAG{S0_3a5y_1254!!}
