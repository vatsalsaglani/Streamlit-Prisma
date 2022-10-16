import streamlit as st
from utilities import Movies
from components import card, grid

st.set_page_config(page_title='Prisma Demo', page_icon='💎')

movObj = Movies()

st.markdown(
    """<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
""",
    unsafe_allow_html=True)
st.header("Prisma Demo")

st.markdown("""
## Introduction
This application is connected to a PostgreSQL DB hosted on AWS RDS using Prisma. Its a small demo w.r.t. how one can use the simplicity of Streamlit and the powerful Prisma ORM to connect any SQL or NoSQL database and develop a data app in no time
""")

movieText = st.text_input("Search Movies")

if movieText:
    with st.spinner(text="Searching.."):
        movies = movObj.list_movies_by_title(movieText.rstrip().lstrip())
        # for ix in range()
        st.markdown("""<br />""", unsafe_allow_html=True)
        st.markdown(grid(movies), unsafe_allow_html=True)