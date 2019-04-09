import json
import logging.config
from os import path


def logger_config():
    with open(path.join(path.abspath(path.dirname(__file__)), 'config.json')) as file:
        print(file)
        return json.load(file)


log_config = logger_config()


def logger_path(path_to_file):
    def log(function):
        def decor_log(*args, **kwargs):
            log_config["handlers"]["fileHandler"]["filename"] = path.join(path_to_file, 'Logs.log')
            logging.config.dictConfig(log_config)
            logger = logging.getLogger("logInfo")
            logger.info(f'Вызов функции {function.__name__} c параметрами {args, kwargs}')
            result = function(*args, **kwargs)
            logger.info(f'Функция вернула результат {result}')
            return result
        return decor_log
    return log
