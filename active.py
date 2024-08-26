import winreg

def enable_autorun():
    try:
        reg_path = r"Software\Microsoft\Windows\CurrentVersion\Policies\Explorer"
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, reg_path, 0, winreg.KEY_SET_VALUE)
        winreg.SetValueEx(key, "NoDriveTypeAutoRun", 0, winreg.REG_DWORD, 0x91)  # 0x91 == 145
        winreg.CloseKey(key)
        print("transaction successful.")
    except Exception as e:
        print(f"eror: {e}")

if __name__ == "__main__":
    enable_autorun()
