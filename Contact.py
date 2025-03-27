import streamlit as st

def showing_contact():
    st.title("Contact")
    st.write("Contact me through these links:")

    # Define the image URL (replace with your image)
    icon_url = 'https://content.linkedin.com/content/dam/me/business/en-us/amp/brand-site/v2/bg/LI-Bug.svg.original.svg'  # React logo as an example

    # Define the LinkedIn URL
    link_url = 'www.linkedin.com/in/anggia-monnier'

    # Display the clickable icon as an image with Markdown
    st.markdown(f'<a href="{link_url}" target="_blank"><img src="{icon_url}" width="50" height="50"></a>', unsafe_allow_html=True)

    #Email
    st.write("Email: monnier.anggia@gmail.com")