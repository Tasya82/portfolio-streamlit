import streamlit as st

st.set_page_config(layout='wide')
st.title('My Portfolio')
st.header('Data Scientist')

st.sidebar.title('Navigation')

page = st.sidebar.radio('Choose page', ['About Me', 'Project', 'Contact'])

if page == 'About Me':
    import About
    About.about_me()
elif page == 'Contact':
    import Contact
    Contact.showing_contact()
elif page == 'Project':
    import Project
    Project.show_project()