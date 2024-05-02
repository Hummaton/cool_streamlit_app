# Harjot Gill 
import streamlit as st
import base64
import pandas as pd
from matplotlib import pyplot as plt

# Include CSS files
def include_css(filename):
    with open(filename, 'r') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

#Display graphs onto the screen in place of all the elements
def display_graph(option, dataframe):
    if option == "Line":
        plt.title("Favorite Animal Count (Line Graph)")
        plt.xlabel("Favorite Animal")
        plt.ylabel("Count")
        plt.grid(True)        
        plt.plot(dataframe)
        st.pyplot()
    elif option == "Bar":
        plt.title("Favorite Animal Count (Bar Graph)")
        plt.xlabel("Favorite Animal")
        plt.ylabel("Count")
        plt.bar(dataframe.index, dataframe)
        st.pyplot()
    elif option == "Pie":
        plt.title("Favorite Animal Count (Pie Chart)")
        plt.pie(dataframe, labels=dataframe.index, autopct='%1.1f%%')
        st.pyplot()
        

    
        

def main():
    if 'data' not in st.session_state:
        st.session_state.data = []

    # Include page styling and header removal  CSS files
    include_css('.style/header_remove.css')

    placeholder = st.empty()
    # ******Body of the page*****

    with placeholder.container():
        #Display the background image
        include_css('.style/page_style.css')
    
        # Title of the page
        title = "EcoCAR Form"
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
        graph_options = st.selectbox("", options=["Select the type of graph", "Line", "Bar", "Pie"])
    

    if graph_options != "Select the type of graph":
        fav_count_dataframe = dataframe['Favorite Animal'].value_counts()
        placeholder.empty()
        display_graph(graph_options, fav_count_dataframe)
    

if __name__ == "__main__":
    main()
