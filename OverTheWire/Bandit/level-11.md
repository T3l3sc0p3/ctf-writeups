# [Bandit Level 11 → Level 12](https://overthewire.org/wargames/bandit/bandit12.html)
## Level Goal

The password for the next level is stored in the file **data.txt**, where all lowercase (a-z) and uppercase (A-Z) letters have been rotated by 13 positions

## Solution

Just like [level 10](https://github.com/T3l3sc0p3/ctf-write-up/blob/master/OverTheWire/Bandit/level-10.md), this's also an encoded data. It called **Caesar Cipher**. You can check it out [here](https://www.geeksforgeeks.org/caesar-cipher-in-cryptography/)

The term **Rot13** that you see in the `Helpful Reading Material` section is actually a **Caesar Cipher** with a shift of 13

So you can use the online tool like [rot-13-cipher](https://www.dcode.fr/rot-13-cipher) or [caesar-cipher](https://www.dcode.fr/caesar-cipher)

Or this command to solve it if you want to: `cat data.txt | tr 'A-Za-z' 'N-ZA-Mn-za-m'`

### Note

`tr` is used to translate, squeeze, and/or delete characters. Use `man tr` for more informations
