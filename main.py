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

    tab1, tab2, tab3, tab4 = st.tabs(["show_project", "Project Dashboard", "Project Prediction", "Attrition Proportion"])

    with tab1:
        Project.show_project()
    with tab2:
        Project.Dashboard1()
    with tab3:
        Project.Prediction1()
    with tab4:
        Project.Prediction2()