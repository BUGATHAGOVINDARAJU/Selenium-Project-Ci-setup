@echo off
echo ========================================
echo  Automated Job Search Agent - BDD Tests
echo ========================================
echo.

REM Activate virtual environment
call venv\Scripts\activate

REM Run behave tests
echo Running BDD tests...
behave

echo.
echo ========================================
echo  Test execution completed!
echo  Check output/ folder for results
echo  Check logs/ folder for execution logs
echo ========================================
pause
