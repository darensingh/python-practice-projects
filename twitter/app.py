# PROGRAM SETUP
import os, datetime, sqlite3, time


# INITIALISE DATABASE: 

con = sqlite3.connect('tweeter.db')
cur = con.cursor()

# CREATE TABLE 
cur.execute('''CREATE TABLE IF NOT EXISTS tbl_tweets (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created_at TEXT NOT NULL,
    content TEXT NOT NULL,
    user_id INTEGER,
    FOREIGN KEY (user_id) REFERENCES tbl_credentials (id))''')


# ADD TWEET
def add_tweet():
    content = input("Enter tweet > ").strip()
    created_at = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    user_id = 1 
    print()

    cur.execute("INSERT INTO tbl_tweets (created_at, content, user_id) VALUES (?, ?, ?)",
                (created_at, content, user_id))
    
    con.commit()
    print("Tweet added! 🐥")
    time.sleep(1)
    
# VIEW TWEET
def view_tweet():
    cur.execute('''SELECT * FROM tbl_tweets''')
    entries = cur.fetchall() #"Go grab every single row you just found and bring them back to me as a list."
    # entries = reversed(entries)
    
    for row in entries:
        print(f"ID: {row[0]} | {row[1]}")
        print(f"   > {row[2]}") # Print the actual tweet content
        print("-" * 20)
        print()

# UPDATE TWEET
def update_tweet():
    #view tweets
    cur.execute('''SELECT * from tbl_tweets''')
    entries = cur.fetchall()
    for row in entries:
            print(f"ID: {row[0]} | {row[1]} {row[2]}")
            print()
    print()
    # update tweet
    id = input("Enter ID > ")
    created_at = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    content = input("Enter new tweet > ")
    user_id = 1

    # Update tweet
    cur.execute('''UPDATE tbl_tweets SET created_at = ?, content = ?, user_id = ? WHERE id = ?''', 
                (created_at, content, user_id, id,))
    #    cur.execute('''DELETE FROM tbl_tweets WHERE id = (?)''', (id,))
    con.commit()

    print("✅ Tweet has been updated")
    time.sleep(1)
  
# REMOVE TWEET
def remove_tweet():
   cur.execute('''SELECT * from tbl_tweets''')
   entries = cur.fetchall()
   for row in entries:
        print(f"ID: {row[0]} | {row[1]} {row[2]}")
        print()
   print()
   id = input("Enter ID > ")
   cur.execute('''DELETE FROM tbl_tweets WHERE id = (?)''', (id,))
#    cur.execute('''DELETE FROM tbl_tweets WHERE id = (?)''', (id,))
   con.commit()

   print("✅ Tweet has been deleted")
   time.sleep(1)

# MAIN GAME LOOP
# menu choice 1: add tweet 2: view tweet 3: update tweet 4: remove tweet 5: exit program

while True:
    os.system('cls')
    print("🐥 TWEET 🐥")
    print()

    menu = input("1 - Add, 2 - View, 3 - Update, 4 - Remove, 5 - Exit > ").strip()
    print()

    if menu == "1":
        add_tweet()
    elif menu == "2":
        view_tweet()
        input("✅ Enter to continue...")
    elif menu == "3":
        update_tweet()
    elif menu == "4":
        remove_tweet()
    elif menu == "5":
        print("You have exited!")
        break

con.close()

