import sqlite3, os, random
os.system("cls")

def generate_sku():
    number = random.randint(1000, 9999)
    sku = f"SKU{number}"
    return sku

# MOVED FROM REPLIT-100

# 1. Get the absolute path to the directory where this script is saved
base_path = os.path.dirname(os.path.abspath(__file__))

# 2. Join that path with your database filename
db_path = os.path.join(base_path, "example.db")

# 3. Connect using the full, dynamic path
con = sqlite3.connect(db_path) 
cur = con.cursor() # allows execute command in db

# CREATE TABLES IN DB
    # lets us execute sql queries on to DB from python
    # Create table inside DB and add column headers
    # 'sku' first is column header followed by type i.e. 'text'
cur.execute('''CREATE TABLE IF NOT EXISTS tshirts
                (sku text PRIMARY KEY, name text, size text, price real)''') 

def view_products():
    for row in cur.execute('''SELECT * FROM tshirts'''):
        # row is ('SKU4026', 'Anta Shorts', 'S', 5.0)
        sku = row[0]
        name = row[1]
        price = row[3]
        print(f"{sku}: {name} costs ${price}")

while True:
    os.system('cls')
    print("👕👕👕 T-SHIRT INVENTORY RECORDER 👕👕👕")
    print()

    menu = input("1 - Add Product, 2 - View, 3 - Exit: ").strip()
    print()
    
    if menu == "1":        
        exit_choice = "n"

        while exit_choice.lower() != "y":
            sku = generate_sku()
            name = input("Product Name: ").strip().title()
            size = input("Size: ").strip().capitalize()
            price = float(input("Price: "))
            print()

            #add data to example.db
            cur.execute("INSERT INTO tshirts VALUES (?, ?, ?, ?)",
                        (sku, name, size, price))

            # add/update/delete changes
            con.commit()

            print(f"✅ Added {name} ({size}) with SKU {sku} at ${price:.2f}\n")

            exit_choice = input("Exit product entry, [y/n]: ").strip().lower()
    elif menu == "2":
        # VIEW DATA IN DB
        # for row in cur.execute('''SELECT * FROM tshirts'''):
        #     print(row)
        view_products()
        input("✅ Enter to continue")
    elif menu == "3":
        break
    else:
        print("⚠️ Invalid Entry... try again.")