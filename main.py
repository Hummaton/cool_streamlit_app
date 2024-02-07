# Harjot Gill 
import streamlit as st
import base64
import pandas as pd
from matplotlib import pyplot as plt


def main():
    if 'data' not in st.session_state:
        st.session_state.data = []

    # Include CSS files
    def include_css(filename):
        with open(filename, 'r') as f:
            st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

    # Include page styling and header removal  CSS files
    # include_css('.style/page_style.css')
    include_css('.style/header_remove.css')


    # ******Body of the page*****
    # Title of the page
    title = "Nice Form"
    st.markdown(f"<center><h1 style='color: white;'>{title}</h1></center>", unsafe_allow_html=True)
    

    # Create a form
    with st.form(key='my_form'):
        # Add form elements
        col1, col2 = st.columns(2)
        first_name = col1.text_input("First Name")
        last_name = col2.text_input("Last Name") 
        fav_animal = st.selectbox("Pick your favorite animal", options=["Select an animal", "dog", "cat", "bird", "fish", "rabbit"])
        submit_button = st.form_submit_button(label='Submit')

    if submit_button:
        if fav_animal == "Select an animal" or first_name == "" or last_name == "":   #<-- If parameters not are filled 
            st.write("Invalid input")
        else:
            #Adding the data to the dataframe
            st.session_state.data.append({'First Name': first_name, 'Last Name': last_name, 'Favorite Animal': fav_animal})

        dataframe = pd.DataFrame(st.session_state.data)

        if not dataframe.empty:
            st.write(dataframe)

        

    # ******Sidebar of the page*****
    with st.sidebar:
        st.markdown("<center><h1> Graphs </h1></center>", unsafe_allow_html=True)
        st.selectbox("", options=["Select the type of graph", "Line", "Bar", "Pie"])

if __name__ == "__main__":
    main()












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