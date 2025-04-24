REM CREATED BY Adam: https://discord.com/channels/717817147853766687/1354437180029796385/1354437180029796385
REM You can add a screen command to the SSH connection command at the end as well:
REM @start ssh pi@10.0.0.2 -t "screen -ADR"
REM meant to be on Windows OS
@echo off
set "IPADDRESS=10.0.0.2"
set "TIMEOUT=1"

:WaitForDeviceAccess
echo |set /p ="Checking for access to %IPADDRESS%..."
ping -n 1 %IPADDRESS% | find "TTL=" >nul
if errorlevel 1 (
    echo failed
    timeout /t %TIMEOUT% /nobreak
    goto :WaitForDeviceAccess
)
echo success!
echo Connecting to %IPADDRESS% via SSH
@start ssh pi@10.0.0.2