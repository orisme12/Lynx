# Welcome to development to commerce API

If you already cloned the repository and you know that you need to deep dive in the code, here are some guidelines to set up your environment.


### Virtual enviroment with `pipenv`

#### Install pipenv

```sh
pip install pipenv
```

#### Initialize virutal enviroment

```sh
pipenv shell
```

#### Building dependecies

It will install all the dependencies and your local FastAPI in your local environment.

```sh
pipenv run pip install -r requirements.txt
```

#### Run server with `uvicorn`

Alredy for development...

```shell
pipenv run dev # uvicorn src.main:app --reload
```

### Thank for read

Now I will teach you the development tools... Go `doc/tools_development.md`