# [Bandit Level 22 → Level 23](https://overthewire.org/wargames/bandit/bandit23.html)
## Level Goal

A program is running automatically at regular intervals from **cron**, the time-based job scheduler. Look in **/etc/cron.d/** for the configuration and see what command is being executed.

**NOTE:** Looking at shell scripts written by other people is a very useful skill. The script for this level is intentionally made easy to read. If you are having problems understanding what it does, try executing it to see the debug information it prints.

## Solution

Just like [level 22](https://github.com/T3l3sc0p3/ctf-writeups/blob/master/OverTheWire/Bandit/level-22.md), we `cd` to `/etc/cron.d` and read file by using `cat cronjob_bandit23`

```sh
@reboot bandit23 /usr/bin/cronjob_bandit23.sh  &> /dev/null
* * * * * bandit23 /usr/bin/cronjob_bandit23.sh  &> /dev/null
```

After that, we run `cat /usr/bin/cronjob_bandit23.sh` and we get another bash script:

```sh
#!/bin/bash

myname=$(whoami)
mytarget=$(echo I am user $myname | md5sum | cut -d ' ' -f 1)

echo "Copying passwordfile /etc/bandit_pass/$myname to /tmp/$mytarget"

cat /etc/bandit_pass/$myname > /tmp/$mytarget
```

As you can see, it fetches the current username (in this case it is **bandit23**), creates an MD5 hash from a string, and then copies a password file to the /tmp directory with the hashed filename

Therefore, all we need to do is perform the same steps to get the password!

```sh
cat /tmp/$(echo "I am user bandit23" | md5sum | cut -d ' ' -f 1)
```
