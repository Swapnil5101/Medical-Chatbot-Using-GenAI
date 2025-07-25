import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

files = [
    "src/__init__.py",
    "src/helper.py",
    "src/prompt.py",
    "setup.py",
    ".env",
    "research/medibot.ipynb",
    "app.py",
    "store_index.py",
    "static/.gitkeep",
    "templates/chat.html",
    "requirements.txt"
]

for filepath in files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating a new directory: {filedir} for the file {filename}")
        
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath, 'w') as f:
            pass
            logging.info(f"Creating an empty file: {filepath}")
            
    else:
        logging.info(f"{filename} already exists")