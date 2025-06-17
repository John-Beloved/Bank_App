import streamlit as st
from savings_account import SavingsAccount

st.set_page_config(page_title="Bank App", layout="centered")
my_savings = SavingsAccount(60000, 3000)

st.markdown("<h1 style='font-size: 50px;'>Bank App</h1>", unsafe_allow_html=True)
st.markdown("<p style='font-size: 24px;'>Where you can withdraw and deposit with ease</p>", unsafe_allow_html=True)
