# [Bandit Level 3 → Level 4](https://overthewire.org/wargames/bandit/bandit4.html)
## Level Goal

The password for the next level is stored in a hidden file in the `inhere` directory.

## Solution

First, use `ls -al inhere/` to list all file (even the file starting with .) and you will get `.hidden` file

`-a` mean do not ignore entries starting with . (dot)

`-l` mean use a long listing format

After that, use `cat inhere/.hidden` to get the password to the next level
