import streamlit as st
import pandas as pd
from modules.data import Data
from modules.utils import count_word_occurences

st.set_page_config(
    page_title="Job Application Matcher - HRD",
    page_icon="🧊",
)

st.sidebar.title("Job Application Matcher")
st.image("logo.jpeg", width=350)
st.subheader("Select role")

data = Data()

skills = ["Web Development", "Mobile Development", "UI/UX", "DevOps"]
selected_skill = st.selectbox(
    "Select a role", skills, label_visibility='hidden')
role = None

if selected_skill == "Web Development":
    role = '0'
elif selected_skill == "Mobile Development":
    role = '1'
elif selected_skill == "UI/UX":
    role = '2'
elif selected_skill == "DevOps":
    role = '3'


st.subheader("Applicant details")

name_company = "IndoTech"
address = "Jakarta Selatan"
job_desc = data.get_job_description(role)
st.write("Name Company:", name_company)
st.write("Address:", address)
st.write("Job description:", job_desc)
st.subheader("All applicants")

# Get applicants data based on selected role 
applicants_data = data.get_applicants(role)
applicants = []

# Get keyword based on job description
target_word = count_word_occurences(job_desc)
print(target_word)

# For each applicant, add/decrease score based on matched keyword
for applicant in applicants_data:
    occurence_score = 0
    word_occurence_count = len(count_word_occurences(applicant.job_desc, target_word))
    
    if word_occurence_count > 0:
        occurence_score += 2 * word_occurence_count
    score = applicant.primary_role_score + ((occurence_score) / 10)

    applicants.append({
        'name': applicant.name,
        'address': applicant.address,
        'age': applicant.age,
        'job_desc': applicant.job_desc,
        'score': score
    })

# Sort applicants data based on the new calculated score
applicants.sort(key=lambda el: el['score'], reverse=True)

applicants_data = {
    "Name": [applicant['name'] for applicant in applicants],
    "Age": [applicant['age'] for applicant in applicants],
    "Address": [applicant['address'] for applicant in applicants],
    "Job Description": [applicant['job_desc'] for applicant in applicants],
    "Score": [applicant['score'] for applicant in applicants],
}


df = pd.DataFrame(applicants_data)
st.write(df)