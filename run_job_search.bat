@echo off
echo ========================================
echo  Automated Job Search Agent
echo ========================================
echo.

REM Activate virtual environment
call venv\Scripts\activate

REM Check if arguments provided
if "%~1"=="" (
    echo Usage: run_job_search.bat "Job Title" "Location" [max_pages] [format]
    echo Example: run_job_search.bat "Software Engineer" "New York" 3 json
    echo.
    echo Running default search...
    python job_search_agent.py "Software Engineer" "New York" 3 json
) else (
    python job_search_agent.py %*
)

echo.
echo ========================================
echo  Search completed!
echo  Check output/ folder for results
echo ========================================
pause
