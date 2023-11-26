# [Bandit Level 13 → Level 14](https://overthewire.org/wargames/bandit/bandit14.html)
## Level Goal

The password for the next level is stored in **/etc/bandit_pass/bandit14 and can only be read by user bandit14**. For this level, you don’t get the next password, but you get a private SSH key that can be used to log into the next level. **Note: localhost** is a hostname that refers to the machine you are working on

## Solution

To solve this level, first, you need to run `ssh bandit13@bandit.labs.overthewire.org -p 2220` to connect to the server

Next, run `ls` and you will see a private SSH key, and you may already know what to do next~

![Private SSH Key](https://i.imgur.com/J0X1StQ.png)

To connect to the localhost (which is bandit.labs.overthewire.org) using port 2220, use the command `ssh -i sshkey.private bandit14@localhost -p 2220`. The flag `-i` is used to identity file

Finally, retrieve the password for bandit14 by using `cat /etc/bandit_pass/bandit14`
