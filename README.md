# Flask API endpoint

## Installation

```
git clone https://github.com/dlpazs/test_flask_api.git
python -m venv env
env\Scripts\activate
pip install -r requirements.txt
python run.py
```

## API

* Navigate to `localhost:5000` to see the swagger api documents and to test the endpoints.

```
GET: /users
```
* Returns people who are either listed as living in London or whose current coordinates are within 50 miles of London.

```
GET: /users/london
```
* Returns people who are listed as living in London

```
GET: /users/london/proximity
```
* Returns people whose current coordinates are within 50 miles of London.

## Testing

* From the app's root directory and in a new terminal with the existing flask app running:

```
env\Scripts\activate
pytest -q app/test_router.py
```

## Production

* Change the `app/__init__.py` line 5 from `app.config.from_object('config.DevConfig')` to `app.config.from_object('config.ProdConfig')`
