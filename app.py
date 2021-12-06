# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 18:43:25 2021

@author: kingl
"""

import streamlit as st
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
import pickle
from pathlib import Path

model_file = Path("Modeling/model.pkl").absolute()
infile = open(model_file, 'rb')
model = pickle.load(infile)

#preprocessing user inputs
def preprocessing(df):
    le = LabelEncoder()
    df.Profession = le.fit_transform(df.Profession)
    df.CITY = le.fit_transform(df.CITY)
    df.STATE = le.fit_transform(df.STATE)
    scaler = StandardScaler()
    df = scaler.fit_transform(df)
    return(df)


#preprocessing(data)

# format app to fill screen width
st.set_page_config(layout="wide")

# set main title of application
st.markdown("<h1 style='text-align: center;'>Loan Default Dashboard</h1>", unsafe_allow_html=True)

# create sidebar with multiple options
sidebar = st.sidebar.selectbox("Navigation", ("Main", "Risk Assessment", "Information", "Other"))


data = pd.read_csv("https://raw.githubusercontent.com/mattflaherty97/case-2-team-3/main/Data/app_data.csv")
unique_professions = data['Profession'].unique()
unique_cities = data['CITY'].unique()
unique_states = data['STATE'].unique()


# code for main page
if sidebar == 'Main':
        
    # Page Content
    st.markdown("<h2 style='text-align: center;'>Main Page</h2>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center;'>Through the navigation sidebar, the various application functionalities can be accessed.</h3>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center;'>For documentation, code, and all other relevant files, see the <a href='https://github.com/mattflaherty97/case-2-team-3'>project repo</a>.</h3>", unsafe_allow_html=True)
    #col1, col2, col3 = st.columns([1,1,1]) # this allows us to center the image by selecting col2 in next line
    #col2.image(vandy, use_column_width=True)

# code for application page
if sidebar == 'Risk Assessment':

    # Page Header
    st.markdown("<h2 style='text-align: center;'>User Page</h2>", unsafe_allow_html=True)
        
    income = st.number_input("Applicant Income:", step = 1)
    
    age = st.number_input("Applicant Age:", step = 1)
    
    experience = st.number_input("Applicant Work Experience:", step = 1)
    
    marital_status = st.selectbox("Applicant Marital Status:", ("Single", "Married"))
    if marital_status == "Single":
        final_marital_status = 0
    if marital_status == "Married":
        final_marital_status = 1
    
    house_ownership = st.selectbox("Applicant House Status:", ("None", "Rent", "Own"))
    if house_ownership == "None":
        final_house_ownership = 1
    if house_ownership == "Rent":
        final_house_ownership = 0
    if house_ownership == "Own":
        final_house_ownership = 2
    
    car_ownership = st.selectbox("Applicant Car Ownership Status:", ("Own", "Not Own"))
    if car_ownership == "Own":
        final_car_ownership = 1
    if car_ownership == "Not Own":
        final_car_ownership = 0
    
    profession = st.selectbox("Applicant Profession:", np.sort(unique_professions))
    
    city = st.selectbox("Applicant City:", np.sort(unique_cities))
    
    state = st.selectbox("Applicant State:", np.sort(unique_states))
    
    job_years = st.number_input("Applicant Years at Current Job:", step = 1)
    
    house_years = st.number_input("Applicant Years at Current Residence:", step = 1)
    
    GDP = st.slider("Applicant State GDP (billions):", 0, int(max(data['GDP'])), 1)
    
    input_list = [income, age, experience,  final_marital_status,  final_house_ownership,  final_car_ownership, profession, city, state, job_years, house_years, GDP]
    
    data_length = len(data)
    data.loc[data_length] = input_list
    
    final = preprocessing(data)
    
    if st.button('Get Applicant Default Risk'):
        risk_score = float(model.predict_proba(final[-1].reshape(1,12))[:,1])
        if risk_score < .33:
            risk_assessment = "Low-Risk Applicant! "
            st.success("".join([risk_assessment, "Default Risk: ", str(int(risk_score*100)), "%"]))
        if risk_score > .33 and risk_score < .66:
            risk_assessment = "Moderate-Risk Applicant! "
            st.warning("".join([risk_assessment, "Default Risk: ", str(int(risk_score*100)), "%"]))
        if risk_score > .66:
            risk_assessment = "High-Risk Applicant! "
            st.error("".join([risk_assessment, "Default Risk: ", str(int(risk_score*100)), "%"]))
    
# code for application page
if sidebar == 'Information':

    # Page Header
    st.markdown("<h2 style='text-align: center;'>Government Page</h2>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center;'>Check back soon for additional functionality!</h3>", unsafe_allow_html=True)
    
# code for application page
if sidebar == 'Other':

    # Page Header
    st.markdown("<h2 style='text-align: center;'>Other Page</h2>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center;'>Check back soon for additional functionality!</h3>", unsafe_allow_html=True)