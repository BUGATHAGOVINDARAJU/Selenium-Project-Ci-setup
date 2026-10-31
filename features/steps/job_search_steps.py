from behave import given, when, then
from pages.indeed_search_page import IndeedSearchPage
from pages.indeed_results_page import IndeedResultsPage
from utils.data_handler import DataHandler
from config.config import Config
from utils.logger import Logger

logger = Logger.get_logger(__name__)


import csv
import os
import logging
from behave import then
from pages.indeed_results_page import IndeedResultsPage

logger = logging.getLogger(__name__)

@given('I am on the Indeed job board website')
def step_open_indeed(context):
    context.search_page = IndeedSearchPage(context.driver)
    context.search_page.open_indeed(Config.JOB_BOARD_URL)
    logger.info("Opened Indeed website")

@when('I enter "{job_title}" as job title')
def step_enter_job_title(context, job_title):
    context.search_page = IndeedSearchPage(context.driver)
    context.search_page.enter_job_title(job_title)
    context.job_title = job_title

@when('I enter "{location}" as location')
def step_enter_location(context, location):
    context.search_page = IndeedSearchPage(context.driver)
    context.search_page.enter_location(location)
    context.location = location

@when('I click the search button')
def step_click_search(context):
    context.search_page = IndeedSearchPage(context.driver)
    context.search_page.click_search_button()

@when('I search for "{job_title}" jobs in "{location}"')
def step_search_jobs(context, job_title, location):
    context.search_page = IndeedSearchPage(context.driver)
    context.search_page.search_jobs(job_title, location)
    context.job_title = job_title
    context.location = location

@when('I extract jobs from {num_pages:d} pages')
def step_extract_multiple_pages(context, num_pages):
    context.results_page = IndeedResultsPage(context.driver)
    context.jobs_data = context.results_page.extract_jobs_from_multiple_pages(num_pages)
    logger.info(f"Extracted {len(context.jobs_data)} jobs from {num_pages} pages")

@when('I navigate through all available pages up to {max_pages:d} pages')
def step_navigate_all_pages(context, max_pages):
    context.results_page = IndeedResultsPage(context.driver)
    context.jobs_data = context.results_page.extract_jobs_from_multiple_pages(max_pages)

@then('I should see job search results')
def step_verify_results(context):
    context.results_page = IndeedResultsPage(context.driver)
    job_cards = context.results_page.get_job_cards()
    assert len(job_cards) > 0, "No job search results found"
    logger.info(f"Verified {len(job_cards)} job results are displayed")

# @then('I should be able to extract job listings with following details')
# def step_extract_job_details(context):
#     context.results_page = IndeedResultsPage(context.driver)
#     jobs = context.results_page.extract_all_jobs_on_page()
    
#     assert len(jobs) > 0, "No jobs extracted"
    
#     required_fields = [row['title'] for row in context.table]
    
#     for job in jobs[:3]:
#         for field in required_fields:
#             assert field in job, f"Field '{field}' not found in job data"
#             logger.debug(f"Verified field '{field}' exists in job data")
    
#     context.jobs_data = jobs
#     logger.info(f"Successfully extracted and verified {len(jobs)} job listings")

from behave import then
import logging

logger = logging.getLogger(__name__)

# @then('I should be able to extract job listings with following details:')
# def step_extract_job_details(context):
    # context.results_page = IndeedResultsPage(context.driver)
    
    # # 1. Safely wrap the selenium call to turn unhandled crashes into clean test failures
    # try:
    #     jobs = context.results_page.extract_all_jobs_on_page()
    # except Exception as e:
    #     assert False, f"Selenium browser extraction crashed entirely: {str(e)}"
    
    # # 2. Check if anything was actually found
    # assert len(jobs) > 0, "No jobs extracted from the page at all"
    
    # # 3. Correctly parse the list of required fields from the Gherkin table.
    # # Assumes your feature table column header is named 'field_name' or 'details'.
    # # Adjust 'field_name' below to match the exact column header in your .feature file!
    # try:
    #     required_fields = [row[context.table.headings[0]] for row in context.table]
    # except IndexError:
    #     assert False, "The Gherkin step table must have at least one column describing required fields."

    # # 4. Validate that the dictionary keys match what was requested
    # for index, job in enumerate(jobs[:3]):
    #     for field in required_fields:
    #         assert field in job, (
    #             f"Field verification failed on job sample #{index + 1}. "
    #             f"Expected key '{field}' to exist in extracted dictionary, but it was missing. "
    #             f"Extracted keys available: {list(job.keys())}"
    #         )
    #         logger.debug(f"Verified field '{field}' exists in job data")
    
    # context.jobs_data = jobs
    # logger.info(f"Successfully extracted and verified {len(jobs)} job listings")

@then('I should be able to extract job listings with following details:')
def step_extract_job_details(context):
    if not hasattr(context, 'results_page'):
        context.results_page = IndeedResultsPage(context.driver)
    
    # Define how many pages you want to scrape (e.g., 3 pages)
    MAX_PAGES_TO_SCRAPE = 3
    logger.info(f"Executing Milestone 2: Scraping up to {MAX_PAGES_TO_SCRAPE} pages of results...")
    
    # 1. Call the multi-page tracking method you built in your page object
    jobs = context.results_page.extract_jobs_from_multiple_pages(max_pages=MAX_PAGES_TO_SCRAPE)
    
    # 2. Validation Check
    assert len(jobs) > 0, "Scraper returned 0 jobs across all pages. Check browser state."
    
    # 3. SAVE THE MULTI-PAGE DATA TO CSV IMMEDIATELY
    csv_file_path = os.path.join(os.getcwd(), "extracted_jobs.csv")
    fieldnames = ['title', 'company', 'location', 'description', 'salary', 'url']
    
    try:
        with open(csv_file_path, mode='w', newline='', encoding='utf-8-sig') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(jobs)
        
        # Terminal confirmation banner
        print("\n" + "═"*70)
        print(f"   🎉 MILESTONE 2 & 3: MULTI-PAGE EXTRACTION COMPLETE! 🎉")
        print(f"   📍 FILE LOCATION: {csv_file_path}")
        print(f"   📝 TOTAL COMBINED JOBS SAVED: {len(jobs)}")
        print("═"*70 + "\n")
        
    except Exception as csv_error:
        logger.error(f"Critical error writing pagination data to CSV: {str(csv_error)}")
        raise csv_error

    context.jobs_data = jobs

    
@then('I should have extracted multiple job listings')
def step_verify_multiple_jobs(context):
    assert len(context.jobs_data) > 0, "No jobs were extracted"
    logger.info(f"Verified {len(context.jobs_data)} jobs were extracted")

@then('the job listings should be saved in "{format_type}" format')
def step_save_jobs(context, format_type):
    file_path = DataHandler.save_jobs(context.jobs_data, format_type)
    assert file_path is not None, "Failed to save job listings"
    logger.info(f"Job listings saved to {file_path}")

@then('all job listings should be extracted')
def step_verify_all_jobs_extracted(context):
    assert len(context.jobs_data) > 0, "No jobs were extracted"
    logger.info(f"Total jobs extracted: {len(context.jobs_data)}")

@then('the data should be saved to output directory')
def step_save_to_output(context):
    file_path = DataHandler.save_jobs(context.jobs_data)
    assert file_path is not None, "Failed to save job listings"
    logger.info(f"Data saved to {file_path}")
