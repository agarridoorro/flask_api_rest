from flask import Blueprint

bp_files = Blueprint('files', __name__)

from . import routes
