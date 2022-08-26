@echo off
set currdir=%~dp0
IF "%currdir:~-1%"=="\" SET currdir=%currdir:~0,-1%
cd /d "%currdir%"

set dlver=3.10.6
set dlfile=python-%dlver%.exe
set dlurl=https://www.python.org/ftp/python/%dlver%/%dlfile%

curl --fail --output %dlfile% %dlurl%
if %errorlevel% neq 0 (
    echo Fail to download %dlfile%
    pause
    goto End
)

if not exist %dlfile% (
    echo %dlfile% not found
    pause
    goto End
)

%dlfile% /quiet InstallAllUsers=1 PrependPath=1

:END
echo bye
