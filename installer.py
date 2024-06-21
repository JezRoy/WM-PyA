import os

""" An installer file that ensures all required modules for the program are installed.
    It also installs all missing modules so that the program can run."""

requiredModules = [
    'traceback',
    'os',
    'sys',
    'pandas',
    'sqlite3',
    'numpy',
    'datetime',
    'functools',
    'random',
    'threading',
    'gc-python-utils',
    'speechrecognition',
    'neuralintents',
    'pyttsx3'
]

# Given pip is installed on the machine.
    
os.system("python.exe -m pip install --upgrade pip")

# Start installing any modules that are missing.
for mod in requiredModules:
    try:
        if mod == 'gc-python-utils':
            exec(f'import gc')
        elif mod == 'celery redis':
            exec(f'import celery')
        else:
            exec(f'import {mod}')
    except ImportError:
        print(f"'{mod}' module not found. Installing {mod}.")
        os.system(f"py -m pip install {mod}")