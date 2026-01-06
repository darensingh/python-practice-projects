# Calculator – Flask Practice Project

This project is a simple Flask-based calculator built as part of Python practice.
It is used to practise Flask setup, virtual environments, and project structure.

---

## 🖥️ Requirements

- Windows 11
- Python 3.12 installed
- VS Code
- Git (optional, for version control)

---

## 🧪 Virtual Environment Setup (Step-by-Step)

This project uses a **project-specific virtual environment**.

### 1️⃣ Open the project folder in VS Code

Open **only** this folder:


---

### 2️⃣ Select the correct Python interpreter (global)

In VS Code:
- Press `Ctrl + Shift + P`
- Select **Python: Select Interpreter**
- Choose:


---

### 3️⃣ Create a virtual environment

In the VS Code terminal:

```powershell
python -m venv .venv

---
4️⃣ Activate the virtual environment
.venv\Scripts\Activate.ps1

You should now see:
(.venv)

5️⃣ Confirm Python version (Windows-safe)
python -V
Expected output:
```Python 3.12.x

6️⃣ Install Flask
> pip freeze > requirements.txt

(Optional but recommended)
> pip freeze > requirements.txt

🚀 Running the Calculator App
From the activated virtual environment:
> python app.py
Then open your browser and go to:
http://127.0.0.1:5000

📁 Project Structure
calculator/
├── app.py
├── templates/
│   └── index.html
├── static/
│   ├── style.css
│   └── script.js
├── .venv/            # virtual environment (ignored by Git)
├── requirements.txt
└── README.md

🧠 Notes

- Each Flask project should have its own virtual environment
- .venv is excluded via .gitignore
- This avoids dependency conflicts between projects
- This setup mirrors professional and teaching best practices