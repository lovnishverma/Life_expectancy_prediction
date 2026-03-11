# 🌍 Life Expectancy Predictor Web App

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Flask](https://img.shields.io/badge/Flask-Backend-black)
![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-Glassmorphism-38B2AC)
![Machine Learning](https://img.shields.io/badge/Machine_Learning-Scikit_Learn-orange)

## 📌 Overview
This project is an end-to-end Machine Learning web application designed to predict **Life Expectancy** based on 19 health, economic, and demographic features. It utilizes a pre-trained machine learning model served via a Python Flask backend, coupled with a highly responsive, modern "glassmorphism" frontend built with Tailwind CSS.

## ✨ Features
* **Predictive Inference:** Uses a saved ML model (`model.joblib`) to instantly process user inputs and return accurate life expectancy estimates.
* **Modern UI/UX:** Features a stunning, mobile-friendly glassmorphism interface with custom gradients and hover states.
* **Robust Data Handling:** Captures and correctly types 19 distinct features (e.g., Adult Mortality, GDP, BMI, Polio, Status) before passing them to the model.
* **Lightweight Architecture:** Flask backend ensures fast routing and low-overhead inference.

## 🛠️ Tech Stack
* **Backend:** Python, Flask, Pandas, NumPy, Scikit-Learn / Joblib
* **Frontend:** HTML5, Tailwind CSS (via CDN)
* **Design Pattern:** MVC-inspired (Model-View-Controller)

## 📂 Project Structure
```text
├── app.py                  # Main Flask application and API routes
├── model.joblib            # Pre-trained Machine Learning model
├── requirements.txt        # Python dependencies
└── templates/
    ├── index.html          # Data input form (Glassmorphism UI)
    └── result.html         # Prediction output page (Optional: if separated)
