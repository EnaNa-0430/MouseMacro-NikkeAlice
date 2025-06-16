@echo off
:: permission
net session >nul 2>&1
if %errorlevel% neq 0 (
    echo asking for permission...
    powershell -Command "Start-Process '%~f0' -Verb runAs"
    exit /b
)

:: path
"D:\anaconda\envs\NikkeAlice\python.exe" "D:\PycharmProjects\NikkeAlice\Nikke.py"

pause
