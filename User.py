import streamlit as st
import pandas as pd
from modules.processor import process_text
import numpy as np
from modules.data import Data
from googletrans import Translator
import requests

st.set_page_config(
    page_title="Job Application Matcher - User",
    page_icon="🧊",
)

st.sidebar.title("Job Application Matcher")
st.image("logo.jpeg", width=350)
st.subheader("Input your details")

col1, col2 = st.columns(2)

with col1:
    name = st.text_input("Name",)
    age = st.text_input("Age")
with col2:
    address = st.text_input("Address")
    gender = st.selectbox("Gender", ["Male", "Female"])

linkedin_url = st.text_input("LinkedIn URL")

if st.button("Submit"):
    if name and linkedin_url:
        try:
            # Mengatur endpoint API dan header
            api_endpoint = 'https://nubela.co/proxycurl/api/v2/linkedin'
            api_key = '-jZgYBFOjonR-tOd3fPcyA'
            headers = {'Authorization': 'Bearer ' + api_key}

            # Mengambil data profil LinkedIn menggunakan proxycurl
            response = requests.get(api_endpoint,
                                    params={'url': linkedin_url, 'skills': 'include'},
                                    headers=headers)
            profile_data = response.json()

            # Mendapatkan deskripsi pekerjaan dari profil LinkedIn
            about = profile_data["summary"]

            if about is not None:
                result = process_text(about)
                pred_score = result.detach().numpy().squeeze()
                pred_class = np.argmax(pred_score)

                st.subheader("Your details:")
                st.write(f"Name: {name}")
                st.write(f"Age: {age}")
                st.write(f"Address: {address}")
                st.write(f"Gender: {gender}")

                # Menampilkan bagian 'About' dari profil LinkedIn
                st.subheader("About:")
                st.write(about.replace('\\n', ''))

                # Menampilkan prediksi score
                st.subheader("Prediction Score:")
                score_dict = {0: "Web Development",
                              1: "Mobile Development", 2: "UI/UX", 3: "DevOps"}
                score_df = pd.DataFrame({"Job Category": list(
                    score_dict.values()), "Score": pred_score})
                score_df.set_index("Job Category", inplace=True)
                st.table(score_df.style.format({"Score": "{:.3f}"}))

                # Menampilkan hasil prediksi kelas
                pred_class_label = score_dict[pred_class]
                pred_class_score = float("{:.3f}".format(pred_score[pred_class]))

                st.subheader("Prediction Skills:")
                st.write(pred_class_label)
                st.write(f"Score: {pred_class_score}")

                # Insert data
                Data().add_applicant(name=name, age=age,
                                    job_desc=about, address=address,
                                    gender=gender, pred_score=pred_score,
                                    primary_role=pred_class, primary_role_score=pred_class_score
                                    )
            else:
                st.warning("No 'About' section found in the LinkedIn profile.")
        except Exception as e:
            about = None
