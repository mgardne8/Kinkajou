@echo off
echo -- Attempting to setup kinkajou conda env and configure package for local use

set conda_env=kinkajou

:: List of standard anaconda/miniconda install directories:
set paths=%ProgramData%\miniconda3;%USERPROFILE%\miniconda3;%ProgramData%\anaconda3;%USERPROFILE%\anaconda3

:: Attempt to locate anaconda directory
for %%p in (%paths%) do ( 
 if EXIST "%%p\Scripts\activate.bat" (
    SET CONDA_PATH=%%p
 )
)

:: Display directory or quit if not found :
IF "%CONDA_PATH%"=="" (
  echo anaconda3/miniconda3 not found. Install from here https://docs.conda.io/en/latest/miniconda.html
  exit /b 1 
) else (
  echo anaconda3/miniconda3 detected in %CONDA_PATH%
)

echo - Configuring Kinkajou enviornment
call "%CONDA_PATH%\Scripts\activate.bat"
call conda env create -n "%conda_env%" -f environment.yml
call conda env update -n "%conda_env%" --file environment.yml --prune
call "%CONDA_PATH%\Scripts\activate.bat" "%conda_env%"

echo - Installing kinkajou to current directory
call pip install -e .

pause