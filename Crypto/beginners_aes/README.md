beginners_aes

AES is one of the most important encryption methods in our daily lives.


We are provided with the encrypted flag and the SHA256 hash of the flag's plaintext. Within
the provided chall.py file, we are also provided with most of the key and most of the IV used
in this particular AES encryption. Since only the last byte is unknown in both the key and the IV,
we can feasibly crack the encryption through brute force. I wrote a Python script to do just that.

Since the missing data in both the key and the IV is 1 byte, there are 256 (2^8) candidates each for the
final part of these values. I used two nested for loops to reach every possible combination. On each
iteration, I first completed the partial flag and partial IV from chall.py with the values from 
that iteration's combination. I then attempted to decrypt the provided ciphertext for the flag using
this information. I then compared the SHA256 hash of whatever was decrypted to the provided flag hash.
If they matched, then that means we have found the correct key and IV.

The key and IV were found to be "the_enc_key_is_$" and "my_great_iv_is_O" respectively. This
enabled me to find the flag.

flag: FLAG{7h3_f1r57_5t3p_t0_Crypt0!!}
