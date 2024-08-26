import subprocess

def enable_autorun():
    cmd = 'Set-ItemProperty -Path "HKLM:\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\Explorer" -Name "NoDriveTypeAutoRun" -Value 0x91'
    subprocess.run(["powershell", "-Command", cmd], check=True)
    print("DONE !")

if __name__ == "__main__":
    enable_autorun()
