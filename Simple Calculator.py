from unittest import result

import streamlit as st

st.title("Simple Calculator")

num1 = st.number_input("Enter the first number",step =1)
num2 = st.number_input("Enter the second number",step =2)

operation = st.selectbox("Select operator",
                         ["Add","Subtract", "Multiply", "Divide"])

if operation == "Divide" and num2 == 0:
    st.error("Divide by zero")
else:
    if operation == "Add":
        result = num1 + num2
    elif operation == "Subtract":
        result = num1 - num2
    elif operation == "Multiply":
        result = num1 * num2
    else:
        result = num1 / num2

    st.success(f"Result:{result}")

