# [Bandit Level 8 → Level 9](https://overthewire.org/wargames/bandit/bandit9.html)
## Level Goal

The password for the next level is stored in the file **data.txt** and is the only line of text that occurs only once

## Solution

First, I read the `data.txt` file and noticed that it contained many duplicate and mixed lines. Therefore, I need to sort it using the `sort` command

```sort data.txt```

After sorting the file, I use the command `uniq -u` to get only unique lines. Finally, I combined 2 commands using a pipeline

```sort data.txt | uniq -u```

### Note

`sort` is used to sort a file, arranging the records in a particular order (from [GeeksforGeeks](https://www.geeksforgeeks.org/sort-command-linuxunix-examples/))

`uniq` is used to report or omit repeated lines. The flag `-u` or `--unique` in the above command will make it only print unique lines
