#Write you name here!!!!!!!!!!!!!!!!!

import streamlit as st
import base64
import pandas as pd
from matplotlib import pyplot as plt

#Editing a default Streamlit theme via inspect element/markdowns, (removing header)
remove_header = """
<style>
.stDeployButton
    {
        visibility: hidden;
    }   
.st-emotion-cache-czk5ss.e16jpq800
    {
        visibility: hidden;
    }
[data-testid="stHeader"] {
    background-color: rgba(0, 0, 0, 0.0);
}
</style>            
"""
st.markdown(remove_header, unsafe_allow_html=True)

#Background image 
page_bg_img = """
    <style>
    [data-testid="stAppViewContainer"] {
    background-image: url("https://buffer.com/cdn-cgi/image/w=1000,fit=contain,q=90,f=auto/library/content/images/size/w300/2023/09/instagram-image-size.jpg");
    background-size: cover;
    }
    </style>
    """
st.markdown(page_bg_img, unsafe_allow_html=True)

#Title of the page
title = "EcoCAR Form"
st.markdown(f"<h1 style='text-align: center;'>{title}</h1>", unsafe_allow_html=True)
st.sidebar.title("Centered Sidebar")




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