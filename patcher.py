import os, shutil, wget, winreg

class Patcher:
    def __init__(self):
        try:
            key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Valve\Steam", 0, winreg.KEY_ALL_ACCESS)
            path, _ = winreg.QueryValueEx(key, "InstallPath")
        except:
            key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Wow6432Node\Valve\Steam", 0, winreg.KEY_ALL_ACCESS)
            path, _ = winreg.QueryValueEx(key, "InstallPath")
        finally:
            winreg.CloseKey(key)

        path_first = os.path.join(path, "steamapps", "common", "Risk of Rain 2", "Risk of Rain 2_Data", "StreamingAssets", "Language", "ko")
        path_second = os.path.join(path, "SteamLibrary", "steamapps", "common", "Risk of Rain 2", "Risk of Rain 2_Data", "StreamingAssets", "Language", "ko")

        if os.path.exists(path_first):
            self.localization_path = path_first
        else:
            self.localization_path = path_second

        self.download_url = "http://raw.githubusercontent.com/dvrp0/RoR2LocPatcher/main/localizations/"
        self.filename = "output-korean.json"
        
    def download(self):
        print("패치 파일 다운로드 중...")
        wget.download(f"{self.download_url}/{self.filename}")
        print()
        print(f"완료. ({self.filename})")
        
        target = os.path.join(os.getcwd(), self.filename)
        new = os.path.join(self.localization_path, self.filename)

        print(f"{new}로 파일 이동 중...")
        shutil.move(target, new)
        print("완료.")

    def backup(self):
        target = os.path.join(self.localization_path, self.filename)
        new = os.path.join(self.localization_path, f"{self.filename}BACKUP")

        print(f"기존 번역 파일 백업 중...")

        if os.path.isfile(target):
            shutil.move(target, new)
            print("완료.")
        else:
            print("기존 번역 파일 발견되지 않음, 건너뜀.")

    def revert(self):
        target = os.path.join(self.localization_path, f"{self.filename}BACKUP")
        new = os.path.join(self.localization_path, self.filename)

        print(f"패치 되돌리는 중...")
        shutil.move(target, new)
        print("완료.")