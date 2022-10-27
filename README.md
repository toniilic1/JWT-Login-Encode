### JWT Login Encode

[![File Number](https://img.shields.io/github/directory-file-count/toniilic1/JWT-Login-Encode "File Number")](https://github.com/toniilic1/JWT-Login-Encode)
[![Size](https://img.shields.io/github/repo-size/toniilic1/JWT-Login-Encode)](https://github.com/toniilic1/JWT-Login-Encode)
[![Commits](https://img.shields.io/github/commit-activity/m/toniilic1/JWT-Login-Encode)](https://github.com/toniilic1/JWT-Login-Encode/graphs/commit-activity)
[![License](https://img.shields.io/github/license/toniilic1/JWT-Login-Encode "License")](https://github.com/toniilic1/JWT-Login-Encode/blob/master/LICENSE.txt "License")

## Introduction
A Python project using PyJWT library in order to create tokens for clients when they log into the system.

Using sqlite3 a database and a table is creataed containing three clients which are searched with two inputs. Error is shown if the client does not exist.

Otherwise a token is created which is valid for the next 45 seconds and is inserted into the database for the corresponding client.

## Installation
1. Clone the project:
- ```git clone https://github.com/toniilic1/JWT-Login-Encode```

2. Create a virtual env:
- ```py -m venv .venv```
- ```.venv\scripts\activate```

3. Install the jwt:
- ```pip install pyjwt```
or
- ```pip install -r requirements.txt```

## License

MIT
