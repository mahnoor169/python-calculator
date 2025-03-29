
# # this is a simple calculator code without streamlit:-


# operation = input("Enter the operation (+, -, *, /): ")

# num1 = float(input("Enter the first number: "))
# num2 = float(input("Enter the second number: "))

# if operation == "+":
#     print(f"The result is: {num1 + num2}")
# elif operation == "-":
#     print(f"The result is: {num1 - num2}")
# elif operation == "*":
#     print(f"The result is: {num1 * num2}")
# elif operation == "/":
#     if num2 != 0:
#         print(f"The result is: {num1 / num2}")
#     else:
#         print("Error: Division by zero is not allowed.")
# else:
#     print("Invalid operation.")





# with streamlit:-


import streamlit as st

st.title("🧮 Simple Calculator 🔢")

operation = st.selectbox("select an operation", ["+", "-", "*", "/"])

num1 = st.number_input("Enter the first number", step = 0.1, format = "%.2f")
num2 = st.number_input("Enter the second number", step = 0.1, format = "%.2f")


result = None
if st.button("Calculate"):

    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        if num2 != 0:
            result = num1 / num2
        else:
           result = "Error: Division by zero is not allowed."

st.success(f"Result: {result}")




 