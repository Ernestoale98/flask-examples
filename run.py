# App
from app import create_app

#Core
import os
import configparser

config = configparser.ConfigParser()
config.read(os.path.abspath(os.path.join(".ini")))

if __name__ == '__main__':
    app = create_app()

    """App Config"""
    app.config['DEBUG'] = True
    app.config['SECRET_KEY'] = config['TEST']['SECRET_KEY']
    app.config['MONGO_CLUSTER_URI'] = config['TEST']['MONGO_CLUSTER_URI']
    app.config['MONGO_DB'] = config['TEST']['MONGO_DB']


    app.run()
