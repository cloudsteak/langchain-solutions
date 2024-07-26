import streamlit as st
import langchain_helper


st.title("Make my Restaurant")
cuisine = st.sidebar.selectbox('Pick a Cuisine', ('Hungarian','Italian', 'Japanese', 'Mexican', 'Chinese', 'Indian', 'French', 'Thai', 'Greek', 'Turkish', 'Spanish', 'Vietnamese', 'Korean', 'Lebanese', 'Moroccan', 'Ethiopian', 'Peruvian', 'Brazilian', 'Argentinian', 'Russian', 'German', 'Austrian'))





if cuisine:
    response = langchain_helper.generate_restaurant_name_and_items(cuisine) 
    st.header(response["restaurant_name"].strip()) 
    menu_items = response['menu_items'].strip().split(",")
    st.write("**Special Menu for Today**")
    for item in menu_items:
        st.write("-", item)
