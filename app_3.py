import streamlit as st
import pandas as pd
import joblib
import plotly.graph_objects as go
import plotly.express as px
import datetime

# ---------------- PAGE CONFIG ----------------

st.set_page_config(
    page_title="Financial Threat Detection System",
    layout="wide"
)

# ---------------- LOAD MODEL ----------------

model = joblib.load("fraud_model.pkl")

# ---------------- LOAD DATASET ----------------

dataset = pd.read_csv(
"C:/Fraud_Detection/PS_20174392719_1491204439457_log1.csv/PS_20174392719_1491204439457_log.csv",
nrows=20000
)

# ---------------- HEADER ----------------

col1,col2 = st.columns([4,1])

with col1:
    st.title("🏦 Financial Threat Detection System")

with col2:
    now = datetime.datetime.now()
    st.write("Date:", now.strftime("%d %b %Y"))
    st.write("Time:", now.strftime("%H:%M"))

st.divider()

# ---------------- SIDEBAR ----------------

st.sidebar.title("🏦 Bank Fraud System")

page = st.sidebar.radio(
"Navigation",
["Dashboard","Transaction Analysis"]
)

st.sidebar.markdown("---")

st.sidebar.subheader("Instructions")

st.sidebar.write("""
1. Go to **Transaction Analysis**
2. Enter transaction details
3. Click **Analyze Transaction**
4. System predicts fraud probability
""")

st.sidebar.markdown("---")

st.sidebar.subheader("Fraud Detection Rules")

st.sidebar.write("""
• Foreign currency transactions are high risk

• Large transaction amounts increase fraud risk

• Balance mismatch may indicate fraud

• Machine learning model analyses transaction behaviour
""")

# ---------------- DASHBOARD ----------------

if page == "Dashboard":

    total_tx = len(dataset)
    fraud_tx = dataset["isFraud"].sum()
    legit_tx = total_tx - fraud_tx
    blocked_tx = fraud_tx

    col1,col2,col3,col4 = st.columns(4)

    col1.metric("Total Transactions Today", total_tx)
    col2.metric("Legitimate Transactions", legit_tx)
    col3.metric("Fraud Transactions", fraud_tx)
    col4.metric("Blocked Transactions", blocked_tx)

    total_amount = dataset["amount"].sum()
    fraud_rate = round((fraud_tx/total_tx)*100,2)

    col5,col6 = st.columns(2)

    col5.metric("Total Amount Today", f"₹{total_amount:,.0f}")
    col6.metric("Fraud Rate", f"{fraud_rate}%")

    st.divider()

    col7,col8 = st.columns(2)

    with col7:

        st.subheader("Transaction Activity")

        activity = dataset.groupby("step").size().reset_index(name="transactions")

        fig = px.line(
        activity.head(100),
        x="step",
        y="transactions"
        )

        st.plotly_chart(fig,use_container_width=True)

    with col8:

        st.subheader("Fraud vs Legitimate")

        fraud_counts = dataset["isFraud"].value_counts()

        fig2 = px.pie(
        values=fraud_counts,
        names=["Legitimate","Fraud"]
        )

        st.plotly_chart(fig2,use_container_width=True)

    st.divider()

    if fraud_tx > 0:

        st.error("""
🚨 FRAUD ALERT

High risk transactions detected

Status: Blocked
""")

    st.subheader("Today's Fraudulent Transactions")

    fraud_data = dataset[dataset["isFraud"]==1].head(10)

    st.dataframe(
    fraud_data[
    ["type","amount","oldbalanceOrg","newbalanceOrig"]
    ]
    )

    csv = fraud_data.to_csv(index=False)

    st.download_button(
    label="Download Fraud Report",
    data=csv,
    file_name="fraud_report.csv",
    mime="text/csv"
    )

# ---------------- TRANSACTION ANALYSIS ----------------

elif page == "Transaction Analysis":

    st.title("Transaction Risk Analysis")

    col1,col2 = st.columns(2)

    with col1:

        type_option = st.selectbox(
        "Transaction Type",
        ["CASH_IN","CASH_OUT","DEBIT","PAYMENT","TRANSFER"]
        )

        currency = st.selectbox(
        "Currency",
        [
        "INR (India)",
        "USD (United States)",
        "EUR (Europe)",
        "GBP (United Kingdom)",
        "JPY (Japan)",
        "AUD (Australia)",
        "CAD (Canada)",
        "SGD (Singapore)",
        "AED (UAE)",
        "CNY (China)"
        ]
        )

        amount = st.text_input("Transaction Amount")
        oldbalanceOrg = st.text_input("Old Balance Sender")
        newbalanceOrig = st.text_input("New Balance Sender")

    with col2:

        oldbalanceDest = st.text_input("Old Balance Receiver")
        newbalanceDest = st.text_input("New Balance Receiver")

    if st.button("Analyze Transaction"):

        if amount and oldbalanceOrg and newbalanceOrig and oldbalanceDest and newbalanceDest:

            amount=float(amount)
            oldbalanceOrg=float(oldbalanceOrg)
            newbalanceOrig=float(newbalanceOrig)
            oldbalanceDest=float(oldbalanceDest)
            newbalanceDest=float(newbalanceDest)

            if currency!="INR (India)":

                probability=1
                prediction=1
                st.error("🚨 Fraudulent Transaction Detected (Foreign Currency)")

            else:

                type_CASH_IN = 1 if type_option=="CASH_IN" else 0
                type_CASH_OUT = 1 if type_option=="CASH_OUT" else 0
                type_DEBIT = 1 if type_option=="DEBIT" else 0
                type_PAYMENT = 1 if type_option=="PAYMENT" else 0
                type_TRANSFER = 1 if type_option=="TRANSFER" else 0

                data={
                'step':1,
                'type_CASH_IN':type_CASH_IN,
                'type_CASH_OUT':type_CASH_OUT,
                'type_DEBIT':type_DEBIT,
                'type_PAYMENT':type_PAYMENT,
                'type_TRANSFER':type_TRANSFER,
                'amount':amount,
                'oldbalanceOrg':oldbalanceOrg,
                'newbalanceOrig':newbalanceOrig,
                'oldbalanceDest':oldbalanceDest,
                'newbalanceDest':newbalanceDest,
                'isFlaggedFraud':0
                }

                sample=pd.DataFrame([data])

                sample=sample[model.feature_names_in_]

                prediction=model.predict(sample)[0]
                probability=model.predict_proba(sample)[0][1]

                st.write("Fraud Probability:",round(probability*100,2),"%")

                if prediction==1:
                    st.error("🚨 Fraudulent Transaction Detected")
                else:
                    st.success("✅ Legitimate Transaction")

            st.divider()

            # ---------------- RISK GAUGE ----------------

            st.subheader("Fraud Risk Score")

            risk_score=int(probability*100)

            fig = go.Figure(go.Indicator(
            mode="gauge+number",
            value=risk_score,
            title={'text':"Fraud Risk Score"},
            gauge={
            'axis':{'range':[0,100]},
            'steps':[
            {'range':[0,30],'color':"green"},
            {'range':[30,70],'color':"yellow"},
            {'range':[70,100],'color':"red"}
            ]
            }
            ))

            st.plotly_chart(fig)

            # ---------------- REPORT GENERATION ----------------

            st.subheader("Transaction Analysis Report")

            if probability < 0.3:
                risk_level="Low Risk"
            elif probability < 0.7:
                risk_level="Medium Risk"
            else:
                risk_level="High Risk"

            result = "Fraudulent Transaction" if prediction==1 else "Legitimate Transaction"

            report_data={
            "Transaction Type":[type_option],
            "Currency":[currency],
            "Amount":[amount],
            "Sender Old Balance":[oldbalanceOrg],
            "Sender New Balance":[newbalanceOrig],
            "Receiver Old Balance":[oldbalanceDest],
            "Receiver New Balance":[newbalanceDest],
            "Fraud Probability (%)":[round(probability*100,2)],
            "Prediction Result":[result],
            "Risk Level":[risk_level]
            }

            report_df=pd.DataFrame(report_data)

            st.dataframe(report_df)

            csv = report_df.to_csv(index=False)

            st.download_button(
            label="Download Transaction Report",
            data=csv,
            file_name="transaction_analysis_report.csv",
            mime="text/csv"
            )

        else:

            st.warning("Please fill all fields before analysing the transaction.")