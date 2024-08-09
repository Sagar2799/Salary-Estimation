import streamlit as st
import pickle
import numpy as numpy


def load_model():
    with open('saved_steps.pkl', 'rb') as file:
      data = pickle.load(file)
    return data

data = load_model()

regressor = data["model"]
le_country = data["le_country"]
le_education = data["le_education"]

def show_preedict_page():
    st.title("Software Developer Salary Prdiction")


    st.write("""### We need sme information to predict the Salary""")