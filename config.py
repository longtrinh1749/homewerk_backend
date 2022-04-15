import os
from dotenv import load_dotenv

ROOT_DIR = os.path.abspath(os.path.join(
    os.path.dirname(__file__)
))

_DOT_ENV_PATH = os.path.join(ROOT_DIR, '.env')
load_dotenv(_DOT_ENV_PATH)

ENV_MODE = os.environ.get('ENV_MODE', '').upper()
DEBUG = os.getenv('FLASK_DEBUG') not in ('0', None)

MYSQL_DATABASE = os.getenv('MYSQL_DATABASE', 'homewerk')
MYSQL_HOST = os.getenv('MYSQL_HOST', 'localhost')
MYSQL_USER = os.getenv('MYSQL_USER', 'root')
MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD', 'root')
MYSQL_ROOT_PASSWORD = os.getenv('MYSQL_ROOT_PASSWORD', 'root')
MYSQL_FORWARD_PORT = os.getenv('MYSQL_FORWARD_PORT', '3306')