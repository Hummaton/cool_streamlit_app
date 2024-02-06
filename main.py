# Harjot Gill 
import streamlit as st
import base64
import pandas as pd
from matplotlib import pyplot as plt

#Background image and button coloring 
page_styling = """ 
    <style>
    [data-testid="stAppViewContainer"] {
    background-image: url("https://lh3.googleusercontent.com/fife/AGXqzDlKSA5a1hW-ljDjV1v-fHa_U-3EVvIrGhvdQkl4bxxIXLzPDMLkSGuv5_UbD8IP241VNaVGJywDd55fgn-DgkjYYJDnYBNvsOiql8sJ1IeCe2eLEOnbStyZaAakJulIqlEhZ5wzsMlGJS0Ing7XliTc4s-vDEPYDM7CBHWcWo2blYTnrngPI2chasWk3LKm6bkjUJg4VsMwoRZZ2qe4F5u8QPhtOozJX_wkWQRd6LDcaIUJ8AG9Y_g8UQ9s_f_JxNjDHTQd3O3P28IMl9jjpfglAPCiV_m0V9aEVJL6SJVSwSBBCkNTJYdeXSY3Q5CuqplMikGr_F4DqDYyRdZfZgOg4feCC6tRPdlZLZqwhusVkGGjLJ-ygZmqS1UrRGpiP2lIhwK0vPZAHF6MhOfZWSqSrO69aE5D2Pk6qVf-g4CL_abFqt64clHQgEgmKqnELEUTRAzGEjYx3kXcKXPAnwUWGZE3oXH43n1QoiiiCQ7mGYi3rTZ-iIa5KQ5-mSqclEw50iCC5S5zcopCQQSt4VJJ7M0JU3eN-z33HNLEbhzE8ybYDRS8eiOW_rXK7yrv9tISokgpLcmkgib6QAfFSGBDmgG3kR95Xkfz-VFUkjKumZWPSm9aMX55ucqGXGGLUPfGvFNRjhGCFcRIGpbvwbKDaxnODLTxkMewnK1QE5h44Rhm2iDzlEDzRYEoOoa8Hsh2J5NZoAvv1wYVeSQIQ-sP4m8Pj5hMzq8BjFG4eXpgMdR1xS7BgwHMcwswU9N8zPs3Pfus9m0F9MydSbP-thKhfBcxKlapvtxpe0GVy-gcoIuAhw-NDYe2eOTqNYonk3JlGIx6nT0jmRr3E5EdaWuSEq3iyzr8kJMVk33SU8xwsF0tUUW66kUYZqtdYUyXePktFgd2cJS0PdZcvaXQ7W0HyChRXisRePLjcacDUJmEF5_ELVmwMjFDPDiTlokJt2SgFdsuRIWy-EagPI83xRyGOCh25CWkrQalAmxCr264nNaqvNMwLM-NRiudFneryhwK_y6u9fpTpUbMpFvxKK_j8G0b_UZ2mnfz5lo-XQur7ID1CVus3CZ2RqnxYaD3pzQYSCu__ItdbfbQB_jB2qN5wZmIYattyGtcGQxDQw7gv4oiroV4SYHwf74-0_oOs7KkwcWTZsEBkUigoJygcVp3dXOgjt-dP0Ir65Sbwgppc3fxl9L1rlQfcH1oeN3EuAgOxMFhPE4EAlytZXdTE89tR7uUeP7VFqA2Xkjjj90IUZgueBgY9djgCKxDrhJPvc2P3C8SBAzfowTFr3uKsPQppJFbBTO4z5sexOR3muSP6tj_F0RVKz50DdpN8DYb5cg0wI97EvQoC5P9gdVAE0nq0k6_UgaD87Ypo-zmjNksAEkX6kwe9rG88JFmP7X9qtENIo7bX5v6iGetvwBvRfIc97gIAlbVLC4N0G9hzQGn1PoPYjwoJpRoCKYhbBgYZS3ov3H4cz64Eo_rj8WTP8RZmiejYn6-6brRYQFiAd7lebWThHqqCer-3RFkMqu68-k-orWpql4L32bd-iT7AXt-wNMMW4MT2eeVwhmAnfzK-QMb-xorcve7dOVjncNNebNMuLXDxI6dJ5mGBqs=w958-h893");
    background-size: cover;
    }

    # Figure this out!!!! 

    .st-ax input {
    background-color: white;
    }

    .stSelectbox div[data-baseweb="select"] > div:first-child {
            background-color: white;
            border-color: #2d408d;
        }

    .st-bb {
        color: black;
        background: snow;

        
    }

}
    </style>
    """
st.markdown(page_styling, unsafe_allow_html=True)



#Removing header)
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

# Title of the page
title = "EcoCAR Form"
st.markdown(f"<center><h1>{title}</h1></center>", unsafe_allow_html=True)

with st.sidebar:
    st.markdown("<center><h1>Centered Sidebar</h1></center>", unsafe_allow_html=True)



col1, col2 = st.columns(2)
col1.text_input("First Name")
col2.text_input("Last Name") 


select = st.selectbox("Pick your favorite animal", options=["Select an animal", "dog", "cat", "bird", "fish", "rabbit"])
submit_button = st.button("Submit")













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