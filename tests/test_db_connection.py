#Pytest
import pytest

#Pymongo
from pymongo import MongoClient



@pytest.mark.connection
@pytest.mark.usefixtures('config')
def test_db_setup(client,config):
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
