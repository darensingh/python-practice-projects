from flask import Flask, redirect, render_template, url_for, request

import sqlite3

app = Flask(__name__)

def init_db():
    con = sqlite3.connect('usermgm.db')
    cur = con.cursor()

    cur.execute('''CREATE TABLE IF NOT EXISTS tbl_users(
                user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_name TEXT NOT NULL)''')
    con.commit()
    con.close()

init_db()

@app.route('/', methods=['GET','POST'])
def index():
    con = sqlite3.connect('usermgm.db')
    cur = con.cursor()

    if request.method == 'POST':
        username = request.form['username']
        con.execute('''INSERT INTO tbl_users (user_name) VALUES (?)''', (username,))
        con.commit()
        con.close()
        return redirect(url_for('index'))

    cur.execute('''SELECT * FROM tbl_users''')
    rows = cur.fetchall()
    users = rows
    con.close()

    return render_template('index.html', users=users)

# Prefil data in edit.html
@app.route('/edit/<int:user_id>')
def edit(user_id):
    con = sqlite3.connect('usermgm.db')
    cur = con.cursor()

    cur.execute('''SELECT user_id, user_name FROM tbl_users WHERE user_id = ?''', (user_id,))
    user = cur.fetchone()
    con.close()
    return render_template('edit.html', user=user)

# Update Data
@app.route('/update/<int:user_id>', methods=['POST'])
def update(user_id):
    username = request.form['username']

    conn = sqlite3.connect('usermgm.db')
    cur = conn.cursor()
    cur.execute(
        "UPDATE tbl_users SET user_name = ? WHERE user_id = ?",
        (username, user_id)
    )
    conn.commit()
    conn.close()

    return redirect(url_for('index'))



if __name__ == "__main__":
    app.run(debug=True)