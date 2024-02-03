# [Bandit Level 18 → Level 19](https://overthewire.org/wargames/bandit/bandit19.html)
## Level Goal

The password for the next level is stored in a file **readme** in the homedirectory. Unfortunately, someone has modified **.bashrc** to log you out when you log in with SSH.

## Solution

In this level, there is an automatic logout after accessing the server and say "Byebye!"

However, with a few searches, I found out that we can execute commands through SSH. Just need to add the command we want to execute in the quote like this:

```sh
ssh bandit18@bandit.labs.overthewire.org -p 2220 "ls"
```

It still logout, but now it also run `ls` command as you can see here

![](assets/level-19/img/readme.png)

Finally, you just need to read the file **readme** and you will get the password

```sh
ssh bandit18@bandit.labs.overthewire.org -p 2220 "cat readme"
```
