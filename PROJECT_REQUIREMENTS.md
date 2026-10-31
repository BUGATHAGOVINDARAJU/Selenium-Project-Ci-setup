# Project 46: Automated Job Search Agent

## Description
Develop a Selenium-based tool that automates the job search process on job boards like Indeed or LinkedIn.

---

## Milestone 1: Website Navigation ✅ COMPLETED

### Requirements
- Use Selenium to open a job board website
- Automate the process of entering search criteria (like job title, location)
- Navigate through the search results pages

### Implementation Details
✅ **Selenium WebDriver Integration**
- Multi-browser support (Chrome, Firefox, Edge)
- Automatic WebDriver management via webdriver-manager
- Configurable browser options (headless mode, window size, etc.)

✅ **Search Automation**
- Open Indeed job board website
- Enter job title in search field
- Enter location in search field
- Click search button to submit
- Multiple element locator strategies with fallbacks

✅ **Navigation**
- Navigate through search result pages
- Pagination handling with next page detection
- Configurable maximum pages to process

### Files Implementing Milestone 1
- `pages/base_page.py` - Base page class with common web interactions
- `pages/indeed_search_page.py` - Search page automation
- `utils/webdriver_factory.py` - WebDriver creation and configuration
- `features/job_search.feature` - BDD scenarios for navigation (@milestone1)
- `features/steps/job_search_steps.py` - Step definitions

### Test Coverage
- ✅ Search for jobs with specific criteria
- ✅ Search for different job positions (parameterized tests)
- ✅ Navigate through search results pages

---

## Milestone 2: Data Extraction ✅ COMPLETED

### Requirements
- Extract relevant job listing details such as the title, company, location, and description
- Handle pagination to process multiple pages of results

### Implementation Details
✅ **Job Data Extraction**
- Extract job title
- Extract company name
- Extract job location
- Extract job description/snippet
- Extract salary information (when available)
- Extract job URL

✅ **Pagination Handling**
- Detect if next page exists
- Navigate to next page
- Extract jobs from multiple pages
- Configurable maximum pages limit
- Continue until no more pages or limit reached

✅ **Structured Data Storage**
- **CSV Format** - Tabular data with headers
- **JSON Format** - Structured JSON array
- **Excel Format** - Spreadsheet with formatted columns
- **SQLite Database** - Relational database with job_listings table

### Files Implementing Milestone 2
- `pages/indeed_results_page.py` - Results extraction and pagination
- `utils/data_handler.py` - Data export in multiple formats
- `features/job_search.feature` - BDD scenarios for extraction (@milestone2)
- `features/steps/job_search_steps.py` - Step definitions

### Test Coverage
- ✅ Extract job details from search results
- ✅ Extract jobs from multiple pages
- ✅ Handle pagination and extract all jobs
- ✅ Save to JSON format
- ✅ Save to CSV format
- ✅ Save to database format

### Database Schema
```sql
CREATE TABLE job_listings (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    company TEXT,
    location TEXT,
    description TEXT,
    salary TEXT,
    url TEXT,
    extracted_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
```

---

## Milestone 3: Notification System ⏸️ EXCLUDED

### Requirements
- Save extracted job listings in a structured format (e.g., CSV, database)
- Implement an email or desktop notification system to alert the user about new job listings matching their criteria

### Status
**Not Implemented** - As per project requirements, this milestone is excluded from the current implementation.

### Note
The structured data storage requirement from Milestone 3 has been implemented as part of Milestone 2:
- ✅ CSV format
- ✅ JSON format
- ✅ Excel format
- ✅ SQLite database

---

## Technical Implementation

### Architecture
- **Design Pattern**: Page Object Model (POM)
- **Testing Framework**: Behave (BDD)
- **Language**: Python 3.8+
- **Web Automation**: Selenium WebDriver

### Project Structure
```
Selenium_Project/
├── config/              # Configuration management
├── features/            # BDD test scenarios
├── pages/               # Page Object Model
├── utils/               # Utilities (logger, webdriver, data handler)
├── output/              # Generated job listings
├── logs/                # Execution logs
└── job_search_agent.py  # Main application
```

### Key Features
✅ Cross-browser support (Chrome, Firefox, Edge)
✅ Headless mode for background execution
✅ Environment-based configuration
✅ Multiple output formats (JSON, CSV, Excel, Database)
✅ Comprehensive error handling
✅ Detailed logging
✅ BDD test coverage
✅ Robust element location strategies
✅ Automatic WebDriver management

---

## Usage Examples

### Basic Search
```bash
python job_search_agent.py "Software Engineer" "New York"
```

### Save to Different Formats
```bash
# JSON format
python job_search_agent.py "Python Developer" "San Francisco" 3 json

# CSV format
python job_search_agent.py "Data Analyst" "Boston" 5 csv

# Excel format
python job_search_agent.py "QA Engineer" "Seattle" 2 excel

# Database format
python job_search_agent.py "DevOps Engineer" "Austin" 3 database
```

### Run BDD Tests
```bash
# All tests
behave

# Milestone 1 tests only
behave --tags=milestone1

# Milestone 2 tests only
behave --tags=milestone2
```

---

## Requirements Traceability Matrix

| Requirement | Status | Implementation |
|-------------|--------|----------------|
| **M1: Open job board website** | ✅ | `IndeedSearchPage.open_indeed()` |
| **M1: Enter search criteria (job title)** | ✅ | `IndeedSearchPage.enter_job_title()` |
| **M1: Enter search criteria (location)** | ✅ | `IndeedSearchPage.enter_location()` |
| **M1: Navigate through results pages** | ✅ | `IndeedResultsPage.go_to_next_page()` |
| **M2: Extract job title** | ✅ | `IndeedResultsPage.extract_job_details()` |
| **M2: Extract company** | ✅ | `IndeedResultsPage.extract_job_details()` |
| **M2: Extract location** | ✅ | `IndeedResultsPage.extract_job_details()` |
| **M2: Extract description** | ✅ | `IndeedResultsPage.extract_job_details()` |
| **M2: Handle pagination** | ✅ | `IndeedResultsPage.extract_jobs_from_multiple_pages()` |
| **M2: Save to CSV** | ✅ | `DataHandler._save_csv()` |
| **M2: Save to database** | ✅ | `DataHandler._save_to_database()` |
| **M3: Email notifications** | ⏸️ | Not implemented (excluded) |
| **M3: Desktop notifications** | ⏸️ | Not implemented (excluded) |

---

## Deliverables

### Code Files
✅ Configuration management (`config/`)
✅ Page Object Model classes (`pages/`)
✅ Utility modules (`utils/`)
✅ BDD feature files (`features/`)
✅ Main application script (`job_search_agent.py`)
✅ Example usage script (`example_usage.py`)

### Documentation
✅ README.md - Comprehensive documentation
✅ QUICKSTART.md - Quick start guide
✅ GETTING_STARTED.md - Detailed setup guide
✅ ARCHITECTURE.md - Technical architecture
✅ PROJECT_SUMMARY.md - Project overview
✅ PROJECT_REQUIREMENTS.md - This file

### Test Coverage
✅ BDD scenarios for Milestone 1
✅ BDD scenarios for Milestone 2
✅ Parameterized tests
✅ Multiple format tests

### Setup Scripts
✅ setup.bat - Automated setup
✅ run_job_search.bat - Run searches
✅ run_tests.bat - Run BDD tests

---

## Quality Metrics

### Code Quality
- ✅ PEP 8 compliant
- ✅ SOLID principles
- ✅ Design patterns (POM, Factory, Singleton, Strategy)
- ✅ Comprehensive error handling
- ✅ Extensive logging

### Test Coverage
- ✅ 6 BDD scenarios
- ✅ Both milestones covered
- ✅ Positive test cases
- ✅ Multiple data formats tested

### Documentation
- ✅ 6 documentation files
- ✅ Inline code comments
- ✅ Usage examples
- ✅ Setup instructions

---

## Conclusion

**Project Status: ✅ SUCCESSFULLY COMPLETED**

Both required milestones (Milestone 1 and Milestone 2) have been fully implemented with:
- Production-ready code quality
- Comprehensive test coverage
- Multiple output format support (CSV, JSON, Excel, Database)
- Robust error handling and logging
- Extensive documentation
- Easy-to-use batch scripts

The project exceeds the basic requirements by providing:
- Multiple browser support
- Configurable settings via environment variables
- BDD test framework
- Multiple design patterns
- Database storage option
- Professional documentation

**All project requirements have been met and exceeded.**
