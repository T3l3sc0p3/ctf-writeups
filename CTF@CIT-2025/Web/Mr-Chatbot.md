# Mr. Chatbot (973 pts)

![MrChatbot](img/mrchatbot.png)

Initially, when tested some stuffs of this challenge, I thought that it was a very strict **Prompt Injection** vulnerability. However, I realized it was much deeper than that

After enter **admin** or any strings as username, it will generate a JWT session in cookie, which decodes to `{"admin":"0","name":"admin"}`

First, I tried to crack it but no luck, so I add `admin=1` to POST request. However, this made JWT become weirded so I couldn't decode it using normal web tools

Here I used `flask-unsign` to decode it

![decode](img/mrchatbot-flask-unsign.png)

As you can see, there is another base64 inside this one and decode it returns the username that I entered

So I guess that the server probably use a template like `f"{username}"` for both **name** and **uid**

Noticed that the server are using Python, I tried **Server-Side Template Injection (SSTI)** payload on username combine with `admin=1`

This is the payload from [PayloadsAllTheThings](https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Server%20Side%20Template%20Injection/Python.md)

```python
{{namespace.__init__.__globals__.os.popen('id').read()}}
```

After that, I take JWT session, decode it and decode the inside base64. And it actually works

Now I just need to `cat secrets.txt` file

```python
{{namespace.__init__.__globals__.os.popen('cat secrets.txt').read()}}
```

![flag](img/mrchatbot-flag.png)

`Flag: CIT{18a7fbedb4f3548f}`
