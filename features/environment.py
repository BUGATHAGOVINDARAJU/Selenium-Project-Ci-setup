import sys
import traceback
from utils.webdriver_factory import WebDriverFactory
from utils.logger import Logger
from config.config import Config

logger = Logger.get_logger(__name__)

def before_all(context):
    Config.create_directories()
    logger.info("Test execution started")

def before_scenario(context, scenario):
    logger.info(f"Starting scenario: {scenario.name}")
    
    try:
        # Attempt to get the configured driver
        context.driver = WebDriverFactory.get_driver()
        context.jobs_data = []
    except Exception as hook_error:
        # --- LOOP BREAKER & DIAGNOSTIC LOG ---
        print("\n" + "!"*60, file=sys.stderr)
        print("CRITICAL DRIVER INITIALIZATION FAILED!", file=sys.stderr)
        print("The exact Python failure causing the crash is detailed below:", file=sys.stderr)
        print("-" * 60, file=sys.stderr)
        # Prints the exact line number and code file that caused the crash
        traceback.print_exc(file=sys.stderr) 
        print("!"*60 + "\n", file=sys.stderr)
        
        # Hard exit the process immediately so Chrome doesn't loop/flash repeatedly
        sys.exit(1)

def after_scenario(context, scenario):
    logger.info(f"Completed scenario: {scenario.name} - Status: {scenario.status}")
    if hasattr(context, 'driver') and context.driver:
        try:
            context.driver.quit()
            logger.info("Browser closed")
        except Exception:
            pass

def after_all(context):
    logger.info("Test execution completed")