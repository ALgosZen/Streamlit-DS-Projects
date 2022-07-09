import streamlit as st

st.title("Streamlit DataScience Project Dashboard")

st.header("this is a header")

st.subheader("this is subheader")

st.text("this is text")

#this is magic text

"""
## header
### subheader 
"""

some_dictionary = {
    "first name":"suresh",
    "last name":"mallela"
}


st.write(some_dictionary)

some_list = [1,2,3]

some_text = st.write(some_list)
