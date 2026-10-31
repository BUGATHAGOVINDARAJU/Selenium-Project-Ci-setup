from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from config.config import Config
from utils.logger import Logger

logger = Logger.get_logger(__name__)

class BasePage:
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, Config.EXPLICIT_WAIT)
    
    def find_element(self, locator, timeout=None):
        try:
            wait_time = timeout or Config.EXPLICIT_WAIT
            element = WebDriverWait(self.driver, wait_time).until(
                EC.presence_of_element_located(locator)
            )
            return element
        except TimeoutException:
            logger.error(f"Element not found: {locator}")
            raise
    
    def find_elements(self, locator, timeout=None):
        try:
            wait_time = timeout or Config.EXPLICIT_WAIT
            elements = WebDriverWait(self.driver, wait_time).until(
                EC.presence_of_all_elements_located(locator)
            )
            return elements
        except TimeoutException:
            logger.warning(f"Elements not found: {locator}")
            return []
    
    def click(self, locator, timeout=None):
        try:
            element = self.wait_for_clickable(locator, timeout)
            element.click()
            logger.debug(f"Clicked element: {locator}")
        except Exception as e:
            logger.error(f"Failed to click element {locator}: {str(e)}")
            raise
    
    def send_keys(self, locator, text, timeout=None):
        try:
            element = self.find_element(locator, timeout)
            element.clear()
            element.send_keys(text)
            logger.debug(f"Entered text '{text}' in element: {locator}")
        except Exception as e:
            logger.error(f"Failed to send keys to {locator}: {str(e)}")
            raise
    
    def get_text(self, locator, timeout=None):
        try:
            element = self.find_element(locator, timeout)
            return element.text
        except Exception as e:
            logger.error(f"Failed to get text from {locator}: {str(e)}")
            return ""
    
    def get_attribute(self, locator, attribute, timeout=None):
        try:
            element = self.find_element(locator, timeout)
            return element.get_attribute(attribute)
        except Exception as e:
            logger.error(f"Failed to get attribute '{attribute}' from {locator}: {str(e)}")
            return ""
    
    def wait_for_clickable(self, locator, timeout=None):
        try:
            wait_time = timeout or Config.EXPLICIT_WAIT
            element = WebDriverWait(self.driver, wait_time).until(
                EC.element_to_be_clickable(locator)
            )
            return element
        except TimeoutException:
            logger.error(f"Element not clickable: {locator}")
            raise
    
    def is_element_present(self, locator, timeout=5):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator)
            )
            return True
        except TimeoutException:
            return False
    
    def scroll_to_element(self, locator):
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        logger.debug(f"Scrolled to element: {locator}")
    
    def execute_script(self, script, *args):
        return self.driver.execute_script(script, *args)
    
    def get_current_url(self):
        return self.driver.current_url
    
    def navigate_to(self, url):
        logger.info(f"Navigating to: {url}")
        self.driver.get(url)
