import streamlit as st 
import pickle

st.set_page_config(page_title="Viz Demo")

with open('df.pkl','rb') as file:
    df=pickle.load(file)

st.dataframe(df)    

st.header('Enter the information')

# property type
property_type=st.selectbox('Property Type',['flat','house'])

# sector 
sector=st.selectbox('Sector',sorted(df['sector'].unique().tolist()))
