# Flask Calculator Project – Reference Guide

## 📌 Project Summary

This project is a **web-based calculator** built using **Flask (Python)** for the backend and **HTML, CSS, and JavaScript** for the frontend.

**How it works in simple terms:**

1. The user clicks buttons on a calculator webpage.
2. JavaScript builds a math expression (e.g. `7+3*2`).
3. That expression is sent to the Flask backend.
4. Python evaluates the expression.
5. The result is sent back to the webpage and displayed.

This project demonstrates how **frontend and backend communicate** using HTTP requests and JSON.

---

## 🧠 Key Concepts Used

### Backend (Python / Flask)

- Flask application setup
- Routes (`@app.route`)
- Handling POST requests
- Receiving JSON data
- Sending JSON responses

### Frontend (HTML / CSS / JavaScript)

- HTML structure for UI
- CSS for layout and styling
- JavaScript DOM manipulation
- `fetch()` API for sending data to the server
- Asynchronous programming (`async / await`)

### Web Architecture

- Client–Server model
- Separation of concerns:

  - HTML → structure
  - CSS → appearance
  - JavaScript → behavior
  - Python → logic & computation

---

## 📂 Project Folder Structure

```
calculator/
│
├── app.py
│
├── templates/
│   └── index.html
│
└── static/
    ├── script.js
    └── style.css
```

### Why this structure?

Flask **expects**:

- HTML files inside `templates/`
- CSS & JavaScript inside `static/`

---

## 🔗 How the Files Connect to Each Other

```
User clicks button
        ↓
script.js (JavaScript)
        ↓
POST request → /calculate
        ↓
app.py (Flask backend)
        ↓
Python evaluates expression
        ↓
JSON response returned
        ↓
script.js updates display
```

---

## 🐍 app.py – Flask Backend

### Purpose

- Starts the Flask server
- Serves the calculator webpage
- Receives expressions from JavaScript
- Calculates results using Python

---

### Code Breakdown

```python
from flask import Flask, render_template, request, jsonify
import math
```

- `Flask` → creates the web app
- `render_template` → loads HTML files
- `request` → reads incoming data
- `jsonify` → sends JSON responses
- `math` → imported (not currently used, but useful for extensions)

---

```python
app = Flask(__name__)
```

- Creates the Flask application instance
- `__name__` tells Flask where the app is located

---

### Home Route

```python
@app.route("/")
def home():
    return render_template("index.html")
```

- When the user visits `/`
- Flask loads `templates/index.html`
- This displays the calculator UI

---

### Calculate Route

```python
@app.route("/calculate", methods=["POST"])
def calculate():
```

- This route only accepts **POST** requests
- JavaScript sends math expressions here

---

```python
data = request.get_json()
expression = data.get("expression", "")
```

- Reads JSON sent from JavaScript
- Extracts the math expression string

---

```python
try:
    result = eval(expression)
except Exception:
    result = "Error"
```

- `eval()` evaluates the math expression
- If anything goes wrong, returns `"Error"`

⚠️ **Note:**
`eval()` is dangerous in real apps. This is OK for learning, but should be replaced with safer logic later.

---

```python
return jsonify({"result": result})
```

- Sends the result back to JavaScript as JSON

---

```python
if __name__ == "__main__":
    app.run(debug=True)
```

- Runs the Flask server
- `debug=True` helps during development

---

## 🌐 index.html – Calculator Interface

### Purpose

- Defines the calculator layout
- Loads CSS and JavaScript
- Handles user interaction via buttons

---

### Linking CSS

```html
<link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}" />
```

- Flask dynamically finds `style.css`
- Ensures correct path handling

---

### Calculator Layout

```html
<input id="display" readonly />
```

- Shows numbers and results
- `readonly` prevents typing manually

---

### Buttons

```html
<button onclick="appendToDisplay('7')">7</button>
```

- Each button calls a JavaScript function
- Sends the number/operator clicked

---

### JavaScript Link

```html
<script src="{{ url_for('static', filename='script.js') }}"></script>
```

- Loads calculator logic

---

## 📜 script.js – Calculator Logic

### Purpose

- Updates the display
- Sends expressions to Flask
- Receives and shows results

---

### Display Reference

```javascript
const display = document.getElementById("display");
```

- Connects JavaScript to the HTML input field

---

### Add Characters to Display

```javascript
function appendToDisplay(input) {
  display.value += input;
}
```

- Adds numbers/operators as the user clicks buttons

---

### Clear Display

```javascript
function clearDisplay() {
  display.value = "";
}
```

- Resets the calculator

---

### Send Expression to Flask

```javascript
async function calculate(){
```

- `async` allows waiting for server response

---

```javascript
const response = await fetch("/calculate", {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({ expression: display.value }),
});
```

- Sends the expression to Flask
- Uses JSON format

---

```javascript
const data = await response.json();
display.value = data.result;
```

- Receives the calculated result
- Displays it on screen

---

## 🎨 style.css – Visual Styling

### Purpose

- Makes the calculator look clean and usable
- Uses modern CSS layout techniques

---

### Centering the Calculator

```css
body {
  display: flex;
  justify-content: center;
  align-items: center;
}
```

- Uses Flexbox to center content

---

### Calculator Container

```css
#calculator {
  background-color: hsl(0, 0%, 15%);
  border-radius: 15px;
}
```

- Dark theme with rounded corners

---

### Display Styling

```css
#display {
  font-size: 2rem;
  direction: rtl;
}
```

- Large text
- Scrolls from right (calculator-style)

---

### Buttons

```css
button {
  font-size: 1.5rem;
  cursor: pointer;
}
```

- Large, clickable buttons

---

### Operator Buttons

```css
.operator-btn {
  background-color: hsl(35, 100%, 55%);
}
```

- Operators stand out visually

---

## 🚀 What You Learned from This Project

- How Flask serves HTML pages
- How JavaScript talks to Python
- How POST requests work
- How JSON is used for data exchange
- How frontend and backend responsibilities are separated

---

## 🧩 Possible Extensions

- Add square root, power, or percentage
- Replace `eval()` with safe parsing
- Add keyboard support
- Add error highlighting
- Deploy online using Render or PythonAnywhere

---
