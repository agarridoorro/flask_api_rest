from flask import Flask

from .cfg.log import Log
from .cfg.app_context import AppContext
from .common.serialization import GenericEncoder

encoder = GenericEncoder()

def create_app(settings_module):
    app = Flask(__name__)
    app.config.from_object(settings_module)

    Log.configure(app)

    # Registro de los Blueprints
    from .explorer import bp_explorer
    app.register_blueprint(bp_explorer, url_prefix='/explorer')
    from .files import bp_files
    app.register_blueprint(bp_files, url_prefix='/files')

    AppContext.register_error_handlers(app)
    #AppContext.register_interceptors(app)

    return app

