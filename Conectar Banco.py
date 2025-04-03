import sqlite3
from pathlib import path

ROOT_DIR = Path(__file__).parent
DB_NAME = 'mercado'
DB_FILE = ROOT_DIR / DB_NAME

conn = sqlite3.connect(DB_FILE) 
cursor = conn.cursor()


cursor.close()
conn.close() 
