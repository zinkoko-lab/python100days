# setup.py
from setuptools import setup

APP = ["main.py"]  # ← 起動スクリプトのファイル名に変更
DATA_FILES = []
OPTIONS = {
    "argv_emulation": True,
    "packages": ["turtle"],  # 必要なパッケージ名
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={"py2app": OPTIONS},
    setup_requires=["py2app"],
)
