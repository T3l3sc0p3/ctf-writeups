# Epoch
Be honest, you have always wanted an online tool that could help you convert UNIX dates and timestamps! Wait... it doesn't need to be online, you say? Are you telling me there is a command-line Linux program that can already do the same thing? Well, of course, we already knew that! Our website actually just passes your input right along to that command-line program!
## Write-up
First, I started to put some numbers to convert. But when putting some commands like `ls` in there. It appears this error: `exit status 1`
So I started adding ';' after the numbers and execute `Command Injection`
```9;ls```
And after a while of searching, I found the flag with the command: `9;env` (`env` is used to print environment variables)

Flag: ```flag{7da6c7debd40bd611560c13d8149b647}```
