import logging
from flask import jsonify, request
from werkzeug.exceptions import HTTPException

logger = logging.getLogger(__name__)

class AppContext:
    @staticmethod
    def register_error_handlers(app):
        @app.errorhandler(HTTPException)
        def http_handler(e):
            logger.exception(e)
            return jsonify({
                "code": e.code,
                "name": e.name,
                "description": e.description
            }), e.code

        @app.errorhandler(Exception)
        def exception_handler(e):
            logger.exception(e)
            return jsonify({
                "code": 500,
                "name": "Internal Server Error",
                "description": "The server encountered an internal error and was unable to complete your request. Either the server is overloaded or there is an error in the application."
            }), 500

    @staticmethod
    def register_interceptors(app):
        @app.before_request
        def log_request_info():
            logger.debug('Headers: %s', request.headers)
            logger.debug('Body: %s', request.get_data())