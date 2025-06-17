import streamlit as st
from savings_account import SavingsAccount

st.set_page_config(page_title="Savings account", layout="centered")
my_savings = SavingsAccount(100000, 5000)


st.markdown("<h1 style='font-size: 50px;'>Savings Account</h1>", unsafe_allow_html=True)
with st.form("savings-form"):
    st.write(f'<p style="font-size: 24px;">Savings Account Balance: {my_savings.balance}</p>', unsafe_allow_html=True)
    amount = st.number_input("Enter Amount", min_value=1000)
    operations = st.selectbox("Deposit/Withdraw", ("Deposit", "Withdraw"))
    submit = st.form_submit_button("Submit")

    if submit:
        with st.spinner("Processing..."):
            if submit and operations == "Withdraw":
                try:
                        my_savings.withdraw(amount)
                        st.success(f"New balance: {my_savings.balance}")
                except ValueError as e:
                        st.error(str(e))
            elif operations == "Deposit":
                try:
                        my_savings.deposit(amount)
                        st.success(f"New balance: {my_savings.balance}")
                except ValueError as e:
                        st.error(str(e))
