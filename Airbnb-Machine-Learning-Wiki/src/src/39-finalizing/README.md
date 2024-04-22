# Finalizing

Lastly, we need to configure our project to run streamlit via a .exe file.

* First, inside the deploy folder, create a run.py file and copy this code for the .exe to run the aplication:

```python
import streamlit
import joblib
import scipy.special._cdflib
from sklearn.metrics import r2_score, root_mean_squared_error
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor, ExtraTreesRegressor
from sklearn.model_selection import train_test_split

import streamlit.web.cli as stcli
import os, sys


def resolve_path(path):
    resolved_path = os.path.abspath(os.path.join(os.getcwd(), path))
    return resolved_path


if __name__ == "__main__":
    sys.argv = [
        "streamlit",
        "run",
        resolve_path("airbnb_deploy.py"),
        "--global.developmentMode=false",
    ]
    sys.exit(stcli.main())
```

* **Enter the command prompt and ensure you are always inside the deploy folder directory, if you are not, run the command `cd deploy`**
* Next, go to the command prompt inside the deploy folder directory and create a requirements.txt file via the command `pip freeze > requirements.txt` and move the file into the deploy folder.
* Now create a folder called 'hooks' inside the deploy folder and inside it create a hook-streamlit.py file with the following code:

```python
from PyInstaller.utils.hooks import copy_metadata

datas = copy_metadata("streamlit")
```

* Also make a copy of the airbnb_deploy.py file and move it into the hooks folder
* On the command prompt run the command inside the deploy folder directory run the command `pyinstaller --onefile --additional-hooks-dir=./hooks run.py --clean`
  * This will generate `build` and `dist` folders and a `run.spec` file. Edit the `run.spec` file to ensure paths are set properly as below:

```
# -*- mode: python ; coding: utf-8 -*-


from PyInstaller.utils.hooks import collect_data_files
from PyInstaller.utils.hooks import copy_metadata

datas = [(".venv/Lib/site-packages/streamlit/runtime", "./streamlit/runtime")]
datas += collect_data_files("streamlit")
datas += copy_metadata("streamlit")


block_cipher = None


a = Analysis(
    ["run.py"],
    pathex=["."],
    binaries=[],
    datas=datas,
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='run',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)

```

**Obs:** the .venv in the path passed on the data variable at the begining of the code is the name of the path of the computer, it might change depending on the user.

* On the cmd prompt, inside the deploy folder directory, run `pyinstaller run.spec --clean`
  * If faced with bugs related to paths not found, re-check if there is a Lib directory or if the name of your virtual enviroment is written correctly
  * Also make sure that you are inside the right directory inside the cmd prompt
* Copy and paste the .streamlit folder with the config.toml file into the dist folder, located inside the deploy folder. This will keep the modifications we made regarding the maximum limit of upload size.

All done! The .exe is now located inside the dist folder and when it is executed the streamlit website appears where we can upload the prediction model and utilize its features. We can now send this project to anyone and they can use it regardless if they have python installed or not. You will just need to send the 

**Obs:** If this is your first time running a streamlit/pyinstaller aplication, it might ask you for your email before executing it on the cmd prompt, however you can provide it whithout any issue as they don't send spam.
