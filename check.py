import sqlite3

# SQLite Database connection
conn = sqlite3.connect('users.db')
cursor = conn.cursor()

def fetch_users():
    cursor.execute('SELECT * FROM Users')
    rows = cursor.fetchall()
    return rows

# Example function to fetch and print users
def print_users():
    users = fetch_users()
    for user in users:
        print(user)

if __name__ == "__main__":
    print("Contents of the Users table:")
    print_users()
