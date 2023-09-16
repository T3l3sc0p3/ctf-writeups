# Bandit Level 0 → Level 1
## Level Goal

The password for the next level is stored in a file called readme located in the home directory. Use this password to log into bandit1 using SSH. Whenever you find a password for a level, use SSH (on port 2220) to log into that level and continue the game.

## Solution

```ssh bandit0@bandit.labs.overthewire.org -p 2220```

After connecting to bandit0 with the `bandit0` password, use `cat readme` to get the password to level 1
