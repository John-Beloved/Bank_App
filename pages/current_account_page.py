import streamlit as st
from current_account import CurrentAccount

st.set_page_config(page_title="Current account", layout="centered")
my_current = CurrentAccount(100000)


st.markdown("<h1 style='font-size: 50px;'>Current Account</h1>", unsafe_allow_html=True)
with st.form("current-form"):
    st.write(f'<p style="font-size: 24px;">Current Account Balance: {my_current.balance}</p>', unsafe_allow_html=True)
    amount = st.number_input("Enter Amount", min_value=1000)
    operations = st.selectbox("Deposit/Withdraw", ("Deposit", "Withdraw"))
    submit = st.form_submit_button("Submit")

    if submit:
        with st.spinner("Processing..."):
            if operations == "Withdraw":
                 try:
                        my_current.withdraw(amount)
                        st.success(f"New balance: {my_current.balance}")
                 except ValueError as e:
                        st.error(str(e))
            elif operations == "Deposit":
                my_current.deposit(amount)
                st.success(f"New balance: {my_current.balance}")