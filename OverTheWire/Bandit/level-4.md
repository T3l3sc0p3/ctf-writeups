# [Bandit Level 4 → Level 5](https://overthewire.org/wargames/bandit/bandit5.html)
## Level Goal

The password for the next level is stored in the only human-readable file in the inhere directory. Tip: if your terminal is messed up, try the “reset” command.

## Solution

First, run `file inhere/./-*` to find which ones is human-readable file and you will see that `-file07` is human-readable file because it is ASCII text

After that, run `cat inhere/./-file07` to get the password to the next level
