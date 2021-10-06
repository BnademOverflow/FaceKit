# Facekit 🪐

![facekit](.github/header.svg)

<p align="center">
    <img src="https://img.shields.io/badge/Dev-Yezz123-green?style" />
    <img src="https://img.shields.io/badge/language-python-blue?style" />
    <img src="https://img.shields.io/static/v1?label=%F0%9F%8C%9F&message=If%20Useful&style=style=flat color=BC4E99"alt="Star Badge" />
</p>

A version of facebook using command line work on windows , macOS, linux created using python and flask with a lot of things.

including :

- uploaded photos
- tagged photos
- videos
- friends list and their profile photos (including Followers, Following, Work Friends, College Friends etc)
- and all public posts/statuses available on the user's timeline.
- check groups and invitation.

## Usage 🔧

### Prerequisites

- Python 3.6 or higher.
- Flask.
- Docker (Optional).

### Project setup

```sh
# clone the repo
$ git clone https://github.com/BnademOverflow/FaceKit

# move to the project folder
$ cd FaceKit
```

### Creating virtual environment

- Create a virtual environment using virtualenv.

```shell
# creating virtual environment
$ virtualenv venv

# activate virtual environment
$ source venv/bin/activate

# install all dependencies
$ pip install -r requirements.txt
```

### How to Run 🥶

- After install all what u need write :

```bash
python run.py
```

- and the code will run and u will find a menu like this :

  - 1). Go To Menu
  - 2). Start Web Version
  - 3). Login
  - 4). Logout
  - 5). Update
  - 0). Exit

- First step :

logging using facebook cookies.

```bash
   [?] Your Facebook Cookies:
```

- Then use it to start [FaceKit_web](FaceKit_web/start_web.py) or stay using command line by going to Menu!

## Running the Docker Container

- We have the Dockerfile created in above section. Now, we will use the Dockerfile to create the image of the Flask app and then start the app container.
- Using a preconfigured `Makefile` tor run the Docker Compose:

```sh
# Pull the latest image
$ make pull

# Build the image
$ make build

# Run the container
$ make start
```

 ---

## Important Message

This tool is for research purposes only. The developers of this tool won't be responsible for any misuse of data collected using this tool. Used by many researchers and open source intelligence (OSINT) analysts.

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

## License

This project is licensed under the terms of the MIT license.
