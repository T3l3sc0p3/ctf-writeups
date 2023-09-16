# Bandit Level 5 → Level 6
## Level Goal

The password for the next level is stored in a file somewhere under the `inhere` directory and has all of the following properties:

    human-readable
    1033 bytes in size
    not executable

## Solution

Run `find inhere/ -type f -size 1033c` to find files that match the task

You will see that `inhere/maybehere07/.file2` matchs the task
