import pymysql
from pymysql.cursors import DictCursor

#General token for bots
Token = ''

#Connection to bd (mysql)
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

#Reactions roles
POST_ID = #post id

ROLES = {
    'smile roles': #id your roles,
}
    
MAX_ROLES_PER_USER = 3