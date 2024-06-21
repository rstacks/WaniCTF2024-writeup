nc

Pwn challenges often require connecting to the challenge server using the nc (netcat) command. It's important to learn how to use nc.

You can connect to the challenge server by executing the following command in your shell. Solve the problem at the connection point and obtain the flag.

nc chal-lz56g6.wanictf.org 9003


This was a very simple challenge, as it was clearly meant to be an introduction to using
the nc command. After running the provided nc command, we are given a simple problem to solve:
15 + 1 = ?. Providing the correct answer causes the flag to be printed.

flag: FLAG{th3_b3ginning_0f_th3_r0ad_to_th3_pwn_p1ay3r}
