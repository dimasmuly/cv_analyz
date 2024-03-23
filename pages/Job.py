import streamlit as st
from modules.data import Data
import yaml
from yaml.loader import SafeLoader
from streamlit_authenticator import Authenticate

with open('config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

    
authenticator = Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)

name, authentication_status, username = authenticator.login(fields='main')

if authentication_status:
    authenticator.logout('Logout', 'main')
    data = Data()

    skills = ["Web Development", "Mobile Development", "UI/UX", "DevOps"]
    selected_skill = st.selectbox(
        "Select a role", skills)
    role = None

    if selected_skill == "Web Development":
        role = '0'
    elif selected_skill == "Mobile Development":
        role = '1'
    elif selected_skill == "UI/UX":
        role = '2'
    elif selected_skill == "DevOps":
        role = '3'

    job_desc = data.get_job_description(role)
    new_job_desc = st.text_area('Job Description', value=job_desc)

    if st.button("Update"):
        data.update_job_description(role, new_job_desc)
elif authentication_status == False:
    st.error('Username/password is incorrect')
elif authentication_status == None:
    st.warning('Please enter your username and password')
