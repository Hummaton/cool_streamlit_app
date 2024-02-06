# Harjot Gill 
import streamlit as st
import base64
import pandas as pd
from matplotlib import pyplot as plt

# Include CSS files
def include_css(filename):
    with open(filename, 'r') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Include page styling and header removal  CSS files
include_css('.style/page_style.css')
include_css('.style/header_remove.css')


# ******Body of the page*****
# Title of the page
title = "EcoCAR Form"
st.markdown(f"<center><h1 style='color: white;'>{title}</h1></center>", unsafe_allow_html=True)
 
#name input
col1, col2 = st.columns(2)
col1.text_input("First Name")
col2.text_input("Last Name") 

#animal selection
select = st.selectbox("Pick your favorite animal", options=["Select an animal", "dog", "cat", "bird", "fish", "rabbit"])
submit_button = st.button("Submit")

# dataframe logic 
"""   TODO:
    1. Create a dataframe with the following columns: 
        - Name
        - Animal
    2. Append the data to the dataframe 
    3. Display the dataframe on the page
"""


# ******Sidebar of the page*****
with st.sidebar:
    st.markdown("<center><h1> Graphs </h1></center>", unsafe_allow_html=True)
    st.selectbox("", options=["Select the type of graph", "Line", "Bar", "Pie"])














#Make sure any arrays/tables/dataframes aren't reseting everytime streamlit reruns

#Remove the header of the streamlit page 

#Keep any text centered

#Make sure the info is collected using a form

#Make the animal list anything you like as long as its list of things to track

#You can use any preferred libraries to produce the graphs

#You are welcome to make it better in any way as long as the main steps are kept the same (CHECK THE RUBRIC IN THE DOC)

#Use the image "photo.jpg" for the background

#Save the code as "main.py" put it on a folder name "[Your Name] Streamlit Test"
#Transfer it into a zip file then email the zip folder to airtija@ucdavis.edu and CC upmorgan@ucdavis.edu