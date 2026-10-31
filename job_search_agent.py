import sys
from utils.webdriver_factory import WebDriverFactory
from pages.indeed_search_page import IndeedSearchPage
from pages.indeed_results_page import IndeedResultsPage
from utils.data_handler import DataHandler
from utils.logger import Logger
from config.config import Config

logger = Logger.get_logger(__name__)

class JobSearchAgent:
    
    def __init__(self):
        self.driver = None
        self.search_page = None
        self.results_page = None
    
    def initialize(self):
        logger.info("Initializing Job Search Agent")
        Config.create_directories()
        self.driver = WebDriverFactory.get_driver()
        self.search_page = IndeedSearchPage(self.driver)
        self.results_page = IndeedResultsPage(self.driver)
    
    def search_and_extract_jobs(self, job_title, location, max_pages=None):
        try:
            max_pages = max_pages or Config.MAX_PAGES
            
            logger.info(f"Starting job search for '{job_title}' in '{location}'")
            
            self.search_page.open_indeed(Config.JOB_BOARD_URL)
            
            self.search_page.search_jobs(job_title, location)
            
            jobs_data = self.results_page.extract_jobs_from_multiple_pages(max_pages)
            
            logger.info(f"Successfully extracted {len(jobs_data)} jobs")
            
            return jobs_data
            
        except Exception as e:
            logger.error(f"Error during job search: {str(e)}")
            raise
    
    def save_results(self, jobs_data, format_type=None, filename=None):
        try:
            file_path = DataHandler.save_jobs(jobs_data, format_type, filename)
            logger.info(f"Results saved to: {file_path}")
            return file_path
        except Exception as e:
            logger.error(f"Error saving results: {str(e)}")
            raise
    
    def cleanup(self):
        if self.driver:
            self.driver.quit()
            logger.info("Browser closed")
    
    def run(self, job_title, location, max_pages=None, output_format=None):
        try:
            self.initialize()
            
            jobs_data = self.search_and_extract_jobs(job_title, location, max_pages)
            
            if jobs_data:
                file_path = self.save_results(jobs_data, output_format)
                logger.info(f"Job search completed successfully. Found {len(jobs_data)} jobs.")
                return jobs_data, file_path
            else:
                logger.warning("No jobs found matching the criteria")
                return [], None
                
        except Exception as e:
            logger.error(f"Job search failed: {str(e)}")
            raise
        finally:
            self.cleanup()

def main():
    if len(sys.argv) < 3:
        print("Usage: python job_search_agent.py <job_title> <location> [max_pages] [output_format]")
        print("Example: python job_search_agent.py 'Software Engineer' 'New York' 3 json")
        sys.exit(1)
    
    job_title = sys.argv[1]
    location = sys.argv[2]
    max_pages = int(sys.argv[3]) if len(sys.argv) > 3 else Config.MAX_PAGES
    output_format = sys.argv[4] if len(sys.argv) > 4 else Config.OUTPUT_FORMAT
    
    agent = JobSearchAgent()
    
    try:
        jobs_data, file_path = agent.run(job_title, location, max_pages, output_format)
        print(f"\n{'='*60}")
        print(f"Job Search Summary")
        print(f"{'='*60}")
        print(f"Search Query: {job_title} in {location}")
        print(f"Total Jobs Found: {len(jobs_data)}")
        print(f"Results Saved To: {file_path}")
        print(f"{'='*60}\n")
        
    except Exception as e:
        print(f"Error: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
