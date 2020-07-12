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
Post_Id = 0 #id your post
Roles = {
    'emoji': #id your roles,
    'emoji': #id your roles,
    'emoji': #id your roles,
    'emoji': #id your roles,
}
Excroles = {}
Max_Roles_Per_User = 3