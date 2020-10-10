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
POST_ID = 731981491076333691
ROLES = {
    '💩': 715990789074714696,  #turd-code
    '<:jaba_jaba:731979672614731777>': 731975982256488469,  #Жаба
    '<:kchemusnyatsyalyagushki1:731979889154195566>': 731976126393745450,  #Главная Жаба
    '🤖': 731976556528009237,  #Отбитый
}
MAX_ROLES_PER_USER = 3