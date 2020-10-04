<p align="center">
  <img src="https://github.com/Py-Project/FaceKit/blob/main/img/facebook-logo.png">
</p>
<p align="center"><img src="https://img.shields.io/badge/Version-1.0-brightgreen"></p>

</p> 
<p align="center"><img src="https://img.shields.io/badge/Author-Yezz123-green.svg"> 
</p>


<p align="center">
  <a href="https://github.com/yezz123">
    <img src="https://img.shields.io/github/followers/yezz123?label=Follow&style=social">
  </a>
  <a href="https://github.com/Py-Project/FaceKit/stargazers">
    <img src="https://img.shields.io/github/stars/Py-Project/FaceKit?style=social">
  </a>
</p>

# Facekit 🪐
A version of facebook using command line work on windows , macOS, linux created using python and flask with a lot of things.

including :
- uploaded photos
- tagged photos
- videos
- friends list and their profile photos (including Followers, Following, Work Friends, College Friends etc)
- and all public posts/statuses available on the user's timeline.
- check groupes and invitation.

## Usage 🔧

### Installation 💻 

You will need to:

- install [Flask](https://flask.palletsprojects.com/en/1.1.x/installation/)
- Install [Python 3](https://www.python.org/downloads/)
- install [bs4](https://pypi.org/project/beautifulsoup4/)
- Have a Facebook account without 2FA enabled

```bash
git clone https://github.com/Py-Project/FaceKit.git
cd FaceKit
```
### How to Run 🥶

After install all what u need write :
```bash
python run.py
```

and the code will run and u will find a menu like this :
- 1). Go To Menu
- 2). Start Web Version
- 3). Login
- 4). Logout
- 5). Update
- 0). Exit

First step :

loging using facebook cookies.
```bash
   [?] Your Facebook Cookies:
```
you can understand more check [Cookies](https://github.com/Py-Project/FaceKit/blob/main/FaceKit_web/README.md).

Then use it to start FaceKit_web or stay using command line by going to Menu 

### About Code 😃
For FaceKit_web u can see that i use [Flask framework](https://flask.palletsprojects.com/)
```python
from flask import Flask, render_template, request
```
Also i try to create all what i need in FaceKit folder
```python
from FaceKit import Account
from FaceKit import function
from FaceKit import sorting
from getpass import getpass
from FaceKit_web import start_web
import os, time, random, FaceKit, sys
```
You can also check the codes of Template they aren't mine cause i don't write `HTML` or `JS` or `CSS` a lot 🙅‍♂️ but i try to create magic using python.

 Also Don't be worry about updates i create a choice is number 5 for update:
 ```python
 elif choose == 5:
		os.system("git pull --verbose https://github.com/Py-Project/FaceKit.git ")
 ```
 Also i use bs4 for [output.py](https://github.com/Py-Project/FaceKit/blob/main/FaceKit/output.py)
 ```python
 from bs4 import BeautifulSoup as bs
 ```
 ---

## Important Message ⚠️

This tool is for research purposes only. Hence, the developers of this tool won't be responsible for any misuse of data collected using this tool. Used by many researchers and open source intelligence (OSINT) analysts.

This tool will not works if your account was set up with 2FA. You must disable it before using.

### Warning
- 1. Your account can be banned if you use this
- 2. After successfully logging in your account will
automatically comment on the author
profile photo and react
- 3. Don't use this for crime
- 4. Everything the user does is not the responsibility
of the author
- 5. By using this the user is considered to
understand and comply with the above provisions

---
## Issues 🔨

[![GitHub Issues](https://img.shields.io/github/issues/harismuneer/Ultimate-Facebook-Scraper.svg?style=flat&label=Issues&maxAge=2592000)](https://www.github.com/Py-Project/FaceKit/issues)

If you face any issue, you can create a new issue in the Issues Tab and I will be glad to help you out.
## Author 👼
<p align="center">
	<a href="https://www.instagram.com/froggy__19/">
  <code><img src="https://img.shields.io/badge/Froggy__19%20-%23E4405F.svg?&style=for-the-badge&logo=Instagram&logoColor=white"/></code>
		</a>
	<a href="https://www.twitch.tv/yassertahiri">
  <code><img src="https://img.shields.io/badge/yassertahiri%20-%239146FF.svg?&style=for-the-badge&logo=Twitch&logoColor=white"/></code>
	</a>
	<a href="https://twitter.com/THyasser1">
  <code><img src="https://img.shields.io/badge/THyasser1%20-%231DA1F2.svg?&style=for-the-badge&logo=Twitter&logoColor=white"/></code>
  </a>
</p>

## License 📄

[![MIT](https://img.shields.io/cocoapods/l/AFNetworking.svg?style=style&label=License&maxAge=2592000)](LICENSE)

Copyright (c) 2020
