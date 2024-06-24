# replacement

## Description

No one can read my diary!

## Attachments

[cry-replacement.zip](https://github.com/rstacks/WaniCTF2024-writeup/blob/master/Crypto/replacement/attachments/cry-replacement.zip)

## Solution

- From the provided script <code>chall.py</code> (which is within the zip file above), we can see that each character of the plaintext is ASCII encoded,
run through an MD5 hash, and then converted to a decimal value. The resulting value is appended to
the output file. We are given this output file in the zip file above. Logically, we should attempt to reverse the actions
of <code>chall.py</code> to get the plaintext, but it isn't possible to reverse the MD5 hashing process.
- Luckily, since each character of the plaintext is most likely one of the 128 ASCII characters, **brute
forcing** the solution is feasible. I wrote my own [Python script](https://github.com/rstacks/WaniCTF2024-writeup/blob/master/Crypto/replacement/codebreaker.py) to use this technique to recover
the plaintext.
- I started by reading the [provided output file](https://github.com/rstacks/WaniCTF2024-writeup/blob/master/Crypto/replacement/input.txt) (with the opening and closing brackets
removed) and getting all of the integer values into an array. For each element of this array, I
compared its value to every single ASCII character's MD5 hash. Once a match between the two hashes was found, I knew I had
found the correct character, and so I appended that character to a string.
- Once the entire array
had been read, I printed out the string, and the flag was revealed.

## Flag

FLAG{13epl4cem3nt}
