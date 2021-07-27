# App
from app import create_app

# Pytest
import pytest

# Core
import os
import configparser

# Pymongo
from pymongo import MongoClient

# MongoEngine
from mongoengine import connect

config = configparser.ConfigParser()
config.read(os.path.abspath(os.path.join(".ini")))


@pytest.fixture
def app():
    app = create_app()

    """App Config"""
    app.config['SECRET_KEY'] = config['TEST']['SECRET_KEY']
    app.config['MONGO_CLUSTER_URI'] = config['TEST']['MONGO_CLUSTER_URI']
    app.config['MONGO_DB'] = config['TEST']['MONGO_DB']

    return app

@pytest.fixture
def db():
    db = MongoClient(config['TEST']['MONGO_CLUSTER_URI'])[config['TEST']['MONGO_DB']]
    return db

@pytest.fixture
def connection():
    connection = connect(host="{}/{}?authSource=admin".format(config['TEST']['MONGO_CLUSTER_URI'],config['TEST']['MONGO_DB']))
    return connection
