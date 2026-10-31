# Quick Start Guide

## 🚀 Get Started in 5 Minutes

### Step 1: Setup Environment
```bash
# Navigate to project
cd "c:\Users\Ajaygowtham_S\OneDrive - Dell Technologies\Desktop\Selenium_Project"

# Create virtual environment
python -m venv venv

# Activate virtual environment
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Step 2: Configure Settings
```bash
# Copy environment template
copy .env.example .env

# Edit .env if needed (optional - defaults work fine)
```

### Step 3: Run Your First Job Search

**Option A: Using Standalone Script**
```bash
python job_search_agent.py "Python Developer" "New York"
```

**Option B: Using BDD Tests**
```bash
behave
```

### Step 4: Check Results
- **Output Files**: Check `output/` folder for job listings
- **Logs**: Check `logs/` folder for execution logs

## 📊 Example Commands

### Search for Different Positions
```bash
# Software Engineer in San Francisco
python job_search_agent.py "Software Engineer" "San Francisco" 3 json

# Data Analyst in Boston (save as CSV)
python job_search_agent.py "Data Analyst" "Boston" 5 csv

# QA Engineer in Seattle (save as Excel)
python job_search_agent.py "QA Engineer" "Seattle" 2 excel
```

### Run Specific BDD Scenarios
```bash
# Run only Milestone 1 tests
behave --tags=milestone1

# Run only Milestone 2 tests
behave --tags=milestone2

# Run with verbose output
behave -v
```

## 🎯 What Gets Extracted?

For each job, the tool extracts:
- ✅ Job Title
- ✅ Company Name
- ✅ Location
- ✅ Job Description
- ✅ Salary (if available)
- ✅ Job URL

## 🔧 Customization

### Change Browser
Edit `.env` file:
```env
BROWSER=chrome    # or firefox, edge
```

### Run in Headless Mode
Edit `.env` file:
```env
HEADLESS=True
```

### Change Number of Pages
Edit `.env` file:
```env
MAX_PAGES=10
```

Or pass as command argument:
```bash
python job_search_agent.py "Developer" "NYC" 10
```

## 📁 Project Structure Overview

```
Selenium_Project/
├── job_search_agent.py    # Main script - START HERE
├── features/              # BDD test scenarios
├── pages/                 # Page Object Models
├── utils/                 # Helper utilities
├── config/                # Configuration
├── output/                # Your results go here
└── logs/                  # Execution logs
```

## ❓ Troubleshooting

**Problem: Module not found**
```bash
# Make sure virtual environment is activated
venv\Scripts\activate
pip install -r requirements.txt
```

**Problem: Browser doesn't open**
```bash
# Check if Chrome/Firefox is installed
# Try different browser in .env file
```

**Problem: No jobs found**
```bash
# Run without headless to see what's happening
# Edit .env: HEADLESS=False
```

## 🎓 Next Steps

1. ✅ Run the examples above
2. ✅ Check the output files in `output/` folder
3. ✅ Review logs in `logs/` folder
4. ✅ Read full README.md for advanced usage
5. ✅ Customize search parameters in `.env`

## 💡 Pro Tips

- Start with 2-3 pages for testing
- Use headless mode for faster execution
- Check logs if something goes wrong
- JSON format is best for further processing
- CSV/Excel formats are great for manual review

Happy Job Hunting! 🎉
