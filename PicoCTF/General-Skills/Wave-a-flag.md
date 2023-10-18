# [picoCTF 2021] [Wave a flag](https://play.picoctf.org/practice/challenge/170)

## Description

Can you invoke help flags for a tool or binary? [This program](https://mercury.picoctf.net/static/beec4f433e5ee5bfcd71bba8d5863faf/warm) has extraordinarily helpful information...

### Hints

1. This program will only work in the webshell or another Linux computer.
2. To get the file accessible in your shell, enter the following in the Terminal prompt: `$ wget https://mercury.picoctf.net/static/beec4f433e5ee5bfcd71bba8d5863faf/warm`
3. Run this program by entering the following in the Terminal prompt: `$ ./warm`, but you'll first have to make it executable with `$ chmod +x warm`
4. -h and --help are the most common arguments to give to programs to get more information from them!
5. Not every program implements help features like -h and --help.


## Solution

To complete this task, you should first download the program. Once it's downloaded, make it executable by using the command `chmod +x warm`. If you're unsure what `+x` means, you can learn more about it by visiting [chmodcommand](https://chmodcommand.com/)

After you've made the program executable, run it using the command `./warm`. This will display a message, which you can see in the screenshot linked below

![-h](https://i.imgur.com/ldKcZlt.png)

Follow the message, add the `-h` option to the command, like this: `./warm -h` and you will get the flag ;)

![flag](https://i.imgur.com/iAiaDAC.png)
