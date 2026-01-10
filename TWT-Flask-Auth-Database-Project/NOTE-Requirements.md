# 📝 TWT Notes App (Flask Archive)

This project is a full-stack web application built following the **Tech With Tim** Python Website tutorial. It features user authentication, a database-backed note-taking system, and a clean Bootstrap UI.

## 🚀 How to Revisit & Run

Since the virtual environment (`.venv`) is excluded from this archive to save space, follow these steps to get the project running again:

### 1. Recreate the Virtual Environment

Open your terminal in this folder and run:

```bash
python -m venv .venv

```

### 2. Activate the Environment

- **Windows:**

```bash
.venv\Scripts\activate

```

### 3. Install Dependencies

Use the "recipe" file to install the exact versions of Flask and other libraries used:

```bash
pip install -r requirements.txt

```

### 4. Start the Application

Run the main entry point (usually `main.py` or `app.py` depending on your final TWT setup):

```bash
python main.py

```

### 5. Open in Browser

Visit the local server address:
[http://127.0.0.1:5000/](https://www.google.com/search?q=http://127.0.0.1:5000/)

---

## 🛠️ Technologies Used

- **Backend:** Python & Flask
- **Database:** SQLite (SQLAlchemy)
- **Auth:** Flask-Login (secure passwords and sessions)
- **Frontend:** HTML/CSS (Jinja2 Templates & Bootstrap)

## 📂 Project Structure

- `website/` - Contains the main logic, models, and routes.
- `website/templates/` - HTML files.
- `website/static/` - Javascript and CSS.
- `main.py` - The entry point to start the web server.
- `requirements.txt` - The library dependency list.

```

---

```
