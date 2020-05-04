import logging
import settings

class Logger(object):
    def __init__(self,file_path,level):
        file_handler = logging.FileHandler(file_path, 'a', encoding='utf-8')
        fmt = logging.Formatter(fmt="%(asctime)s - %(name)s - %(levelname)s -%(module)s:  %(message)s")
        file_handler.setFormatter(fmt)

        self.logger = logging.Logger('cmdb', level=level)
        self.logger.addHandler(file_handler)

    def error(self,msg):
        self.logger.error(msg)

logger = Logger(settings.LOGGING_PATH,logging.DEBUG)