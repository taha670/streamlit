import streamlit as st

def calculator():
    st.title("Simple Calculator")

    # Input fields for numbers
    num1 = st.number_input("Enter the first number:", value=0.0, step=0.1, format="%.2f")
    num2 = st.number_input("Enter the second number:", value=0.0, step=0.1, format="%.2f")

    # Dropdown for operation selection
    operation = st.selectbox("Choose an operation:", ["Add", "Subtract", "Multiply", "Divide"])

    # Perform calculation based on selected operation
    if operation == "Add":
        result = num1 + num2
        st.success(f"The result of addition is: {result}")
    elif operation == "Subtract":
        result = num1 - num2
        st.success(f"The result of subtraction is: {result}")
    elif operation == "Multiply":
        result = num1 * num2
        st.success(f"The result of multiplication is: {result}")
    elif operation == "Divide":
        if num2 != 0:
            result = num1 / num2
            st.success(f"The result of division is: {result}")
        else:
            st.error("Division by zero is not allowed.")

if _name_ == "_main_":
    calculator()
