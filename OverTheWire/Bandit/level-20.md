# [Bandit Level 19 → Level 20](https://overthewire.org/wargames/bandit/bandit20.html)
## Level Goal

To gain access to the next level, you should use the setuid binary in the homedirectory. Execute it without arguments to find out how to use it. The password for this level can be found in the usual place (/etc/bandit_pass), after you have used the setuid binary.

## Solution

To execute the binary file, just add `./` before that file name

![](assets/level-20/img/execute.png)

You will see that this file will allow us to run the command as another user (bandit20)

And you also can get the password of level 20 through this file by using this command:

![](assets/level-20/img/password.png)
