# beginners_rsa

## Description

Do you know RSA?

## Attachments

[cry-beginners-rsa.zip](https://github.com/rstacks/WaniCTF2024-writeup/blob/master/Crypto/beginners_rsa/attachments/cry-beginners-rsa.zip)

## Solution

- We are provided with the values of <code>n</code>, <code>e</code>, and the encrypted flag. From the code provided in
<code>chall.py</code> (which is provided in the zip file above), we can see that <code>n</code> is comprised of 5 prime factors. I used 
https://www.dcode.fr/prime-factors-decomposition to find each of these prime factors, as they will be needed for the decryption process.
- I wrote a [Python script](https://github.com/rstacks/WaniCTF2024-writeup/blob/master/Crypto/beginners_rsa/decrypt.py) to decrypt the ciphertext. The only additional information needed is <code>d</code>,
the private key. Knowing the prime factors of <code>n</code>, we can apply [Euler's totient function](https://en.wikipedia.org/wiki/Euler's_totient_function) and
the modular inverse function from [sympy](https://www.sympy.org/en/index.html) to calculate <code>d</code>. See my script for how I went about this
process.
- All that's left to do is to decrypt the ciphertext. I used Python's built-in <code>pow()</code> function,
then used <code>long_to_bytes()</code> to undo the provided script's usage of <code>bytes_to_long()</code> to get the flag
in plaintext.

## Flag

FLAG{S0_3a5y_1254!!}
