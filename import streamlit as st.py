import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def main():
    st.title('Data Collection App')

    # Initialize session state to store data
    if 'data' not in st.session_state:
        st.session_state.data = []

    # Create form
    with st.form(key='my_form'):
        first_name = st.text_input(label='Enter your first name')
        last_name = st.text_input(label='Enter your last name')
        fav_animal = st.text_input(label='Enter your favorite animal')
        submit_button = st.form_submit_button(label='Submit')

    if submit_button:
        # Append data to session state
        st.session_state.data.append({'First Name': first_name, 'Last Name': last_name, 'Favorite Animal': fav_animal})
        st.write('Data submitted successfully!')

    # Convert session state data to DataFrame
    dataframe = pd.DataFrame(st.session_state.data)

    # Show DataFrame
    st.write('Current Data:')
    st.write(dataframe)

    # Create empty placeholder for plot
    plot_placeholder = st.empty()

    # Generate a plot
    x = np.linspace(0, 10, 100)
    y = np.sin(x)
    plt.plot(x, y)

    # Display the plot in the placeholder
    plot_placeholder.pyplot()

if __name__ == '__main__':
    main()
