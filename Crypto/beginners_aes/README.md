# beginners_aes

## Description

AES is one of the most important encryption methods in our daily lives.

## Attachments

[cry-beginners-aes.zip](https://github.com/rstacks/WaniCTF2024-writeup/blob/master/Crypto/beginners_aes/attachments/cry-beginners-aes.zip)

## Solution

- We are provided with the encrypted flag and the SHA256 hash of the flag's plaintext. Within
the provided <code>chall.py</code> file, we are also provided with most of the key and most of the IV used
in this particular AES encryption. Since only the last byte is unknown in both the key and the IV,
we can feasibly crack the encryption through **brute force**. I wrote a [Python script](https://github.com/rstacks/WaniCTF2024-writeup/blob/master/Crypto/beginners_aes/brute_forcer.py) to do just that.
- Since the missing data in both the key and the IV is 1 byte, there are 256 (there are 8 bits per byte, and 2<sup>8</sup> = 256) candidates each for the
final part of these values. I used two nested for loops to reach every possible combination.
- On each
iteration, I first completed the partial key and partial IV from <code>chall.py</code> with the values from 
that iteration's combination. Next, I attempted to decrypt the provided ciphertext for the flag using the key and IV I just created. I then compared the SHA256 hash of my decryption to the provided flag hash. If the hashes matched, then that means I found the correct key and IV.
- The key and IV were found to be "the_enc_key_is_$" and "my_great_iv_is_O" respectively. This
enabled me to find the flag.

## Flag

FLAG{7h3_f1r57_5t3p_t0_Crypt0!!}
