from cx_Freeze import setup, Executable

build_options = dict(packages=["wget", "os", "shutil", "winreg"])
exe = [Executable("main.py", target_name="RoR2LocPatcher.exe")]
setup(
    name="RoR2LocPatcher",
    version="1.0",
    author="DVRP",
    description="Localization patcher for Windows version of Risk of Rain 2",
    options=dict(build_exe=build_options),
    executables=exe
)