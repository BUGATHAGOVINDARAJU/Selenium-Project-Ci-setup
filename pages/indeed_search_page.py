from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
import time
import random  # <-- Added for generating human-like typing intervals
from pages.base_page import BasePage
from utils.logger import Logger

logger = Logger.get_logger(__name__)

class IndeedSearchPage(BasePage):
    
    SEARCH_WHAT_INPUT = (By.ID, "text-input-what")
    SEARCH_WHERE_INPUT = (By.ID, "text-input-where")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    
    ALTERNATIVE_WHAT_INPUT = (By.CSS_SELECTOR, "input[name='q']")
    ALTERNATIVE_WHERE_INPUT = (By.CSS_SELECTOR, "input[name='l']")
    
    def __init__(self, driver):
        super().__init__(driver)
    
    def open_indeed(self, url):
        self.navigate_to(url)
        logger.info("Opened Indeed job board")
        time.sleep(2)

    def _send_keys_humanly(self, locator, text):
        """
        Internal helper to simulate genuine human typing variance.
        Bypasses Cloudflare's keystroke speed threshold telemetry.
        """
        element = self.find_element(locator)
        element.clear()
        
        for character in text:
            element.send_keys(character)
            # Delays human hand movements randomly between 60ms and 180ms
            time.sleep(random.uniform(0.06, 0.18))
    
    def enter_job_title(self, job_title):
        try:
            if self.is_element_present(self.SEARCH_WHAT_INPUT, timeout=5):
                self._send_keys_humanly(self.SEARCH_WHAT_INPUT, job_title)
            elif self.is_element_present(self.ALTERNATIVE_WHAT_INPUT, timeout=5):
                self._send_keys_humanly(self.ALTERNATIVE_WHAT_INPUT, job_title)
            else:
                logger.error("Could not find job title input field")
                raise Exception("Job title input field not found")
            
            logger.info(f"Entered job title humanly: {job_title}")
        except Exception as e:
            logger.error(f"Failed to enter job title: {str(e)}")
            raise
    
    def enter_location(self, location):
        try:
            if self.is_element_present(self.SEARCH_WHERE_INPUT, timeout=5):
                self._send_keys_humanly(self.SEARCH_WHERE_INPUT, location)
            elif self.is_element_present(self.ALTERNATIVE_WHERE_INPUT, timeout=5):
                self._send_keys_humanly(self.ALTERNATIVE_WHERE_INPUT, location)
            else:
                logger.error("Could not find location input field")
                raise Exception("Location input field not found")
            
            logger.info(f"Entered location humanly: {location}")
        except Exception as e:
            logger.error(f"Failed to enter location: {str(e)}")
            raise
    
    def click_search_button(self):
        """
        Submits the form utilizing keyboard execution rather than mouse coordinates.
        This evades the 'isTrusted = false' flag attached to automated mouse clicks.
        """
        try:
            if self.is_element_present(self.SEARCH_BUTTON, timeout=5):
                element = self.find_element(self.SEARCH_BUTTON)
                # FIX: Sending Keys.ENTER to the button strips the automated mouse click fingerprinting
                element.send_keys(Keys.ENTER)
                logger.info("Submitted search form via ENTER key action on Search button")
                time.sleep(3)
            else:
                logger.warning("Search button not found, falling back to location input field submission")
                element = self.find_element(self.SEARCH_WHERE_INPUT)
                element.send_keys(Keys.RETURN)
                time.sleep(3)
        except Exception as e:
            logger.error(f"Failed to submit search: {str(e)}")
            raise
    
    def search_jobs(self, job_title, location):
        self.enter_job_title(job_title)
        self.enter_location(location)
        self.click_search_button()
        logger.info(f"Searched for '{job_title}' in '{location}'")