import os
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()

class Config:
    BASE_DIR = Path(__file__).resolve().parent.parent
    
    JOB_BOARD_URL = os.getenv('JOB_BOARD_URL', 'https://www.indeed.com')
    BROWSER = os.getenv('BROWSER', 'chrome')
    HEADLESS = os.getenv('HEADLESS', 'False').lower() == 'true'
    
    IMPLICIT_WAIT = int(os.getenv('IMPLICIT_WAIT', '10'))
    EXPLICIT_WAIT = int(os.getenv('EXPLICIT_WAIT', '20'))
    PAGE_LOAD_TIMEOUT = int(os.getenv('PAGE_LOAD_TIMEOUT', '30'))
    
    OUTPUT_FORMAT = os.getenv('OUTPUT_FORMAT', 'json')
    OUTPUT_PATH = os.getenv('OUTPUT_PATH', str(BASE_DIR / 'output'))
    MAX_PAGES = int(os.getenv('MAX_PAGES', '5'))
    
    LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')
    LOG_PATH = os.getenv('LOG_PATH', str(BASE_DIR / 'logs'))
    
    @classmethod
    def create_directories(cls):
        os.makedirs(cls.OUTPUT_PATH, exist_ok=True)
        os.makedirs(cls.LOG_PATH, exist_ok=True)
