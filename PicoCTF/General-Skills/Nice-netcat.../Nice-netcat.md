# [picoCTF 2021] [Nice netcat...](https://play.picoctf.org/practice/challenge/156)

## Description

There is a nice program that you can talk to by using this command in a shell: `$ nc mercury.picoctf.net 7449`, but it doesn't speak English...

### Hints

1. You can practice using netcat with this picoGym problem: [what's a netcat?](https://play.picoctf.org/practice/challenge/34)
2. You can practice reading and writing ASCII with this picoGym problem: [Let's Warm Up](https://play.picoctf.org/practice/challenge/22)

## Solution

After running the command `nc mercury.picoctf.net 7449`, I noticed that the output consisted of ASCII in decimal format separated by new lines

Therefore, I wrote a bash script to instantly convert these numbers into characters. But you can also do it manually if you want to~

```
#!/bin/bash
decimal=$(nc mercury.picoctf.net 7449)
flag=$(echo "$decimal" | awk '{printf "%c", $0}')
echo "Flag: $(echo $flag | tr -d $'\n')"
```

![flag](https://i.imgur.com/sQUxqPx.png)
