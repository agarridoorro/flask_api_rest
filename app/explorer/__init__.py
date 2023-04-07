from flask import Blueprint

bp_explorer = Blueprint('explorer', __name__)

from . import routes
