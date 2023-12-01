# KaloriKu_Backend

## Setup
The first thing to do is to clone the repository:
```sh
$ git clone https://github.com/gocardless/https://github.com/KaloriKu/KaloriKu_Backend.git
$ cd KaloriKu_Backend
```

Create .env file based on the .env.example:
```sh
DB_NAME=KaloriKu
DB_USER=postgres
DB_PASSWORD=postgres
DB_HOST=localhost
DB_PORT=5432
SECRET_KEY=HALOAKUGANTENG
```

Create a virtual environment to install dependencies in and activate it:
```sh
$ python -m venv env
$ env\Scripts\activate.bat
```

Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```
Note the `(env)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment.

Once `pip` has finished downloading the dependencies:
```sh
(env)$ python manage.py runserver
```
