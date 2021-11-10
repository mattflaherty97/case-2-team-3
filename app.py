# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 18:43:25 2021

@author: kingl
"""

import streamlit as st
import pandas as pd
import numpy as np
import janitor

# format app to fill screen width
st.set_page_config(layout="wide")

# set main title of application
st.markdown("<h1 style='text-align: center;'>Loan Default Dashboard</h1>", unsafe_allow_html=True)

# create sidebar with multiple options
sidebar = st.sidebar.selectbox("Navigation", ("Main", "User", "Government", "Other"))


train = pd.read_csv("Data/train_data.csv").clean_names()
# test = pd.read_csv("Data/test_data.csv").clean_names()
unique_professions = train['profession'].unique()
unique_cities = train['city'].unique()
unique_states = train['state'].unique()


# code for main page
if sidebar == 'Main':
        
    # Page Content
    st.markdown("<h2 style='text-align: center;'>Main Page</h2>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center;'>Through the navigation sidebar, the various application functionalities can be accessed.</h3>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center;'>For documentation, code, and all other relevant files, see the <a href='https://github.com/mattflaherty97/case-2-team-3'>project repo</a>.</h3>", unsafe_allow_html=True)
    #col1, col2, col3 = st.columns([1,1,1]) # this allows us to center the image by selecting col2 in next line
    #col2.image(vandy, use_column_width=True)

# code for application page
if sidebar == 'User':

    # Page Header
    st.markdown("<h2 style='text-align: center;'>User Page</h2>", unsafe_allow_html=True)
    
    user = st.selectbox("I am a:", ("Borrower", "Lender"))
    
    income = st.number_input("Applicant Income:", step = 1)
    
    age = st.number_input("Applicant Age:", step = 1)
    
    experience = st.number_input("Applicant Work Experience:", step = 1)
    
    marrital_status = st.selectbox("Applicant Marital Status:", ("Single", "Married"))
    
    house_ownership = st.selectbox("Applicant House Status:", ("None", "Rent", "Own"))
    
    profession = st.selectbox("Applicant Profession:", np.sort(unique_professions))
    
    city = st.selectbox("Applicant City:", np.sort(unique_cities))
    
    state = st.selectbox("Applicant State:", np.sort(unique_states))
    
    job_years = st.number_input("Applicant Years at Current Job:", step = 1)
    
    house_years = st.number_input("Applicant Years at Current Residence", step = 1)
    
    if st.button('Get Applicant Default Risk'):
        risk_score = np.random.rand()
        if risk_score < .33:
            st.success("Low-Risk Applicant!")
        if risk_score > .33 and risk_score < .66:
            st.warning("Moderate-Risk Applicant!")
        if risk_score > .66:
            st.error("High-Risk Applicant!")
    
# code for application page
if sidebar == 'Government':

    # Page Header
    st.markdown("<h2 style='text-align: center;'>Government Page</h2>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center;'>Check back soon for additional functionality!</h3>", unsafe_allow_html=True)
    
# code for application page
if sidebar == 'Other':

    # Page Header
    st.markdown("<h2 style='text-align: center;'>Other Page</h2>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center;'>Check back soon for additional functionality!</h3>", unsafe_allow_html=True)