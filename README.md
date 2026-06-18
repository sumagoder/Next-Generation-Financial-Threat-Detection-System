Here's your GitHub README description — just copy and paste:

---

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
- 
- 



### Transaction Risk Analysis
- Enter transaction details (type, amount, balances, currency)
- Get instant fraud probability percentage
- View a **Fraud Risk Score Gauge** (0–100)
- Download a detailed transaction analysis report

---

## ⚙️ System Architecture

```
Data Source → Data Preprocessing → Feature Selection → ML Model Training → Fraud Detection → Alert System
<img width="1536" height="1024" alt="System_architecture_diagram" src="https://github.com/user-attachments/assets/cf447077-e370-4987-9365-ef48699d1819" />  

```

---

## 🧠 Machine Learning Model

| Property | Details |
|---|---|
| Algorithm | Decision Tree Classifier |
| Framework | Scikit-learn |
| Training Data | PaySim Financial Transaction Dataset |
| Model File | `models/fraud_model.pkl` |

### Input Features

| Feature | Description |
|---|---|
| `step` | Unit of time (1 step = 1 hour) |
| `amount` | Transaction amount |
| `oldbalanceOrg` | Sender's balance before transaction |
| `newbalanceOrig` | Sender's balance after transaction |
| `oldbalanceDest` | Receiver's balance before transaction |
| `newbalanceDest` | Receiver's balance after transaction |
| `isFlaggedFraud` | Flagged by rule engine |
| `type_CASH_IN/OUT/DEBIT/PAYMENT/TRANSFER` | One-hot encoded transaction type |

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

### 3. Add the dataset
Download the [PaySim dataset from Kaggle](https://www.kaggle.com/datasets/ealaxi/paysim1) and place it at:
```
data/transactions.csv 
```

### 4. Run the app
```bash
streamlit run app.py
```

---

## 📁 Project Structure

```
fraud-detection-project/
├── app.py                  ← Streamlit web application
├── models/
│   └── fraud_model.pkl     ← Trained Decision Tree model
├── data/                   ← Place your dataset CSV here
├── docs/
│   └── System_architecture_diagram.png
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
| Matplotlib / Seaborn | Data visualization |
| Streamlit | Web application UI |
| Plotly | Interactive charts & gauge |

---

## ✅ Key Features

- **Automated fraud detection** — classifies transactions as fraudulent or legitimate instantly
- **Fraud probability score** — shows percentage likelihood of fraud for each transaction
- **Interactive dashboard** — real-time metrics including total transactions, fraud rate, and blocked count
- **Risk gauge chart** — visual 0–100 fraud risk score with color-coded zones (green / yellow / red)
- **Multi-currency support** — accepts 10 currencies; flags non-INR transactions as high risk
- **Fraud report download** — export fraud transaction data as CSV
- **Transaction visualization** — activity line graph and fraud vs legitimate pie chart

---

## 📊 Dataset

This project uses the **PaySim Synthetic Financial Dataset** simulating mobile money transactions.

- 📥 Download: [Kaggle – PaySim Dataset](https://www.kaggle.com/datasets/ealaxi/paysim1)
- Place the CSV file in the `data/` folder before running

---

## 📚 Literature Survey

Recent research that motivated this project:

| Paper | Year | Key Contribution |
|---|---|---|
| Credit Card Fraud Detection with Subspace Learning | 2023 | Handles imbalanced datasets |
| Enhancing Detection using Neural Network & SMOTE | 2024 | Balances datasets with oversampling |
| Hybrid Ensemble ML Model for Fraud Detection | 2024 | Combines multiple ML algorithms |
| Heterogeneous Graph Auto-Encoder | 2024 | Uses Graph Neural Networks |
| Comparative Study of ML Models | 2025 | Benchmarks SVM, RF, Neural Networks |

---

## 🎯 Conclusion

This system demonstrates how machine learning can effectively identify fraudulent financial transactions in real time. By analyzing transaction type, amount, and account balances, the model detects suspicious patterns and provides instant predictions through an interactive Streamlit interface. The project highlights the potential of AI-driven solutions to improve security and reduce financial risks in digital banking systems.

---
