# [Bandit Level 12 → Level 13](https://overthewire.org/wargames/bandit/bandit13.html)
## Level Goal

The password for the next level is stored in the file **data.txt**, which is a hexdump of a file that has been repeatedly compressed. For this level it may be useful to create a directory under `/tmp` in which you can work using `mkdir`. For example: `mkdir /tmp/myname123`. Then copy the datafile using cp, and rename it using mv (read the manpages!)

## Solution

First, you'll need to create a directory under `/tmp` with a name of your choice (for instance, `t3l3sc0p3`). Once you have done that, use the `cp` command to copy the file called **data.txt** to the newly created directory

While reading **data.txt**, I noticed that its content is in hexdump format, so I'm running `xxd -r data.txt > data` to decompress it and print the output to file

Next, use the `file` command to know the file type of data. Here I saw this is a `gzip` file

![gzip](https://i.imgur.com/0JUSxT5.png)

Run the `man gzip` command to learn how to use it, and then run `mv data data.gz` to add the `.gz` extension to the file. Finally, run `gzip -d data.gz` to decompress the file

After a few more decompressing, I realize this is a loop of these actions: Decompress -> Detect the type of the file -> Learn how to use tools -> Add extension to the file -> Repeat

So to make it shorter, I will post this image here, this is an image about these commands I use to find the password. Sorry for this lazy~

![I'm too lazy for this](https://i.imgur.com/QJo1HoG.png)
