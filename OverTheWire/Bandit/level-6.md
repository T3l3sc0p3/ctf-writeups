# [Bandit Level 5 → Level 6](https://overthewire.org/wargames/bandit/bandit6.html)
## Level Goal

The password for the next level is stored in a file somewhere under the **inhere** directory and has all of the following properties:

- human-readable
- 1033 bytes in size
- not executable

## Solution

Run `find . -type f -size 1033c ! -executable -exec file {} +` to find files that match the task

You will see that `inhere/maybehere07/.file2` has all of the properties required by the task

Run `cat inhere/maybehere07/.file2` to get the password to the level 6
