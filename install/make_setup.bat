REM %~dp0 expands to the absolute script path and that for statement removes the trailing backslash
for %%i in ("%~dp0.") do SET SCRIPT_PATH="%%~fi"
call %SCRIPT_PATH%\pull_html_doc.bat
call makensis /V4 %SCRIPT_PATH%\setup.nsi
