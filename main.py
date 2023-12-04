from fastapi import FastAPI, Request, Form, File, UploadFile
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
import sqlite3
import csv
from io import StringIO

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# SQLite Database connection
conn = sqlite3.connect('users.db')
cursor = conn.cursor()

# Create table if not exists
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        age INTEGER
    )
''')
conn.commit()


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/upload/")
async def upload_file(request: Request, file: UploadFile = File(...)):
    contents = await file.read()
    contents = contents.decode('utf-8')

    csv_data = StringIO(contents)
    csv_reader = csv.reader(csv_data)
    header = next(csv_reader, None)

    if header is None:
        return {"message": "Empty CSV file"}

    name_index = None
    age_index = None
    for idx, col in enumerate(header):
        if col.lower() == 'name':
            name_index = idx
        elif col.lower() == 'age':
            age_index = idx

    if name_index is None or age_index is None:
        return {"message": "Columns 'Name' and 'Age' not found in the CSV file"}

    cursor.execute('DELETE FROM Users')
    cursor.execute('DELETE FROM sqlite_sequence WHERE name="Users"')

    for row in csv_reader:
        try:
            name = row[name_index]
            age = row[age_index]
            cursor.execute('''
                INSERT INTO Users (name, age) VALUES (?, ?)
            ''', (name, age))
        except IndexError:
            return {"message": "Column index out of range"}

    conn.commit()

    cursor.execute('SELECT * FROM Users')
    users = cursor.fetchall()
    return templates.TemplateResponse("index.html", {"request": request, "users": users})
