# Getting Started with Automated Job Search Agent

## 🎯 What This Tool Does

This tool automatically searches for jobs on Indeed, extracts job details, and saves them in structured formats (JSON, CSV, or Excel). It's built with Python, Selenium, and Behave BDD framework.

## 📋 Prerequisites

Before you begin, ensure you have:
- ✅ Python 3.8 or higher installed
- ✅ Chrome, Firefox, or Edge browser installed
- ✅ Internet connection
- ✅ Windows OS (batch scripts provided for Windows)

## 🚀 Installation & Setup

### Option 1: Automated Setup (Recommended)

1. **Open Command Prompt** in the project directory
2. **Run the setup script**:
   ```bash
   setup.bat
   ```
3. **Wait for installation to complete** (may take 2-3 minutes)

### Option 2: Manual Setup

1. **Create Virtual Environment**:
   ```bash
   python -m venv venv
   ```

2. **Activate Virtual Environment**:
   ```bash
   venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Create Environment File**:
   ```bash
   copy .env.example .env
   ```

## ⚙️ Configuration (Optional)

Edit the `.env` file to customize settings:

```env
# Job Board Configuration
JOB_BOARD_URL=https://www.indeed.com

# Browser Settings
BROWSER=chrome          # Options: chrome, firefox, edge
HEADLESS=False         # Set to True for background execution

# Timeout Settings (in seconds)
IMPLICIT_WAIT=10
EXPLICIT_WAIT=20
PAGE_LOAD_TIMEOUT=30

# Output Settings
OUTPUT_FORMAT=json     # Options: json, csv, excel
OUTPUT_PATH=./output
MAX_PAGES=5           # Maximum pages to scrape
```

## 🎮 How to Use

### Method 1: Quick Run with Batch File

**Basic Usage**:
```bash
run_job_search.bat "Job Title" "Location"
```

**Examples**:
```bash
run_job_search.bat "Software Engineer" "New York"
run_job_search.bat "Python Developer" "San Francisco" 3 json
run_job_search.bat "Data Analyst" "Boston" 5 csv
```

**Parameters**:
1. Job Title (required) - e.g., "Software Engineer"
2. Location (required) - e.g., "New York"
3. Max Pages (optional) - e.g., 3 (default: 5)
4. Output Format (optional) - json/csv/excel (default: json)

### Method 2: Direct Python Execution

```bash
# Activate virtual environment first
venv\Scripts\activate

# Run the script
python job_search_agent.py "Software Engineer" "New York" 3 json
```

### Method 3: BDD Tests

**Run all tests**:
```bash
run_tests.bat
```

**Or manually**:
```bash
venv\Scripts\activate
behave
```

**Run specific tests**:
```bash
behave --tags=milestone1    # Navigation tests
behave --tags=milestone2    # Data extraction tests
```

### Method 4: Python Code

Create a Python script:

```python
from job_search_agent import JobSearchAgent

# Initialize agent
agent = JobSearchAgent()

# Run job search
jobs_data, file_path = agent.run(
    job_title="Python Developer",
    location="San Francisco",
    max_pages=3,
    output_format="json"
)

# Print results
print(f"Found {len(jobs_data)} jobs")
print(f"Saved to: {file_path}")
```

## 📊 Understanding the Output

### Output Location
Results are saved in the `output/` directory with timestamp:
- `output/job_listings_20260628_143022.json`
- `output/job_listings_20260628_143022.csv`
- `output/job_listings_20260628_143022.xlsx`

### Output Structure

**JSON Format**:
```json
[
  {
    "title": "Senior Software Engineer",
    "company": "Tech Corp",
    "location": "New York, NY",
    "description": "We are looking for an experienced...",
    "salary": "$120K - $150K",
    "url": "https://indeed.com/viewjob?jk=..."
  },
  {
    "title": "Python Developer",
    "company": "StartUp Inc",
    "location": "San Francisco, CA",
    "description": "Join our team...",
    "salary": "",
    "url": "https://indeed.com/viewjob?jk=..."
  }
]
```

**CSV/Excel Format**:
| title | company | location | description | salary | url |
|-------|---------|----------|-------------|--------|-----|
| Senior Software Engineer | Tech Corp | New York, NY | We are looking... | $120K - $150K | https://... |

## 📝 Logs

Execution logs are saved in the `logs/` directory:
- `logs/job_search_agent_20260628.log`
- `logs/__main___20260628.log`

**Log Format**:
```
2026-06-28 14:30:22 - job_search_agent - INFO - Starting job search for 'Software Engineer' in 'New York'
2026-06-28 14:30:25 - indeed_search_page - INFO - Opened Indeed job board
2026-06-28 14:30:28 - indeed_results_page - INFO - Found 15 job cards on current page
```

## 🔍 What Gets Extracted?

For each job listing, the tool extracts:

| Field | Description | Always Available? |
|-------|-------------|-------------------|
| **Title** | Job position title | ✅ Yes |
| **Company** | Company name | ✅ Yes |
| **Location** | Job location | ✅ Yes |
| **Description** | Job description snippet | ✅ Yes |
| **Salary** | Salary information | ⚠️ Sometimes |
| **URL** | Link to job posting | ✅ Yes |

## 🎯 Common Use Cases

### Use Case 1: Daily Job Search
```bash
# Search for your target role daily
run_job_search.bat "Your Job Title" "Your City" 5 json
```

### Use Case 2: Multiple Searches
```bash
# Search for different positions
run_job_search.bat "Software Engineer" "New York" 3 json
run_job_search.bat "Data Scientist" "San Francisco" 3 json
run_job_search.bat "Product Manager" "Seattle" 3 json
```

### Use Case 3: Export for Analysis
```bash
# Export to Excel for manual review
run_job_search.bat "Python Developer" "Boston" 5 excel

# Export to CSV for data analysis
run_job_search.bat "Data Analyst" "Chicago" 5 csv
```

### Use Case 4: Automated Testing
```bash
# Run BDD tests to verify functionality
run_tests.bat
```

## ⚡ Performance Tips

1. **Start Small**: Begin with 2-3 pages for testing
2. **Use Headless Mode**: Set `HEADLESS=True` in `.env` for faster execution
3. **Adjust Timeouts**: Increase timeouts if you have slow internet
4. **Close Other Browsers**: Free up system resources

## 🐛 Troubleshooting

### Problem: "Python not found"
**Solution**: Install Python 3.8+ from python.org

### Problem: "Module not found"
**Solution**: 
```bash
venv\Scripts\activate
pip install -r requirements.txt
```

### Problem: "Browser doesn't open"
**Solution**: 
- Ensure Chrome/Firefox/Edge is installed
- Try different browser in `.env` file
- Check if webdriver-manager can download drivers

### Problem: "No jobs found"
**Solution**:
- Run with `HEADLESS=False` to see what's happening
- Check if Indeed is accessible in your region
- Try different search terms
- Check logs in `logs/` directory

### Problem: "Element not found"
**Solution**:
- Increase timeout values in `.env`
- Indeed may have updated their website
- Check logs for specific error details

### Problem: "Permission denied"
**Solution**:
- Run Command Prompt as Administrator
- Check antivirus isn't blocking execution
- Ensure output directory is writable

## 📚 Next Steps

1. **Read the Documentation**:
   - `README.md` - Comprehensive guide
   - `QUICKSTART.md` - Quick reference
   - `ARCHITECTURE.md` - Technical details
   - `PROJECT_SUMMARY.md` - Project overview

2. **Try Examples**:
   ```bash
   python example_usage.py
   ```

3. **Run Tests**:
   ```bash
   run_tests.bat
   ```

4. **Customize**:
   - Modify `.env` for your preferences
   - Adjust search parameters
   - Try different output formats

## 🎓 Learning Resources

### Understanding the Code
- `pages/` - Page Object Model implementation
- `utils/` - Utility functions and helpers
- `features/` - BDD test scenarios
- `config/` - Configuration management

### Design Patterns Used
- **Page Object Model**: Separates UI from logic
- **Factory Pattern**: Browser creation
- **Singleton Pattern**: Logger instance
- **Strategy Pattern**: Multiple export formats

## ✅ Verification Checklist

After setup, verify everything works:

- [ ] Virtual environment created
- [ ] Dependencies installed
- [ ] `.env` file exists
- [ ] Can run: `python job_search_agent.py --help` (should show usage)
- [ ] Can run: `behave --version` (should show version)
- [ ] `output/` directory exists
- [ ] `logs/` directory exists

## 🎉 You're Ready!

You now have a fully functional automated job search agent. Start with a simple search:

```bash
run_job_search.bat "Software Engineer" "New York" 2 json
```

Check the `output/` folder for your results!

## 💡 Pro Tips

1. **Batch Processing**: Create a batch file with multiple searches
2. **Schedule Execution**: Use Windows Task Scheduler for daily runs
3. **Data Analysis**: Import JSON/CSV into Excel or Python for analysis
4. **Filtering**: Post-process results to filter by keywords
5. **Tracking**: Keep historical data to track job market trends

## 📞 Need Help?

1. Check the logs: `logs/` directory
2. Review documentation: `README.md`, `QUICKSTART.md`
3. Verify configuration: `.env` file
4. Test with simple search first
5. Run with `HEADLESS=False` to see browser actions

---

**Happy Job Hunting! 🚀**

For detailed technical information, see `ARCHITECTURE.md`
For quick reference, see `QUICKSTART.md`
For complete guide, see `README.md`
