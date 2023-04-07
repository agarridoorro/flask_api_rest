import os
import logging
from logging.handlers import RotatingFileHandler

from config import *

class Log:
    @staticmethod
    def configure(app):
        # Eliminamos los posibles manejadores, si existen, del logger por defecto
        del app.logger.handlers[:]

        # Añadimos el logger por defecto a la lista de loggers
        loggers = [app.logger, logging.getLogger('werkzeug')]
        handlers = []

        # Creamos un manejador para escribir los mensajes por consola
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(Log.__verbose_formatter())
        # Creamos un manejador para escribir los mensajes a fichero
        log_root = app.config[CFG_BASE_LOG]
        file_handler = RotatingFileHandler(os.path.join(log_root, 'logExplorer.txt'), mode='a', encoding="utf-8", maxBytes=1024 * 1024, backupCount=10)
        file_handler.setFormatter(Log.__verbose_formatter())

        level = logging.INFO
        if app.config[CFG_APP_ENV] == ENV_LOCAL:
            level = logging.DEBUG
        elif app.config[CFG_APP_ENV] == ENV_PRODUCTION:
            level = logging.ERROR

        console_handler.setLevel(level)
        handlers.append(console_handler)
        file_handler.setLevel(level)
        handlers.append(file_handler)

        # Asociamos cada uno de los handlers a cada uno de los loggers
        for l in loggers:
            for handler in handlers:
                l.addHandler(handler)
            l.propagate = False
            l.setLevel(logging.DEBUG)

    @staticmethod
    def __verbose_formatter():
        return logging.Formatter(
            '[%(asctime)s.%(msecs)d]\t %(levelname)s \t[%(name)s.%(funcName)s:%(lineno)d]\t %(message)s',
            datefmt='%d/%m/%Y %H:%M:%S'
        )