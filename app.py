# -*- coding: utf-8 -*-
"""
Created on Tue Jan  3 00:55:10 2023

@author: Afroz
"""

import pandas as pd
import streamlit as st

from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report
st.set_option('deprecation.showPyplotGlobalUse', False)

st.markdown('Use this Streamlit app to make your own scatterplot about Iris Flower') 

# Import Data
st.title("Iris flower Classifier") 
Iris = pd.read_csv('Iris.csv')

st.title('Pandas Profiling of Iris Dataset')
Iris_profile = ProfileReport(Iris, explorative=True)
st_profile_report(Iris_profile)
