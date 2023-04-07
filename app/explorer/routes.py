import logging
from flask import request, jsonify, current_app

from app import encoder

from config import CFG_BASE_PATH
from . import bp_explorer
from .services import ExplorerService
from ..common.validation import RequestValidator

logger = logging.getLogger(__name__)

@bp_explorer.route("/dirItems", methods=['GET'])
def getDirItems():
    basePath = current_app.config[CFG_BASE_PATH]
    items = ExplorerService.getDirectoryItems(basePath)
    return jsonify(items)

@bp_explorer.route("/dirItems", methods=['POST'])
def postDirItems():
    #logger.debug('llega un post')
    RequestValidator.validate_json(request, 'path')
    body = request.get_json()
    items = ExplorerService.getDirectoryItems(body['path'])
    #return Response(encoder.toJson(items), mimetype='application/json')
    return jsonify(items)