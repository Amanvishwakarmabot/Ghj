import os
from os import getenv, environ
from dotenv import load_dotenv



load_dotenv()

class Var(object):
    MULTI_CLIENT = False
    API_ID = int(getenv('API_ID', '24004349'))
    API_HASH = str(getenv('API_HASH', '5aabfb11c262b17d568d828a3100f296'))
    BOT_TOKEN = str(getenv('BOT_TOKEN', '6568488552:AAGUd-ZIsr9EeflSgbdhIoPXSMnidRdUoPA'))
    name = str(getenv('name', 'MovieStorage0_BBot'))
    SLEEP_THRESHOLD = int(getenv('SLEEP_THRESHOLD', '60'))
    WORKERS = int(getenv('WORKERS', '4'))
    BIN_CHANNEL = int(getenv('BIN_CHANNEL', '-1002062708890'))
    PORT = int(getenv('PORT', 8080))
    BIND_ADRESS = str(getenv('WEB_SERVER_BIND_ADDRESS', '0.0.0.0'))
    PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
    OWNER_ID = set(int(x) for x in os.environ.get("OWNER_ID", "5977931010").split())  
    NO_PORT = bool(getenv('NO_PORT', False))
    APP_NAME = None
    OWNER_USERNAME = str(getenv('OWNER_USERNAME', 'BOT_OWNER26'))
    if 'DYNO' in environ:
        ON_HEROKU = True
        APP_NAME = str(getenv('APP_NAME'))
    
    else:
        ON_HEROKU = False
    FQDN = str(getenv('FQDN', BIND_ADRESS)) if not ON_HEROKU or getenv('FQDN') else APP_NAME+'.herokuapp.com'
    HAS_SSL=bool(getenv('HAS_SSL', True))
    if HAS_SSL:
        URL = "https://vifhb-z80b.onrender.com/".format(FQDN)
    else:
        URL = "https://vifhb-z80b.onrender.com/".format(FQDN)
    DATABASE_URL = str(getenv('DATABASE_URL', 'mongodb+srv://Aman:aman@cluster0.cnjkitd.mongodb.net/?retryWrites=true&w=majority'))
    UPDATES_CHANNEL = str(getenv('UPDATES_CHANNEL', 'MOVIEBOTUPDETA'))
    BANNED_CHANNELS = list(set(int(x) for x in str(getenv("BANNED_CHANNELS", "-1002055043634")).split()))
    SHORTLINK_URL = getenv('SHORTLINK_URL', '')
    SHORTLINK_API = getenv('SHORTLINK_API', '')
    TUTORIAL_URL = getenv('TUTORIAL_URL', '')    
