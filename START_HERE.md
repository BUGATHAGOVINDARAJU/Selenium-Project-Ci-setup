# 🚀 START HERE - Automated Job Search Agent

Welcome to the **Automated Job Search Agent** project! This guide will help you get started quickly.

---

## ⚡ Quick Start (5 Minutes)

### Step 1: Setup
```bash
setup.bat
```
This will install everything you need automatically.

### Step 2: Run Your First Search
```bash
run_job_search.bat "Software Engineer" "New York"
```

### Step 3: Check Results
- Open the `output/` folder to see your job listings
- Check `logs/` folder for execution details

**That's it! You're done!** 🎉

---

## 📖 Documentation Guide

Choose the right documentation for your needs:

### 🎯 **For First-Time Users**
👉 **[GETTING_STARTED.md](GETTING_STARTED.md)** - Complete setup and usage guide
- Installation instructions
- Configuration options
- Usage examples
- Troubleshooting

### ⚡ **For Quick Reference**
👉 **[QUICKSTART.md](QUICKSTART.md)** - 5-minute quick reference
- Essential commands
- Common use cases
- Pro tips

### 📚 **For Complete Information**
👉 **[README.md](README.md)** - Comprehensive documentation
- Full feature list
- Detailed usage
- Configuration options
- Output formats

### 🏗️ **For Technical Details**
👉 **[ARCHITECTURE.md](ARCHITECTURE.md)** - Technical architecture
- Design patterns
- Component interaction
- Code structure
- Extensibility

### 📋 **For Project Overview**
👉 **[PROJECT_REQUIREMENTS.md](PROJECT_REQUIREMENTS.md)** - Requirements & implementation
- Milestone details
- Requirements traceability
- Test coverage
- Deliverables

### 📊 **For Project Summary**
👉 **[FINAL_SUMMARY.md](FINAL_SUMMARY.md)** - Complete project summary
- Milestone completion status
- Technical implementation
- Statistics
- Highlights

### ✅ **For Completion Status**
👉 **[PROJECT_COMPLETION.txt](PROJECT_COMPLETION.txt)** - Completion checklist
- Files created
- Features implemented
- Configuration options
- Next steps

---

## 🎮 How to Use

### Method 1: Batch Files (Easiest)
```bash
# Setup (one-time)
setup.bat

# Run job search
run_job_search.bat "Job Title" "Location"

# Run tests
run_tests.bat
```

### Method 2: Python Script
```bash
# Activate environment
venv\Scripts\activate

# Run search
python job_search_agent.py "Python Developer" "San Francisco" 3 json
```

### Method 3: BDD Tests
```bash
# Activate environment
venv\Scripts\activate

# Run all tests
behave

# Run specific milestone
behave --tags=milestone1
behave --tags=milestone2
```

---

## 📂 Project Structure

```
Selenium_Project/
├── 📁 config/              Configuration & settings
├── 📁 features/            BDD test scenarios
├── 📁 pages/               Page Object Model classes
├── 📁 utils/               Utility modules
├── 📁 output/              Your job listings go here ⭐
├── 📁 logs/                Execution logs
├── 📄 job_search_agent.py  Main application
├── 📄 example_usage.py     Usage examples
└── 📄 Documentation files  You are here!
```

---

## 🎯 What This Tool Does

1. **Opens Indeed job board** automatically
2. **Enters your search criteria** (job title, location)
3. **Navigates through results** pages
4. **Extracts job details**:
   - Job Title
   - Company Name
   - Location
   - Description
   - Salary (when available)
   - Job URL
5. **Saves to multiple formats**:
   - JSON
   - CSV
   - Excel
   - SQLite Database

---

## 💡 Common Use Cases

### Daily Job Search
```bash
run_job_search.bat "Your Job Title" "Your City" 5 json
```

### Export for Analysis
```bash
# Excel for manual review
run_job_search.bat "Data Analyst" "Boston" 5 excel

# CSV for data analysis
run_job_search.bat "Python Developer" "NYC" 3 csv

# Database for querying
run_job_search.bat "Software Engineer" "SF" 5 database
```

### Multiple Searches
```bash
run_job_search.bat "Frontend Developer" "Seattle" 3 json
run_job_search.bat "Backend Developer" "Austin" 3 json
run_job_search.bat "Full Stack Developer" "Denver" 3 json
```

---

## ⚙️ Configuration

Edit `.env` file to customize:

```env
BROWSER=chrome              # chrome, firefox, edge
HEADLESS=False             # True for background mode
OUTPUT_FORMAT=json         # json, csv, excel, database
MAX_PAGES=5               # Pages to scrape
```

---

## 🆘 Troubleshooting

### Problem: "Python not found"
**Solution:** Install Python 3.8+ from python.org

### Problem: "Module not found"
**Solution:**
```bash
venv\Scripts\activate
pip install -r requirements.txt
```

### Problem: "Browser doesn't open"
**Solution:**
- Ensure Chrome/Firefox/Edge is installed
- Try different browser in `.env` file

### Problem: "No jobs found"
**Solution:**
- Set `HEADLESS=False` in `.env` to see what's happening
- Check logs in `logs/` folder

---

## 📊 Output Examples

### JSON Output
```json
[
  {
    "title": "Senior Software Engineer",
    "company": "Tech Corp",
    "location": "New York, NY",
    "description": "We are looking for...",
    "salary": "$120K - $150K",
    "url": "https://indeed.com/..."
  }
]
```

### CSV Output
Opens in Excel with columns: title, company, location, description, salary, url

### Database Output
SQLite database with `job_listings` table - queryable with SQL

---

## ✅ Verification Checklist

After setup, verify:
- [ ] Virtual environment created (`venv/` folder exists)
- [ ] Dependencies installed (no errors from setup.bat)
- [ ] `.env` file exists
- [ ] Can run: `run_job_search.bat "Test" "Test"`
- [ ] `output/` folder created
- [ ] `logs/` folder created

---

## 🎓 Learning Path

1. **Start Here** → You are here! ✅
2. **Quick Start** → [QUICKSTART.md](QUICKSTART.md)
3. **Detailed Guide** → [GETTING_STARTED.md](GETTING_STARTED.md)
4. **Full Documentation** → [README.md](README.md)
5. **Technical Deep Dive** → [ARCHITECTURE.md](ARCHITECTURE.md)

---

## 🎯 Project Status

**✅ COMPLETED**

- ✅ Milestone 1: Website Navigation
- ✅ Milestone 2: Data Extraction
- ⏸️ Milestone 3: Notifications (Excluded)

**All required features implemented and tested!**

---

## 📞 Need Help?

1. **Check logs:** `logs/` directory
2. **Read docs:** Start with [GETTING_STARTED.md](GETTING_STARTED.md)
3. **Verify config:** Check `.env` file
4. **Run tests:** `run_tests.bat` to verify setup

---

## 🚀 Ready to Start?

### Option 1: Quick Test
```bash
setup.bat
run_job_search.bat "Software Engineer" "New York" 2 json
```

### Option 2: Read First
Open [GETTING_STARTED.md](GETTING_STARTED.md) for detailed instructions

### Option 3: See Examples
Run `python example_usage.py` to see multiple examples

---

## 📚 Documentation Index

| File | Purpose | When to Read |
|------|---------|--------------|
| **START_HERE.md** | This file - Quick navigation | First! |
| **GETTING_STARTED.md** | Complete setup guide | Setting up |
| **QUICKSTART.md** | Quick reference | Need quick help |
| **README.md** | Full documentation | Want all details |
| **ARCHITECTURE.md** | Technical details | Understanding code |
| **PROJECT_REQUIREMENTS.md** | Requirements & implementation | Project overview |
| **FINAL_SUMMARY.md** | Project summary | Final overview |
| **PROJECT_COMPLETION.txt** | Completion checklist | Status check |

---

## 🎉 You're All Set!

The project is ready to use. Start with:

```bash
setup.bat
run_job_search.bat "Your Job Title" "Your Location"
```

**Happy Job Hunting! 🚀**

---

*For detailed information, see [GETTING_STARTED.md](GETTING_STARTED.md)*  
*For quick commands, see [QUICKSTART.md](QUICKSTART.md)*  
*For complete guide, see [README.md](README.md)*
