# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 03:32:31 2021

@author: Sanni Henry
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 03:32:31 2021

@author: Sanni Henry
"""

import numpy as np
import pickle
import pandas as pd
#from flasgger import Swagger
import streamlit as st 

from PIL import Image

#app=Flask(__name__)
#Swagger(app)

pickle_in = open("HClassifier.pkl","rb")
classifier=pickle.load(pickle_in)

#@app.route('/')
def welcome():
    return "Welcome All"

#@app.route('/predict',methods=["Get"])
def predict_note_authentication(Total_bilirubin,ALT,Alk_Phos,AST,GGT,Gender):
    
    """Let's Authenticate the Banks Note 
    This is using docstrings for specifications.
    ---
    parameters:  
      - name: Total_bilirubin
        in: query
        type: number
        required: true
      - name: ALT
        in: query
        type: number
        required: true
      - name: Alk_Phos
        in: query
        type: number
        required: true
      - name: AST
        in: query
        type: number
        required: true
      - name: GGT
        in: query
        type: number
        required: true
      - name: Gender
        in: query
        type: number
        required: true
    responses:
        200:
            description: The output values
        
    """
    
    prediction=classifier.predict([[Total_bilirubin,ALT,Alk_Phos,AST,GGT,Gender]])
    print(prediction)
    return prediction


def main():
    st.title("COVID 19 Prediction Software, (Hepatic Panel)")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Check your COVID 19 status today </h2>
    </div>

    <div style="background-color:tomato;padding:10px">
    <h3 style="color:yellow;text-align:left;">Result: </h3>
    </div>    

    <div style="background-color:tomato;padding:5px">
    <h4 style="color:yellow;text-align:left;">1-You have COVID 19 </h4>
    </div>    

    <div style="background-color:tomato;padding:5px">
    <h5 style="color:yellow;text-align:left;">0-You are free from the VIRUS </h5>
    </div>    
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    Total_bilirubin = st.text_input("Total_bilirubin","Type Here")
    ALT = st.text_input("ALT","Type Here")
    Alk_Phos = st.text_input("Alk_Phos","Type Here")
    AST = st.text_input("AST","Type Here")
    GGT = st.text_input("GGT","Type Here")
    Gender = st.text_input("Gender","input (1) for male and (0) for female")
    result=""
    if st.button("Predict"):
        result=predict_note_authentication(Total_bilirubin,ALT,Alk_Phos,AST,GGT,Gender)
    st.success('Your COVID 19 Chances {}'.format(result))
    if st.button("About"):
        st.text("Lets LEarn")
        st.text("Built by Henry")

if __name__=='__main__':
    main()
    
    
    