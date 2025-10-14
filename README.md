# 🧪 Regular Expression Tester

This repository contains an interactive web application built with **Streamlit** that allows users to test and visualize Python's built-in **`re` (regular expression)** module functionalities in real-time.

It provides a comprehensive interface to experiment with different regex patterns, source strings, and various search methods.

## 🚀 Live Application

You can use the fully deployed version of this application immediately by clicking the link below:

[**Launch the Live Regex Tester App**](https://regex-app-demo-gsxn8vak6qjluapc3fkcjw.streamlit.app/)

-----

## ✨ Features

  * **Multiple Operations:** Test patterns using `re.findall()`, `re.search()`, `re.match()`, and `re.sub()`.
  * **Visual Highlighting:** Easily see where your pattern matches in the source text.
  * **Regex Flags:** Toggle common Python regex flags like `re.IGNORECASE` and `re.MULTILINE`.
  * **Substitution (`re.sub`):** Test replacement strings and instantly see the output of the substitution function.

-----

## 📂 Repository Contents

| File | Description |
| :--- | :--- |
| `app.py` | The main Python script containing all the Streamlit application logic and the regex functions. |
| `requirements.txt` | Lists the single required dependency: `streamlit`. |

-----

## 💻 Local Setup and Run

To run this application on your local machine, follow these steps:

### 1\. Clone the repository

```bash
git clone https://github.com/POORNI1336/Regular-Expression-Tester.git
cd Regular-Expression-Tester
```

### 2\. Install dependencies

Install the necessary Python package (`streamlit`) using the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

### 3\. Run the Streamlit Application

Start the interactive application using the Streamlit command:

```bash
streamlit run app.py
```

This command will automatically open the application in your default web browser at `http://localhost:8501`.
