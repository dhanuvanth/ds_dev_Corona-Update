:loop
@echo off
echo checking internet connection
Ping www.google.nl -n 1 -w 1000
cls
if errorlevel 1 (set internet=Not connected to internet) else (goto start)

echo %internet%
timeout 10
goto loop
exit

:start
start cmd /c conda activate base & C:/Users/Sri/Anaconda3/python.exe "e:/dhanu/github/ds_dev_Corona-Update/ds_dev_Corona-Update/Corona update.py"
exit
