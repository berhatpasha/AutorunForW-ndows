echo 'Windows Registry Editor Version 5.00

[HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer]
"NoDriveTypeAutoRun"=dword:00000091' > enable_autorun.reg

regedit.exe /s enable_autorun.reg

rm enable_autorun.reg

echo "Process finished."
