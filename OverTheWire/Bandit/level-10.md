# [Bandit Level 9 → Level 10](https://overthewire.org/wargames/bandit/bandit10.html)
## Level Goal

The password for the next level is stored in the file **data.txt** in one of the few human-readable strings, preceded by several `=` characters.

## Solution

First, I use the `strings` command to print the sequences of printable or human-readable characters in `data.txt`

```strings data.txt```

Then, I used the `grep` command to search for strings preceded by `=` characters

Finally, I combined 2 commands using a pipeline to obtain the password for level 10

```strings data.txt | grep ==```

### Note

`strings` is used to print the sequences of printable characters in files
