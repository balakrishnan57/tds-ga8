import streamlit as st

st.title('Maximum of three numbers')
st.subheader('B Balakrishnan 21f2000490')

number1 = st.number_input('Number 1',format = '%d', step = 1)
number2 = st.number_input('Number 2', format = '%d', step = 1)
number3 = st.number_input('Number 3', format = '%d', step = 1)

maximum = max(number1, number2, number3)

st.write(f"The maximum is {maximum}.")
