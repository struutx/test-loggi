# Loggi Test

- To run this API, must follow the steps below:
	1. Clone this repository to your computer
	2. With Dokcker installed on your machine, run on root level ```docker-compose up -d``` to create the PostgreSQL container
	3. Fill the `.env` file with the environment variables describe below.
	4. On project root, run: ```pip3 install -r requirements.txt```
	5. On same level, run: ```python3 manage.py makemigrations``` and after ```python3 manage.py migrate```
	6. Run: ```python3 manage.py runserver```


## Environment Variables
```
SECRET_KEY=django-insecure-r52!n^fmq$&za1-2s1eg)%)ua255w+n=nypxoqumeb=i326z8)
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_HOST=127.0.0.1
POSTGRES_DATABASE=loggi
```

## Postman Requests

- List Users [GET]: ``curl --location 'localhost:8000/test/users/list'``
- Create User [POST]: ```curl --location 'localhost:8000/test/users/create' \ 	--header 'Content-Type: application/json' \ --data-raw '{"name": "UserTest", "email": "testuser@email.com}'```
- Update User [PUT]: ```curl --location 'localhost:8000/test/users/create' \ 	--header 'Content-Type: application/json' \ --data-raw '{"user_id": "f5d94138-1236-409e-9d0f-c46014897562", "email": "testuser@email.com}'```
