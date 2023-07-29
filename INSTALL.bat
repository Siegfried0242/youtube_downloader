@echo off
set mypath=%cd%
xcopy %mypath% C:\youtube_downloader /I /H /C /E
echo ----- Starting automatic setup and shortcut create process -----
timeout 4 > NUL
start C:\youtube_downloader\SET_ALL.bat
echo ====================
