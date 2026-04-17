# 🚀 AI Test Generator VS Code Extension

## 📌 Overview

This project is a **VS Code extension** that automatically generates test cases (e.g., Jest tests) for your code using an AI backend.

### 🔁 Core Flow

```
User runs command → Code is extracted → Sent to AI backend → Tests generated → .test.js file created
```

---

## 🧠 How It Works

1. You open a file in VS Code
2. Run the command: `Generate AI Tests`
3. Extension reads your code
4. Sends it to backend (`http://localhost:8000/generate-tests`)
5. AI returns test cases
6. Extension creates a new file:

```
Component.js → Component.test.js
```

---

## 🧱 Project Structure

```
project/
 ├── package.json        # Defines commands & activation
 ├── extension.js        # Core extension logic
 ├── .vscode/            # Debug configuration (optional)
 ├── README.md
```

---

## ⚙️ Key Files Explained

### 📄 `package.json`

* Registers the command
* Controls when extension activates

```json
"activationEvents": [
  "onCommand:ai-test-generator.generateTests"
]
```

---

### 📄 `extension.js`

Contains the main logic:

* Reads active file
* Sends code to backend
* Receives test code
* Creates `.test.js` file

---

### 📁 `.vscode/launch.json`

* Used only for debugging (F5)
* Not required for extension to run

---

## ▶️ Running the Extension

### 🔹 Step 1: Start Backend

```bash
uvicorn main:app --reload
```

---

### 🔹 Step 2: Run Extension

Press:

```
F5
```

This opens a new **Extension Development Host** window.

---

### 🔹 Step 3: Run Command

* Press `Ctrl + Shift + P`
* Search: `Generate AI Tests`
* Run it

---

## 🔧 What Happens on F5

```
F5 pressed
   ↓
VS Code reads launch.json
   ↓
Opens new VS Code window (Extension Host)
   ↓
You trigger command
   ↓
Extension logic runs
```

---

## ❗ Notes

* `.vscode` folder is optional
* Extension works without it
* It is only used for debugging

---

## 🧰 Tools Used

### Yeoman (`yo`)

* Project scaffolding tool

### generator-code

* Template for VS Code extensions

```
yo → generator-code → extension project
```

---

