# nc

## Description

Pwn challenges often require connecting to the challenge server using the <code>nc</code> (netcat) command. It's important to learn how to use <code>nc</code>.

You can connect to the challenge server by executing the following command in your shell. Solve the problem at the connection point and obtain the flag.

<code>nc chal-lz56g6.wanictf.org 9003</code>

## Attachments

[pwn-nc.zip](https://github.com/rstacks/WaniCTF2024-writeup/blob/master/Pwnable/nc/attachments/pwn-nc.zip)

## Solution

- This was a very simple challenge, as it was clearly meant to be an introduction to using
the <code>nc</code> command. After running the provided <code>nc</code> command, we are given a simple problem to solve:
<code>15 + 1 = ?</code>. Providing the correct answer causes the flag to be printed.

## Flag

FLAG{th3_b3ginning_0f_th3_r0ad_to_th3_pwn_p1ay3r}
