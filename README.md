# Imdb Parser

Created using Flask Restful

## How to use

First, go to the backend directory and copy .env.example and rename it to .env
then make sure the path inside is correct.

To run flask, type the following (bash):

```bash
  source venv/Scripts/activate
  cd backend
  pip install -r requirements.txt
  flask run
```

## Tests

To run the tests, make sure pytest is installed, then run the tests in the backend directory

```bash
  pip install -U pytest
  pytest tests.py
```

## Postman

1. Run the app using the instructions mentioned above
2. Visit this postman collection [here](https://www.postman.com/blue-spaceship-413166/workspace/discoapp-workspace/request/14307953-9f02f0bf-31aa-49f7-b2fb-33212e4a141a)

## Stuff used

* flask
* pytest
* bridge design pattern (in feature 2: files converter)
* postman
