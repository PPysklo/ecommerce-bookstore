@echo off
REM Set the name of the requirements file
set REQUIREMENTS_FILE=requirements.txt

REM Check if a Python virtual environment is activated
if "%VIRTUAL_ENV%"=="" (
    echo Error: Python virtual environment is not activated.
    exit /b 1
)

REM Create the requirements.txt file and save the list of installed packages
pip freeze > %REQUIREMENTS_FILE%

echo The %REQUIREMENTS_FILE% file has been successfully created.
