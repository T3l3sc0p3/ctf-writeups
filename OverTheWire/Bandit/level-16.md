# [Bandit Level 15 → Level 16](https://overthewire.org/wargames/bandit/bandit16.html)
## Level Goal

The password for the next level can be retrieved by submitting the password of the current level to **port 30001 on localhost** using SSL encryption.

**Helpful note: Getting "HEARTBEATING" and "Read R BLOCK"? Use -ign_eof and read the "CONNECTED COMMANDS" section in the manpage. Next to 'R' and 'Q', the 'B' command also works in this version of that command...**

## Solution

Connect to the server and run the command `openssl s_client -connect localhost:30001`, then enter the password level 15 password to get password of level 16
