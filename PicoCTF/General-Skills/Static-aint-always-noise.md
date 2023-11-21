# [picoCTF 2021] [Static ain't always noise](https://play.picoctf.org/practice/challenge/163)

## Description

Can you look at the data in this binary: [static](https://mercury.picoctf.net/static/66932732825076cad4ba43e463dae82f/static)? This [BASH script](https://mercury.picoctf.net/static/66932732825076cad4ba43e463dae82f/ltdis.sh) might help!

## Solution

After downloading 2 above files, I make `ltdis.sh` file executable by using the command `chmod a+x ltdis.sh`

To use the bash script, I simply run `./ltdis.sh <program-file>`, where `<program-file>` refers to the `static` file in this case

And if you don't know how to run this script correctly, just type `./ltdis.sh`, you will see the usage of it

![Usage](https://i.imgur.com/y5EvsY7.png)

This script will try to disassemble the file, making it easier to read the flag as you can see in the image below

![flag](https://i.imgur.com/O4ArG2L.png)

But actually, I can find the flag more easily without running the bash script by using the command `strings static | grep picoCTF{` and still get the same result ;)
