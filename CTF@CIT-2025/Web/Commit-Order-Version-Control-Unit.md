# Commit & Order: Version Control Unit (782 pts)

![CommitOrderVersionControlUnit](img/commitorderversioncontrolunit.png)

As you see in the title and description, this is probably a vulnerability or a problem that related to [git](https://git-scm.com/)

Some devs may forget to exclude `.git` directory when deploying, which can lead to the exposure of the entire source code, creds, authen keys, and more if someone discovers it

First, I tried `http://23.179.17.40:58002/.git/` and I got 403 response. However, this means that the `.git` directory is existed and not properly excluded so I could exploit it :))

Here I used `git-dumper` to clone that repo

```sh
git-dumper http://23.179.17.40:58002/.git/ test
```

Then I checked the changes in the commit using `git diff master <commit-id>` until I reached the commit `68f8fcd`

In this commit, I found this line:

![flag](img/commitorderversioncontrolunit-flag.png)

This is a base64, so I decode it and get the flag

`Flag: CIT{5d81f7743f4bc2ab}`
