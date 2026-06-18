# 🏦 Financial Threat Detection System

A machine learning-powered web application that detects fraudulent financial transactions in real time. Built using Python, Scikit-learn, and Streamlit, this system analyzes transaction patterns and classifies them as **legitimate ✅** or **fraudulent 🚨** with a fraud probability score.

---

## 📌 Project Overview

The rapid growth of digital banking has increased financial fraud such as unauthorized transactions and identity theft. Traditional rule-based fraud detection systems fail to detect new fraud patterns. This project solves that problem by using a **Decision Tree Classifier** trained on real financial transaction data to intelligently detect suspicious activities automatically.

---

## 🖥️ Application Screenshots

### Dashboard
- <img width="1792" height="831" alt="image" src="https://github.com/user-attachments/assets/32cccfeb-2dbd-422d-8d53-010190165697" />
- <img width="1749" height="793" alt="image" src="https://github.com/user-attachments/assets/176dfeea-7061-4070-b6a6-514f3083046c" />
- <img width="1802" height="874" alt="image" src="https://github.com/user-attachments/assets/01599d12-677c-4ba8-ad18-12afd5506bc9" />
- <img width="416" height="828" alt="image" src="https://github.com/user-attachments/assets/815ebff9-8a5b-4ff7-9630-8b22ec3e3708" />
- <img width="1472" height="828" alt="image" src="https://github.com/user-attachments/assets/0f07f8c1-f763-453a-ab08-0b498eabc5c1" />

## ⚙️ System Architecture

```
Data Source → Data Preprocessing → Feature Selection → ML Model Training → Fraud Detection → Alert System
![Uploading image.png…]()

```

## 🧠 Machine Learning Model

| Property | Details |
|---|---|
| Algorithm | Decision Tree Classifier |
| Framework | Scikit-learn |
| Model File | `fraud_model.pkl` |

---

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/sumagoder/fraud-detection-project.git
cd fraud-detection-project
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the app
```bash
streamlit run app.py
```

---

## 📁 Project Structure

```
fraud-detection-project/
├── app.py
├── fraud_model.pkl
├── requirements.txt
└── README.md
```

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Pandas | Data preprocessing & analysis |
| NumPy | Numerical computations |
| Scikit-learn | ML model development |
| Streamlit | Web application UI |
| Plotly | Interactive charts & gauge |

---

## ✅ Key Features

- **Automated fraud detection** — classifies transactions as fraudulent or legitimate instantly
- **Fraud probability score** — shows percentage likelihood of fraud for each transaction
- **Interactive dashboard** — real-time metrics including total transactions, fraud rate, and blocked count
- **Risk gauge chart** — visual 0–100 fraud risk score with color-coded zones
- **Multi-currency support** — accepts 10 currencies; flags non-INR transactions as high risk
- **Fraud report download** — export fraud transaction data as CSV

---

## 🎯 Conclusion

This system demonstrates how machine learning can effectively identify fraudulent financial transactions in real time. By analyzing transaction type, amount, and account balances, the model detects suspicious patterns and provides instant predictions through an interactive Streamlit interface.

---





