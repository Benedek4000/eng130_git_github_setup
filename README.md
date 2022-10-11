### Github setup

Make sure to replace arguments where needed:

- the main library
- the email address
- the public key name

#### Generate SSH key

-enter [main library/.ssh] and generate SSH key (private and public)
```commandline
cd /c/Users/bened
cd .ssh
ssh-keygen -t rsa -b 4096 -C "kovacsbenedek4000@gmail.com"
```

#### Connect local folder to Github repository

- add SSH public key to Github account. read SSH key by copying the public key:  
```commandline
cat id_rsa.pub
```
- create repository on Github
- create README.md file in local folder
- prepare local folder to connect to repository and connect it to repository:
```commandline
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin "git@github.com:[username]/[repository].git"
```
- push local folder to repository:  
```commandline
git push -u origin main
```
