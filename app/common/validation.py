from werkzeug.exceptions import BadRequest
from flask import current_app

from config import CFG_ALLOWED_EXTENSIONS
from .stringutils import StringUtils

class RequestValidator:
    @staticmethod
    def validate_json(request, *args):
        content_type = request.headers.get('Content-Type')
        if (content_type != 'application/json'):
            raise BadRequest("Content type not supported")
        body = request.get_json()
        if body is None:
            raise BadRequest("The request body is null")

        for arg in args:
            if arg not in body:
                raise BadRequest('parameter {0} is missing'.format(arg))

        return None

    @staticmethod
    def validate_form(request, *args):
        for arg in args:
            if arg not in request.form:
                raise BadRequest('{0} is missing in request'.format(arg))
            value = request.form[arg]
            if StringUtils.is_blank(value):
                raise BadRequest('{0} is blank in request'.format(arg))
        return None

    @staticmethod
    def validate_file(request, filename):
        if filename not in request.files:
            raise BadRequest('{0} is missing in request'.format(filename))
        file = request.files['file']
        if file.filename == '':
            raise BadRequest('{0} is missing in request'.format(filename))
        if not file or not RequestValidator.__allowed_file(file.filename):
            raise BadRequest('{0} has an invalid extension'.format(filename))
        return file

    @staticmethod
    def __allowed_file(filename):
        return '.' in filename and \
            filename.rsplit('.', 1)[1].lower() in current_app.config[CFG_ALLOWED_EXTENSIONS] 
       