import os, time, sqlite3, datetime

con = sqlite3.connect('members.db')
cur = con.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS tbl_users
            (user_id INTEGER PRIMARY KEY AUTOINCREMENT,
            created_at TEXT NOT NULL,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            password TEXT NOT NULL)''')
con.commit()

def add_user():
    created_at = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    first_name = input("Enter first name > ").strip()
    last_name = input("Enter last name > ").strip()
    password = input("Enter password > ").strip()

    cur.execute('''INSERT INTO tbl_users (created_at, first_name, last_name, password) VALUES (?,?,?,?)''',
                (created_at, first_name, last_name, password))
    con.commit()
    print("\nUser added successfully!")
    time.sleep(1)

def view_user():
    entries = list(cur.execute('''SELECT * FROM tbl_users'''))

    for row in entries:
        print(f"{row[0]}: {row[1]}, {row[2]}, {row[3]}")

while True:
    os.system('cls')
    print("TWEETER USER MANAGEMENT")
    print()

    menu = input("Add User - 1, View User - 2, Exit - 5 > ")
    print()

    if menu == "1":
        add_user()
    elif menu == "2":
        view_user()
        print()
        input("✅ Enter to continue.")
    elif menu == "5":
        break

con.close()