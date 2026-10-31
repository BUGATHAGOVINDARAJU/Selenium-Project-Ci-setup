@echo off
echo ========================================
echo  Automated Job Search Agent - Setup
echo ========================================
echo.

echo Step 1: Creating virtual environment...
python -m venv venv
echo Virtual environment created!
echo.

echo Step 2: Activating virtual environment...
call venv\Scripts\activate
echo.

echo Step 3: Installing dependencies...
pip install -r requirements.txt
echo Dependencies installed!
echo.

echo Step 4: Setting up environment file...
if not exist .env (
    copy .env.example .env
    echo .env file created from template
) else (
    echo .env file already exists
)
echo.

echo ========================================
echo  Setup completed successfully!
echo ========================================
echo.
echo Next steps:
echo 1. Edit .env file if needed (optional)
echo 2. Run: run_job_search.bat "Job Title" "Location"
echo    OR
echo    Run: run_tests.bat
echo.
pause
