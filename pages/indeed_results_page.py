from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import time
from pages.base_page import BasePage
from utils.logger import Logger
from config.config import Config  # Imported to restore original timeouts

logger = Logger.get_logger(__name__)

class IndeedResultsPage(BasePage):
    
    JOB_CARDS = (By.CSS_SELECTOR, "div.job_seen_beacon")
    JOB_CARD_ALTERNATIVE = (By.CSS_SELECTOR, "div.cardOutline")
    JOB_CARD_ALTERNATIVE_2 = (By.CSS_SELECTOR, "td.resultContent")
    
    SALARY_INFO = (By.CSS_SELECTOR, "div.salary-snippet-container, div.metadata.salary-snippet-container")
    JOB_METADATA = (By.CSS_SELECTOR, "div.metadata")
    
    NEXT_PAGE_BUTTON = (By.CSS_SELECTOR, "a[data-testid='pagination-page-next']")
    NEXT_PAGE_ALTERNATIVE = (By.CSS_SELECTOR, "a[aria-label='Next Page']")
    NEXT_PAGE_ALTERNATIVE_2 = (By.XPATH, "//a[contains(@aria-label, 'Next')]")
    
    def __init__(self, driver):
        super().__init__(driver)
    
    def get_job_cards(self):
        try:
            if self.is_element_present(self.JOB_CARDS, timeout=10):
                cards = self.find_elements(self.JOB_CARDS)
            elif self.is_element_present(self.JOB_CARD_ALTERNATIVE, timeout=5):
                cards = self.find_elements(self.JOB_CARD_ALTERNATIVE)
            elif self.is_element_present(self.JOB_CARD_ALTERNATIVE_2, timeout=5):
                cards = self.find_elements(self.JOB_CARD_ALTERNATIVE_2)
            else:
                logger.warning("No job cards found on page")
                return []
            
            logger.info(f"Found {len(cards)} job cards on current page")
            return cards
        except Exception as e:
            logger.error(f"Error getting job cards: {str(e)}")
            return []
    
    def extract_job_details(self, job_card):
        job_data = {
            'title': '',
            'company': '',
            'location': '',
            'description': '',
            'salary': '',
            'url': ''
        }
        
        # Modernized arrays of locator tuples to bypass Indeed's dynamic styling
        title_selectors = [
            (By.CSS_SELECTOR, "a.jcs-JobTitle"),
            (By.CSS_SELECTOR, "h2.jobTitle span[id^='jobTitle-']"),
            (By.CSS_SELECTOR, "h2.jobTitle span"),
            (By.CSS_SELECTOR, "h2.jobTitle a")
        ]
        
        company_selectors = [
            (By.CSS_SELECTOR, "span[data-testid='company-name']"),
            (By.CSS_SELECTOR, "span.css-63be0t"),
            (By.CSS_SELECTOR, "span.companyName"),
            (By.CSS_SELECTOR, ".company_location .companyName")
        ]
        
        location_selectors = [
            (By.CSS_SELECTOR, "div[data-testid='text-location']"),
            (By.CSS_SELECTOR, "div.css-1resta1"),
            (By.CSS_SELECTOR, "div.companyLocation")
        ]
        
        snippet_selectors = [
            (By.CSS_SELECTOR, "div.job-snippet"),
            (By.CSS_SELECTOR, "div[class*='snippet']"),
            (By.CSS_SELECTOR, "div.underLine")
        ]
        
        try:
            # 1. Extract Title & Optional Job URL
            for selector in title_selectors:
                try:
                    title_element = job_card.find_element(*selector)
                    job_data['title'] = title_element.text.strip()
                    href = title_element.get_attribute('href')
                    if href:
                        job_data['url'] = href
                    if job_data['title']:
                        break
                except NoSuchElementException:
                    continue
            if not job_data['title']:
                logger.warning("Job title not found for this card")
            
            # 2. Extract Company Name
            for selector in company_selectors:
                try:
                    job_data['company'] = job_card.find_element(*selector).text.strip()
                    if job_data['company']:
                        break
                except NoSuchElementException:
                    continue
            
            # 3. Extract Location
            for selector in location_selectors:
                try:
                    job_data['location'] = job_card.find_element(*selector).text.strip()
                    if job_data['location']:
                        break
                except NoSuchElementException:
                    continue
            
            # 4. Extract Job Snippet Description
            for selector in snippet_selectors:
                try:
                    job_data['description'] = job_card.find_element(*selector).text.strip().replace('\n', ' ')
                    if job_data['description']:
                        break
                except NoSuchElementException:
                    continue
            
            # 5. Extract Salary Details
            try:
                job_data['salary'] = job_card.find_element(*self.SALARY_INFO).text.strip()
            except NoSuchElementException:
                pass
                
            logger.debug(f"Extracted job: {job_data['title']} at {job_data['company']}")
            
        except Exception as e:
            logger.error(f"Error extracting job details: {str(e)}")
        
        return job_data
    
    def extract_all_jobs_on_page(self):
        jobs = []
        job_cards = self.get_job_cards()
        
        # --- SPEED VALVE ACTIVATION ---
        # Drop implicit wait to 0.5s so missing selectors fail instantly instead of freezing the thread
        self.driver.implicitly_wait(0.5)
        
        for index, card in enumerate(job_cards, 1):
            try:
                job_data = self.extract_job_details(card)
                if job_data['title']:
                    jobs.append(job_data)
            except Exception as e:
                logger.error(f"Error processing job card {index}: {str(e)}")
                continue
        
        # --- RESTORE FRAMEWORK TIMEOUT ---
        self.driver.implicitly_wait(Config.IMPLICIT_WAIT)
        
        logger.info(f"Extracted {len(jobs)} jobs from current page")
        return jobs
    
    def has_next_page(self):
        try:
            if self.is_element_present(self.NEXT_PAGE_BUTTON, timeout=3):
                return True
            elif self.is_element_present(self.NEXT_PAGE_ALTERNATIVE, timeout=2):
                return True
            elif self.is_element_present(self.NEXT_PAGE_ALTERNATIVE_2, timeout=2):
                return True
            return False
        except Exception as e:
            logger.debug(f"Error checking for next page: {str(e)}")
            return False
    
    def go_to_next_page(self):
        try:
            if self.is_element_present(self.NEXT_PAGE_BUTTON, timeout=5):
                self.click(self.NEXT_PAGE_BUTTON)
            elif self.is_element_present(self.NEXT_PAGE_ALTERNATIVE, timeout=3):
                self.click(self.NEXT_PAGE_ALTERNATIVE)
            elif self.is_element_present(self.NEXT_PAGE_ALTERNATIVE_2, timeout=3):
                self.click(self.NEXT_PAGE_ALTERNATIVE_2)
            else:
                logger.warning("Next page button not found")
                return False
            
            logger.info("Navigated to next page")
            time.sleep(4)  # Anti-bot delay to let the next page build naturally
            return True
        except Exception as e:
            logger.error(f"Error navigating to next page: {str(e)}")
            return False
    
    def extract_jobs_from_multiple_pages(self, max_pages):
        all_jobs = []
        current_page = 1
        
        while current_page <= max_pages:
            logger.info(f"Processing page {current_page} of {max_pages}")
            
            jobs_on_page = self.extract_all_jobs_on_page()
            all_jobs.extend(jobs_on_page)
            
            if current_page < max_pages and self.has_next_page():
                if not self.go_to_next_page():
                    logger.warning("Could not navigate to next page, stopping pagination")
                    break
                current_page += 1
            else:
                logger.info("No more pages available or reached max pages")
                break
        
        logger.info(f"Total jobs extracted: {len(all_jobs)} from {current_page} pages")
        return all_jobs