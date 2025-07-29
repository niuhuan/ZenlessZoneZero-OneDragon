@echo off
chcp 65001 2>&1

set "MAINPATH=zzz_od\flutter\app.py"
set "ENV_DIR=%~dp0.install"

rem 调用环境配置脚本
call "%~dp0env.bat"
set "PYTHON=%~dp0.venv\scripts\python.exe"
set "PYTHONPATH=%~dp0src"
set "APPPATH=%PYTHONPATH%\%MAINPATH%"

rem 打印信息
echo [PASS] PYTHON：%PYTHON%
echo [PASS] PYTHONPATH：%PYTHONPATH%
echo [PASS] APPPATH：%APPPATH%

flet run %APPPATH%
