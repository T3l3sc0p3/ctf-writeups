# [Bandit Level 14 → Level 15](https://overthewire.org/wargames/bandit/bandit15.html)
## Level Goal

The password for the next level can be retrieved by submitting the password of the current level to **port 30000 on localhost.**

## Solution

After connecting to the server, simply run `nc localhost 30000`, enter the current password, and you will receive the next level password
