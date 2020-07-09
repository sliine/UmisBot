import pymysql
from pymysql.cursors import DictCursor

Token = ''

config = {
    'user': '',
    'password': '',
    'host': '',
    'database': '',
}

connection = pymysql.connect(host=config.get('host'),
                             user=config.get('user'),
                             password=config.get('password'),
                             db=config.get('database'),
                             charset='utf8mb4',
                             cursorclass=DictCursor)