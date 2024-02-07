import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def main():
    st.title('Data Collection App')

    # Initialize session state to store data
    if 'data' not in st.session_state:
        st.session_state.data = []

    # Check if form is submitted
    form_submitted = False
    if 'form_submitted' not in st.session_state:
        st.session_state.form_submitted = False

    # Create form if not submitted
    if not st.session_state.form_submitted:
        with st.form(key='my_form'):
            first_name = st.text_input(label='Enter your first name')
            last_name = st.text_input(label='Enter your last name')
            fav_animal = st.text_input(label='Enter your favorite animal')
            submit_button = st.form_submit_button(label='Submit')

        if submit_button:
            # Append data to session state
            st.session_state.data.append({'First Name': first_name, 'Last Name': last_name, 'Favorite Animal': fav_animal})
            st.write('Data submitted successfully!')
            st.session_state.form_submitted = True
            form_submitted = True

    # Convert session state data to DataFrame if form is submitted
    if form_submitted:
        dataframe = pd.DataFrame(st.session_state.data)

        # Hide the form
        st.empty()

        # Generate a plot
        x = np.linspace(0, 10, 100)
        y = np.sin(x)
        plt.plot(x, y)

        # Display the plot
        st.pyplot()

        # Show DataFrame
        st.write('Current Data:')
        st.write(dataframe)

if __name__ == '__main__':
    main()
