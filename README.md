#  CRUD
CRUD is a simple application for learn FastAPI




## Pre-requirements

- python >= 3.10.8
- poetry 1.2.2

## How to setup?
This project need poetry to run.
1. `poetry install`
2. `poetry shell`
3. run `pre-commit install` install to set up the git hook scripts

## How to run?
Run the server with:

`make run`

## What you can do?
http://0.0.0.0:8000/ (this is open api for test our application, you can execute api here)

1. create user http://0.0.0.0:8000/docs#/users/create_user_users__post
2. create article http://0.0.0.0:8000/docs#/articles/create_article_articles__user_id__post
3. create comment http://0.0.0.0:8000/docs#/comments/create_comment_comments__post
4. It also supports retrieve.

### User scenario
1. Create user
2. Create article
3. Create comment

### Create user
![this is api](img/Screenshot%202022-11-19%20at%2010.09.54%20AM.png)

![this is result](img/Screenshot%202022-11-19%20at%2010.10.22%20AM.png)

### Create article
![this is api](img/Screenshot%202022-11-19%20at%2010.12.39%20AM.png)
![this is result](img/Screenshot%202022-11-19%20at%2010.12.46%20AM.png)

### Create comment
![this is api](img/Screenshot%202022-11-19%20at%2010.17.25%20AM.png)
![this is result](img/Screenshot%202022-11-19%20at%2010.17.31%20AM.png)


## Project structure


<pre>
.
├── README.md
├── app
│   ├── init.py
│   ├── api
│   │   ├── init.py
│   │   ├── main.py
│   │   └── sql_app.db
│   ├── crud
│   │   ├── init.py
│   │   ├── articles.py
│   │   ├── comments.py
│   │   └── users.py
│   ├── db
│   │   ├── init.py
│   │   ├── base_class.py
│   │   └── session.py
│   ├── models
│   │   ├── init.py
│   │   ├── articles.py
│   │   ├── base.py
│   │   ├── comments.py
│   │   └── users.py
│   └── schemas
│       ├── init.py
│       ├── articles.py
│       ├── comments.py
│       └── users.py
├── poetry.lock
└── pyproject.toml
</pre>

## DB ERD


![This is an image](img/erd.png)


## Class diagram

![This is an Image](img/mermaid-diagram-2022-11-23-191222.png)