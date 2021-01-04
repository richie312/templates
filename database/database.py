''' Database config '''
import json
import pymysql

with open('database_auth.json','r') as readfile:
    database_auth = json.load(readfile)
host = database_auth['host']
user = database_auth['dbuser']
passwd = database_auth['db_pass']
database = database_auth['dbname']


def db_connection():
    connection = pymysql.connect(host= host, user = user,
                             password = passwd)
    return connection

