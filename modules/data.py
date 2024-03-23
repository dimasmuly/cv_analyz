import streamlit as st
from numpy import ndarray
import json


class Data():
    def __init__(self):
        self.__conn__ = st.connection('mysql', type='sql')

    def get_applicants(self, role: str):
        data = self.__conn__.query("SELECT * from applicants WHERE primary_role = :role ORDER BY primary_role_score DESC;",
                                   params={'role': role}, ttl=0)
        return data.itertuples()

    def add_applicant(self, name: str, age: int, address: str,
                      gender: str, pred_score: ndarray,
                      job_desc: str,
                      primary_role: int, primary_role_score: float) -> None:
        json_score = []
        for score in pred_score:
            json_score.append(float("{:.3f}".format(score)))
        json_score = json.dumps(json_score)

        with self.__conn__.session as session:
            session.execute(
                'INSERT INTO applicants (name, job_desc, age, address, gender, primary_role, primary_role_score, score) \
                    VALUES (:name, :job_desc, :age, :address, :gender, :primary_role, :primary_role_score, :score);',
                {'name': name,
                 'age': age,
                 'address': address,
                 'gender': gender,
                 'job_desc': job_desc,
                 'primary_role': primary_role,
                 'primary_role_score': primary_role_score,
                 'score': json_score
                 })
            session.commit()

    def get_job_description(self, role: str):
        data = self.__conn__.query("SELECT * from jobs WHERE role = :role;",
                                   params={'role': role}, ttl=0)
        return data['description'][0]

    def update_job_description(self, role: str, description: str):
        with self.__conn__.session as session:
            session.execute(
                'UPDATE jobs SET description=:description WHERE role=:role;',
                {'description': description,
                 'role': role
                 })
            session.commit()
