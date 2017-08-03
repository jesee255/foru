import os

basedir = os.path.abspath(os.path.dirname(__file__))

secret_key = 'randomstr'

# db_uri = 'mysql+pymysql://root:sqlpassword@localhost/forum'
db_uri = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')