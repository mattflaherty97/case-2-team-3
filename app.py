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


# format app to fill screen width
st.set_page_config(layout="wide")

# set main title of application
st.markdown("<h1 style='text-align: center;'>Loan Default Dashboard</h1>", unsafe_allow_html=True)

# create sidebar with multiple options
sidebar = st.sidebar.selectbox("Navigation", ("Main", "Risk Assessment", "Information", "Updates"))


data = pd.read_csv("https://raw.githubusercontent.com/mattflaherty97/case-2-team-3/main/Data/app_data.csv")
unique_professions = data['Profession'].unique()
unique_cities = data['CITY'].unique()
unique_states = data['STATE'].unique()


# code for main page
if sidebar == 'Main':
        
    # Page Content
    st.markdown("<h2 style='text-align: center;'>Main Page</h2>", unsafe_allow_html=True)
    st.markdown("<h4 style='text-align: center;'>Through the navigation sidebar, the various application functionalities can be accessed.</h4>", unsafe_allow_html=True)
    st.markdown("<h4 style='text-align: center;'>For documentation, code, and all other relevant files, see the <a href='https://github.com/mattflaherty97/case-2-team-3'>project repo</a>.</h4>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: left;'>Risk Assessment Tab</h3>", unsafe_allow_html=True)
    st.markdown("<h5 style='text-align: left;'>Allows for user input to assess loan default risk using a random forest classifier.</h5>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: left;'>Information Tab</h3>", unsafe_allow_html=True)
    st.markdown("<h5 style='text-align: left;'>Provides further information on modeling methodology and useful links for users regarding default risk factors.</h5>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: left;'>Updates Tab</h3>", unsafe_allow_html=True) 
    st.markdown("<h5 style='text-align: left;'>Details upcoming updates for the application.</h5>", unsafe_allow_html=True)    

# code for application page
if sidebar == 'Risk Assessment':

    # Page Header
    st.markdown("<h2 style='text-align: center;'>User Page</h2>", unsafe_allow_html=True)
        
    income = st.slider("Applicant Income:", 0, int(max(data['Income'])), step = 1, value = int(np.mean(data['Income'])))
    
    age = st.slider("Applicant Age:", 0, int(max(data['Age'])), step = 1, value = int(np.mean(data['Age'])))
    
    experience = st.slider("Applicant Work Experience (years):", 0, int(max(data['Experience'])), step = 1, value = int(np.mean(data['Experience'])))
    
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
    
    job_years = st.slider("Applicant Years at Current Job:", 0, int(max(data['CURRENT_JOB_YRS'])), step = 1, value = int(np.mean(data['CURRENT_JOB_YRS'])))
    
    house_years = st.slider("Applicant Years at Current Residence:", 0, int(max(data['CURRENT_HOUSE_YRS'])), step = 1, value = int(np.mean(data['CURRENT_HOUSE_YRS'])))
    
    GDP = st.slider("Applicant State GDP (billions):", 0, int(max(data['GDP'])), step = 1, value = int(np.mean(data['GDP'])))
    
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
    st.markdown("<h2 style='text-align: center;'>Information Page</h2>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center;'>Check back soon for additional functionality!</h3>", unsafe_allow_html=True)
    
# code for application page
if sidebar == 'Updates':

    # Page Header
    st.markdown("<h2 style='text-align: center;'>Updates Page</h2>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center;'>Check back soon for additional functionality!</h3>", unsafe_allow_html=True)