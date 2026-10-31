# Automated Job Search Agent

A Selenium-based automation tool that automates the job search process on job boards like Indeed or LinkedIn. Built with Python and Behave BDD framework.

## Features

### ✅ Milestone 1: Website Navigation
**Requirements:**
- Use Selenium to open a job board website (Indeed)
- Automate the process of entering search criteria (job title, location)
- Navigate through the search results pages

**Implementation:**
- ✅ Automated navigation to Indeed job board
- ✅ Dynamic job search with customizable criteria (job title, location)
- ✅ Robust element location with multiple fallback strategies
- ✅ Smart waiting mechanisms for dynamic content
- ✅ Navigate through multiple search result pages

### ✅ Milestone 2: Data Extraction
**Requirements:**
- Extract relevant job listing details (title, company, location, description)
- Handle pagination to process multiple pages of results

**Implementation:**
- ✅ Extract comprehensive job details:
  - Job Title
  - Company Name
  - Location
  - Job Description
  - Salary Information (when available)
  - Job URL
- ✅ Intelligent pagination handling
- ✅ Multi-page data extraction (configurable)
- ✅ Save extracted job listings in structured formats:
  - CSV format
  - JSON format
  - Excel format
  - SQLite Database

### ⏸️ Milestone 3: Notification System (Excluded)
**Requirements:**
- Save extracted job listings in structured format (CSV, database)
- Implement email or desktop notification system

**Status:** Not implemented as per project requirements

## Project Structure

```
Selenium_Project/
├── config/
│   ├── __init__.py
│   └── config.py                 # Configuration and environment variables
├── features/
│   ├── steps/
│   │   └── job_search_steps.py  # BDD step definitions
│   ├── environment.py            # Behave hooks
│   └── job_search.feature        # BDD feature files
├── pages/
│   ├── __init__.py
│   ├── base_page.py             # Base Page Object Model
│   ├── indeed_search_page.py    # Search page POM
│   └── indeed_results_page.py   # Results page POM
├── utils/
│   ├── __init__.py
│   ├── logger.py                # Logging utility
│   ├── webdriver_factory.py     # WebDriver factory pattern
│   └── data_handler.py          # Data export utilities
├── output/                       # Generated job listings
├── logs/                         # Application logs
├── job_search_agent.py          # Standalone execution script
├── requirements.txt             # Python dependencies
├── behave.ini                   # Behave configuration
├── .env.example                 # Environment variables template
└── README.md                    # This file
```

## Design Patterns

1. **Page Object Model (POM)**: Separates page structure from test logic
2. **Factory Pattern**: WebDriver creation with browser abstraction
3. **Singleton Pattern**: Logger implementation
4. **Strategy Pattern**: Multiple data export formats

## Installation

### Prerequisites
- Python 3.8 or higher
- Chrome/Firefox/Edge browser installed

### Setup Steps

1. **Clone or navigate to the project directory**
   ```bash
   cd "c:\Users\Ajaygowtham_S\OneDrive - Dell Technologies\Desktop\Selenium_Project"
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**
   - Windows:
     ```bash
     venv\Scripts\activate
     ```
   - Linux/Mac:
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Configure environment variables**
   ```bash
   copy .env.example .env
   ```
   
   Edit `.env` file with your preferences:
   ```env
   JOB_BOARD_URL=https://www.indeed.com
   BROWSER=chrome
   HEADLESS=False
   IMPLICIT_WAIT=10
   EXPLICIT_WAIT=20
   PAGE_LOAD_TIMEOUT=30
   OUTPUT_FORMAT=json         # Options: json, csv, excel, database
   OUTPUT_PATH=./output
   MAX_PAGES=5
   ```

## Usage

### Method 1: Standalone Script

Run the job search agent directly:

```bash
python job_search_agent.py "Software Engineer" "New York" 3 json
```

**Parameters:**
- `job_title`: Job position to search for (required)
- `location`: Job location (required)
- `max_pages`: Number of pages to scrape (optional, default: 5)
- `output_format`: Output format - json/csv/excel (optional, default: json)

**Examples:**
```bash
python job_search_agent.py "Python Developer" "San Francisco"
python job_search_agent.py "Data Analyst" "Boston" 5 csv
python job_search_agent.py "QA Engineer" "Seattle" 2 excel
python job_search_agent.py "DevOps Engineer" "Austin" 3 database
```

### Method 2: BDD Tests with Behave

Run all BDD scenarios:
```bash
behave
```

Run specific scenarios by tag:
```bash
behave --tags=milestone1
behave --tags=milestone2
```

Run specific feature file:
```bash
behave features/job_search.feature
```

Generate detailed report:
```bash
behave -f allure_behave.formatter:AllureFormatter -o allure-results
```

## Configuration

### Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `JOB_BOARD_URL` | Indeed website URL | https://www.indeed.com |
| `BROWSER` | Browser to use (chrome/firefox/edge) | chrome |
| `HEADLESS` | Run browser in headless mode | False |
| `IMPLICIT_WAIT` | Implicit wait timeout (seconds) | 10 |
| `EXPLICIT_WAIT` | Explicit wait timeout (seconds) | 20 |
| `PAGE_LOAD_TIMEOUT` | Page load timeout (seconds) | 30 |
| `OUTPUT_FORMAT` | Default output format (json/csv/excel/database) | json |
| `OUTPUT_PATH` | Directory for output files | ./output |
| `MAX_PAGES` | Maximum pages to scrape | 5 |

## Output

Job listings are saved in the `output/` directory with the following structure:

**JSON Format:**
```json
[
  {
    "title": "Software Engineer",
    "company": "Tech Corp",
    "location": "New York, NY",
    "description": "We are looking for...",
    "salary": "$120K - $150K",
    "url": "https://indeed.com/..."
  }
]
```

**CSV/Excel Format:**
Tabular format with columns: title, company, location, description, salary, url

## Logging

Logs are stored in the `logs/` directory with daily rotation:
- Format: `<module_name>_YYYYMMDD.log`
- Levels: DEBUG (file), INFO (console)
- Includes timestamps, module names, and log levels

## Error Handling

The framework includes robust error handling:
- Multiple element locator strategies with fallbacks
- Graceful degradation when elements are not found
- Detailed error logging
- Browser cleanup on failure

## Best Practices Implemented

1. **Separation of Concerns**: Clear separation between page objects, tests, and utilities
2. **DRY Principle**: Reusable components and utilities
3. **Configuration Management**: Environment-based configuration
4. **Logging**: Comprehensive logging for debugging
5. **Exception Handling**: Graceful error handling and recovery
6. **Wait Strategies**: Smart explicit and implicit waits
7. **Code Modularity**: Small, focused, single-responsibility modules

## Troubleshooting

### Common Issues

1. **WebDriver not found**
   - Solution: The framework uses `webdriver-manager` which auto-downloads drivers
   - Ensure you have internet connection on first run

2. **Element not found errors**
   - Solution: Increase wait times in `.env` file
   - Indeed may have updated their HTML structure - check locators

3. **No jobs extracted**
   - Solution: Check if Indeed is accessible in your region
   - Try with headless mode disabled to see what's happening

4. **Import errors**
   - Solution: Ensure virtual environment is activated
   - Run `pip install -r requirements.txt` again

## Future Enhancements (Milestone 3)

- Email notification system
- Desktop notifications
- Job filtering based on criteria
- Duplicate job detection
- Database integration
- Scheduled automated searches
- Multi-job-board support (LinkedIn, Glassdoor)

## Contributing

This is a POC project. For production use:
- Add rate limiting to respect website policies
- Implement proxy rotation
- Add CAPTCHA handling
- Include unit tests
- Add CI/CD pipeline

## License

This project is for educational purposes only. Please respect Indeed's Terms of Service and robots.txt when using this tool.

## Support

For issues or questions, please check the logs in the `logs/` directory for detailed error information.
