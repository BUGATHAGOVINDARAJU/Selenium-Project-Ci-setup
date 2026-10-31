import logging
import os
from datetime import datetime
from config.config import Config

class Logger:
    _loggers = {}
    
    @staticmethod
    def get_logger(name):
        if name in Logger._loggers:
            return Logger._loggers[name]
        
        Config.create_directories()
        
        logger = logging.getLogger(name)
        logger.setLevel(getattr(logging, Config.LOG_LEVEL))
        
        if not logger.handlers:
            log_file = os.path.join(
                Config.LOG_PATH,
                f"{name}_{datetime.now().strftime('%Y%m%d')}.log"
            )
            
            file_handler = logging.FileHandler(log_file)
            file_handler.setLevel(logging.DEBUG)
            
            console_handler = logging.StreamHandler()
            console_handler.setLevel(logging.INFO)
            
            formatter = logging.Formatter(
                '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                datefmt='%Y-%m-%d %H:%M:%S'
            )
            
            file_handler.setFormatter(formatter)
            console_handler.setFormatter(formatter)
            
            logger.addHandler(file_handler)
            logger.addHandler(console_handler)
        
        Logger._loggers[name] = logger
        return logger
