# [Bandit Level 10 → Level 11](https://overthewire.org/wargames/bandit/bandit11.html)
## Level Goal

The password for the next level is stored in the file **data.txt**, which contains base64 encoded data

## Solution

Before solving this level, you may want to check out `base64` [here](https://en.wikipedia.org/wiki/Base64)

When I check the data.txt file, I discovered that the data was encoded in base64. It could be identified by the presence of either `=` or `==` at the end

After that, I ran `base64 -d data.txt` command to decode the data and obtain the password for level 11. Not too hard, right?

### Note

`-d` or `--decode` flag is used to decode data. You can run `man base64` in your terminal to discover about other flag
