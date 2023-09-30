# [Bandit Level 6 → Level 7](https://overthewire.org/wargames/bandit/bandit7.html)
## Level Goal

The password for the next level is stored somewhere on the server and has all of the following properties:

- owned by user bandit7
- owned by group bandit6
- 33 bytes in size

## Solution

Run `find / -user bandit7 -group bandit6 -size 33c 2>/dev/null` to find files that match the task

In the above command, the `2>/dev/null` part redirects any error messages to /dev/null, preventing them from being displayed.

After finding `/var/lib/dpkg/info/bandit7.password`, you can obtain the password for the level 7
