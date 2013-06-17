import os

# grabs the folder where the script runs
basedir = os.path.abspath(os.path.dirname(__file__))

DATABASE = 'flasktask.sqlite'
USERNAME = 'admin'
PASSWORD = 'admin'
SECRET_KEY = 'my precious'

# defines the full path for the database
DATABASE_PATH = os.path.join(basedir, DATABASE)

