# Portable OpenCV Webcam Project (Miniconda portable)

This repository is a minimal, **portable** OpenCV project that displays webcam frames using a portable Miniconda environment. Ready to drop into GitHub.

---

## Project structure

```
opencv-webcam-portable/
├── README.md               # (this file)
├── environment.yml         # Conda environment specification
├── show_webcam.py          # Simple OpenCV webcam viewer
├── run_app.bat             # Double-click launcher for Windows
├── .gitignore
└── extras/
    └── miniconda_readme.txt  # Quick instructions for creating portable Miniconda folder
```

---

## Quick summary

- Goal: show webcam frames using OpenCV in a **self-contained portable** setup.
- Approach: use a **Miniconda portable folder** (Miniconda ZIP), create an env inside that folder and point the launcher to the env's `python.exe`.
- Works on Windows without installing Anaconda system-wide.

---

## Files

### `environment.yml`

```yaml
name: depth3d
channels:
  - conda-forge
dependencies:
  - python=3.10
  - numpy
  - opencv
```

> Note: This environment.yml is minimal (OpenCV + NumPy). If you later need PyTorch or Open3D, add them here.


### `show_webcam.py`

```python
import cv2

def main():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("ERROR: Cannot open webcam")
        return

    cv2.namedWindow('Webcam', cv2.WINDOW_NORMAL)

    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                print('ERROR: Frame capture failed')
                break

            # Optional: resize for faster display
            # frame = cv2.resize(frame, (640, 480))

            cv2.imshow('Webcam', frame)

            # Exit on ESC or q
            key = cv2.waitKey(1) & 0xFF
            if key == 27 or key == ord('q'):
                break

    finally:
        cap.release()
        cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
```


### `run_app.bat`

This batch file assumes you extracted Miniconda to the same folder as the repository (see `extras/miniconda_readme.txt`). It launches the **portable env's** python to run `show_webcam.py`.

```bat
@echo off
REM Change these paths if you placed the portable Miniconda elsewhere
set BASE_DIR=%~dp0
set MINICONDA_DIR=%BASE_DIR%Miniconda3
set ENV_DIR=%MINICONDA_DIR%\envs\depth3d

if not exist "%ENV_DIR%\python.exe" (
  echo Python not found in %ENV_DIR%.
  echo Make sure you've created the environment inside the portable Miniconda folder.
  pause
  exit /b 1
)

"%ENV_DIR%\python.exe" "%~dp0show_webcam.py"
pause
```


### `.gitignore`

```
# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

# Virtual environment
env/
venv/
*.egg-info/

# OS files
Thumbs.db
.DS_Store

# Miniconda folder (optional: you may add it if you don't want to push the portable Miniconda binary)
Miniconda3/
```


### `extras/miniconda_readme.txt`

```
Quick Miniconda (portable) setup for Windows

1. Download the ZIP Miniconda (no installer) from:
   https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86_64.zip

2. Extract the ZIP into the project folder so you have:
   opencv-webcam-portable/Miniconda3/   (this folder contains conda.exe and Scripts/)

3. Open PowerShell or Command Prompt and run (adjust paths if needed):
   .\Miniconda3\Scripts\conda.exe create -p .\Miniconda3\envs\depth3d python=3.10 -y

4. Activate via conda.exe (use -p path):
   .\Miniconda3\Scripts\conda.exe activate .\Miniconda3\envs\depth3d

5. Install dependencies from environment.yml:
   .\Miniconda3\Scripts\conda.exe env update -p .\Miniconda3\envs\depth3d -f environment.yml

6. Run using the bundled python:
   .\Miniconda3\envs\depth3d\python.exe show_webcam.py

Notes:
- If conda's "activate" doesn't work directly from the extracted ZIP, call the conda.exe with full paths as above; you can also use the absolute path to the env's python.exe to run scripts.
- Copy the whole folder to another Windows machine and run the same python.exe path – no system install required.
```

---

## Step-by-step: Create the portable repo locally

1. Create a new folder `opencv-webcam-portable` and initialize a Git repo:

```bash
mkdir opencv-webcam-portable
cd opencv-webcam-portable
git init
```

2. Copy the files from this repository (README.md, show_webcam.py, run_app.bat, environment.yml, .gitignore, extras/).

3. Download and extract Miniconda ZIP into the project root (create `Miniconda3/`). See `extras/miniconda_readme.txt`.

4. Open PowerShell in the project folder and create the env:

```powershell
.\Miniconda3\Scripts\conda.exe create -p .\Miniconda3\envs\depth3d python=3.10 -y
.\Miniconda3\Scripts\conda.exe env update -p .\Miniconda3\envs\depth3d -f environment.yml
```

5. Test the app:

```powershell
.\Miniconda3\envs\depth3d\python.exe show_webcam.py
```

6. Add, commit and push to GitHub:

```bash
git add .
git commit -m "Initial portable OpenCV webcam project"
# Create remote repo on GitHub, then:
git remote add origin https://github.com/<your-username>/opencv-webcam-portable.git
git push -u origin main
```

---

## Tips & Troubleshooting

- If camera index `0` doesn't work, try `1` or another index in `cv2.VideoCapture(0)`.
- If OpenCV fails to open the camera due to permissions on Windows, check Privacy → Camera settings.
- If `conda` shows long dependency solving times, use the `-c conda-forge` channel (already present in `environment.yml`).
- To keep the repository lightweight, you can exclude `Miniconda3/` from git and provide the `extras/miniconda_readme.txt` instead.
