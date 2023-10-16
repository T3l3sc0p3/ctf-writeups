# [picoCTF 2021] [Python Wrangling](https://play.picoctf.org/practice/challenge/166)

## Description

Python scripts are invoked kind of like programs in the Terminal... Can you run [this Python script](https://mercury.picoctf.net/static/5c4c0cbfbc149f3b0fc55c26f36ee707/ende.py) using [this password](https://mercury.picoctf.net/static/5c4c0cbfbc149f3b0fc55c26f36ee707/pw.txt) to get [the flag](https://mercury.picoctf.net/static/5c4c0cbfbc149f3b0fc55c26f36ee707/flag.txt.en)?

### Hints

1. Get the Python script accessible in your shell by entering the following command in the Terminal prompt: `$ wget https://mercury.picoctf.net/static/5c4c0cbfbc149f3b0fc55c26f36ee707/ende.py`
2. `$ man python`

## Solution

When I ran `python ende.py`, it displayed a usage message

![Usage](https://i.imgur.com/49BEfrl.png)

Based on that, I ran `python ende.py -d flag.txt.en`, with the `-d` option likely meaning "decode". After entering the password, I got the flag

You can use the command `python ende.py -h` to see more detail about how it works or try encoding the flag again :)
