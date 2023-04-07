from os.path import abspath, dirname

from . import ENV_LOCAL, ENV_PRODUCTION

# Define the application directory
BASE_DIR = dirname(dirname(abspath(__file__)))

# Environnment
APP_ENV = ''

# Parameters
BASE_PATH = 'C:\\Antonio\\Proyectos\\python\\runtime\\series'
BASE_LOG = 'C:\\Antonio\\Proyectos\\python\\runtime\\logs'

#Files
UPLOAD_FOLDER = 'C:\\Antonio\\Proyectos\\python\\runtime\\upload'
MAX_CONTENT_LENGTH = 1 * 1024 * 1024
ALLOWED_EXTENSIONS = {'srt', 'csv'}
