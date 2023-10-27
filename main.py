import streamlit as st
import langchain_helper

st.title("Restaurant Name and Menu Generator")

cusine = st.sidebar.selectbox("Pick a cusine", ("Indian", "Persian", "Mexican", "Arabic"))



if cusine:
    response = langchain_helper.generate_restaurant_name_and_items(cusine)
    st.header(response['restaurant_name'].strip())  # strip() method removes any leading, and trailing whitespaces.
    menu_items = response['menu_items'].strip().split(",")
    st.write("**Menu Items**")

    for item in menu_items:
        st.write("-", item)