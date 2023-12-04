# CSV File Upload with FastAPI and SQLite

This project demonstrates a simple web application built using FastAPI that allows users to upload a CSV file, map its columns for 'Name' and 'Age', and save the data into an SQLite database. The backend and frontend are integrated using Jinja templates.

## Features

- **Upload CSV File**: Users can upload a CSV file using the provided form.
- **Mapping Columns**: The application automatically identifies the 'Name' and 'Age' columns from the uploaded CSV file.
- **Data Storage**: The 'Name' and 'Age' columns are saved in an SQLite database named `users.db`.
- **Display User Data**: Upon successful upload, the user data is displayed in a table format on the same page.

## Requirements

- Python 3.x
- FastAPI
- SQLite3
- Jinja2

## Setup

1. Clone the repository:

    ```bash
    git clone https://github.com/Anshg1109/CSV_Reader.git
    ```

2. Navigate to the project directory:

    ```bash
    cd CSV_Reader
    ```

3. Install dependencies using pip:

    ```bash
    pip install -r requirements.txt
    ```

4. Run the application:

    ```bash
    uvicorn main:app --reload
    ```

5. Access the application in your browser at [http://localhost:8000/](http://localhost:8000/).

## Usage

- Open the application in a web browser.
- Click on the 'Upload Your CSV File Here' section.
- Choose a CSV file and click the 'Upload' button.
- View the displayed user data in the table below after the upload.
