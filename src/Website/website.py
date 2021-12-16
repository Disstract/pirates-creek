# import module
import streamlit as st
 
def run(text):
    st.write(text)

# Title
st.title("Site Name")

search = st.text_input("Enter a search:","")

if st.button("Search", key="Search", help="Click button to search query"):
    run(search)
else:
    pass


