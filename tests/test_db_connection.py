# Pytest
import pytest

"""PyMongo"""

#Pymongo
from pymongo import MongoClient


@pytest.mark.usefixtures('config')
def test_db_connection_with_pymongo(client,config):
    """
    Test to verify connection with db 'sample_training'
    """
    result = get_coll_names(config)
    assert len(result) >=5


def get_coll_names(config):
    """
    Return collections in db 'sample_training'
    """
    db = MongoClient(config['MONGO_CLUSTER_URI'])[config['MONGO_DB']]
    return db.list_collection_names()


"""Mongo Engine"""

#Mongo Engine
from mongoengine import connect


@pytest.mark.usefixtures('config')
def test_db_connection_with_mongoengine(client,config):
    connection = connect(host="{}/{}?authSource=admin".format(config['MONGO_CLUSTER_URI'],config['MONGO_DB']))
    assert isinstance(connection, MongoClient)
