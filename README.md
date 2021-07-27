##Description
This project was created by make examples of different packages of python and flask
like:

1. pymongo
2. mongoengine
3. pytest
4. pytest-flask



## Requirements

Server of Mongo DB (atlas) with db 'sample_training' this db is part of 
mongo data examples

Load Sample Data:
This is the *[Load Sample Data Guide](https://docs.mongodb.com/charts/saas/tutorial/order-data/prerequisites-setup/)*.

## Installation

Create virtual env

```bash
    virtualenv venv
```

Activate virtual env

```bash 
    source venv/bin/activate
```

## Quickstart

Install dependencies using requirements.text

```bash
    pip install -r requirements.txt
```

Add your Mongo credentials in example_ini and create .ini file with

```bash
    cp example_ini .ini
```

## Testing

Run test to verify connection with 'sample_training' db

```bash
    pytest tests/test_db_connection.py
```
Run all tests

```bash
    pytest
```
