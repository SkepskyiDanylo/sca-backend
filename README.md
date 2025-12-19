# Spy Cat Agency Backend

SCA - The spy agency like in the movies, but with cats instead of people:)


## How to run:

### Configure virtual environment:

```
    python -m venv .venv
```

### Install requirements:

```bash
    pip install -r requirements.txt
```

### Configure [.env](env.sample) file:

```bash
    touch .env
```

`SECRET_KEY` as Django secret ket and a breed validation `API_URL`

### Apply the migrations:

```bash
    python manage.py migrate
```

### Run the server:
```bash
    python manage.py runserver
```

## All endpoints you can see on `/swagger` endpoint

While developing `SQLITE` db is being used, but for production it's better to set a `PostgreSQL` or kinda database.