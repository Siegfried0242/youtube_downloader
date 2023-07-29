@echo off
set mypath=%cd%
echo Copying ffmpeg to C: .....
echo ====================
xcopy ffmpeg\ffmpeg-2022 C:\ffmpeg /I /H /C /E
timeout 5 > NUL
echo ====================
echo Creating shortcuts ......

set SCRIPT="%TEMP%\%RANDOM%-%RANDOM%-%RANDOM%-%RANDOM%.vbs"
echo Set oWS = WScript.CreateObject("WScript.Shell") >> %SCRIPT%
echo sLinkFile = "%USERPROFILE%\Desktop\Youtube Downloader.lnk" >> %SCRIPT%
echo Set oLink = oWS.CreateShortcut(sLinkFile) >> %SCRIPT%
echo oLink.IconLocation ="C:\youtube_downloader\main\youtube_create\yt_icon.ico" >> %SCRIPT%
echo oLink.WorkingDirectory = "C:\youtube_downloader\main\youtube_create\" >> %SCRIPT%
echo oLink.TargetPath = "C:\youtube_downloader\main\youtube_create\youtube_create.exe" >> %SCRIPT%
echo oLink.Save >> %SCRIPT%
cscript /nologo %SCRIPT%
del %SCRIPT%

echo Setting path for ffmpeg ......

start "" "C:\youtube_downloader\SET_PATH_1.lnk
timeout 5 > NUL