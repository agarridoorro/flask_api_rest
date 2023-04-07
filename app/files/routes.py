import logging
import os
from flask import request, jsonify, current_app
from werkzeug.utils import secure_filename

from config import CFG_UPLOAD_FOLDER
from . import bp_files
from ..common.validation import RequestValidator

logger = logging.getLogger(__name__)

#https://pythonbasics.org/flask-upload-file/
#https://flask.palletsprojects.com/en/2.1.x/patterns/fileuploads/
@bp_files.route('/uploader', methods = ['POST'])
def upload_file():
    RequestValidator.validate_form(request, 'name')
    file = RequestValidator.validate_file(request, 'file')
    name = secure_filename(request.form['name'])
    file.save(os.path.join(current_app.config[CFG_UPLOAD_FOLDER], name))
    return jsonify({"message" : 'file uploaded successfully'})