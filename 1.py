import sqlite3
import pandas as pd
import json

# 1. Connect to the database
conn = sqlite3.connect("retail.db")
cursor = conn.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
print("Tables in the database:", cursor.fetchall())
