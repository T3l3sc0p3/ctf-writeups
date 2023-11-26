# [Bandit Level 7 → Level 8](https://overthewire.org/wargames/bandit/bandit8.html)
## Level Goal

The password for the next level is stored in the file **data.txt** next to the word **millionth**

## Solution

First, you need to know about `grep`. This is a useful command to search for matching patterns in files

Then, you can use `cat data.txt | grep millionth` or `grep -R millionth` to find the password to level 8

### Note

`|` is called pipeline. A pipeline takes the output of one command as the input of next command

`-R`, `-r` or `--recursive` will read all files under each directory, recursively (from [Explainshell.com](https://explainshell.com/explain?cmd=grep+-R+millionth))
