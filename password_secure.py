#Step 1: Importing streamlit and making a fuction
import streamlit as st
import random as r
import string as g

def generate_pass(length:int):
    all = g.ascii_letters + g.digits + g.punctuation
    password = ''
    for i in range(length):
        password += r.choice(all)
    return password

#Step 3:Creating the sidebar part
with st.sidebar:
    st.header('Enetr details:')
    pass_numbers = st.number_input(
        label = 'How many passwords ?',
        min_value = 1,
        max_value = 1000,
        value=1
        )
    pass_length = st.slider (
        label = 'Choose password length:',
        min_value=8,
        max_value=100,
        value = 16)

    button = st.button('Generate Password')


st.title('Secure Password Generator')    
st.header(':green[Generated passwords:]')

if button == True:
    for i in range(pass_numbers):
        result = generate_pass(pass_length)
        st.code(result)