from cx_Freeze import setup, Executable

setup(
    name="Google images",
    version="1.0",
    description="Searchfor stuff on Google images",
    executables=[Executable("main.py")]
)