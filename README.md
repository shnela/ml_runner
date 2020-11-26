# Send ALL code to github

[README_PREVIOUS.md](./README_PREVIOUS.md)

## [DuckDuckgo](https://duckduckgo.com/?q=git+push+all+branches&t=ffab&atb=v192-1&ia=web)
[first link](https://reactgo.com/git-push-remote-branches/)

```
git push --all <remote repo>
```

## Generate pair of ssh keys in cygwin

```bash
$ cd /cygdrive/c/Users/NobleProg/WorkingDir/
$ ssh-keygen.exe
Generating public/private rsa key pair.
Enter file in which to save the key (/home/NobleProg/.ssh/id_rsa):
/home/NobleProg/.ssh/id_rsa already exists.
Overwrite (y/n)? y
Enter passphrase (empty for no passphrase):
Enter same passphrase again:
...

NobleProg@jakub-rxvm /cygdrive/c/Users/NobleProg/WorkingDir
$ cat ~/.ssh/id_rsa.pub
ssh-rsa <some random characters> NobleProg@<nazwa maszyny>
```

## Create new repository in github

1. Settings -> Deploy keys -> Add deploy key
1. Add key
   1. Set some name
   1. paste **public key** from cygwin
   1. check **Allow write access**
1. Add key
1. Copy repository ssh path

In cygwin
```bash
$ pwd
/cygdrive/c/Users/NobleProg/WorkingDir
$ cd ./ml_runner/
$ git remote add personal git@github.com:shnela/test_upload_all.git
$ git push --all personal
```

**Rememeber about pushing changes at the end of the day**