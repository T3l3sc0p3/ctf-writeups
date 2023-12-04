# [Bandit Level 17 → Level 18](https://overthewire.org/wargames/bandit/bandit18.html)
## Level Goal

There are 2 files in the homedirectory: **passwords.old and passwords.new**. The password for the next level is in **passwords.new** and is the only line that has been changed between **passwords.old and passwords.new**

**NOTE: if you have solved this level and see 'Byebye!' when trying to log into bandit18, this is related to the next level, bandit19**

## Solution

Run `diff passwords.old passwords.new` and take the second password, that's it!

![diff](assets/level-18/diff.png)
