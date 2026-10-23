import streamlit as st 
import pickle
import pandas as pd
import numpy as np




st.set_page_config(page_title="price predictor")

with open('df.pkl','rb') as file:
    df=pickle.load(file)

with open('pipeline.pkl','rb') as file:
    pipeline=pickle.load(file)   


st.title("Predictor")     

st.dataframe(df)    

st.header('Enter the information')

# property type
property_type=st.selectbox('Property Type',['flat','house'])

# sector 
sector=st.selectbox('Sector',sorted(df['sector'].unique().tolist()))

#bedroom
bedroom=float(st.selectbox('Number of Bedroom',sorted(df['bedRoom'].unique().tolist())))

# bathroom
bathroom=float(st.selectbox('Number of Bathroom',sorted(df['bathroom'].unique().tolist())))



balcony=st.selectbox('Number of Balconies',sorted(df['balcony'].unique().tolist()))

property_age = st.selectbox('Property Age',sorted(df['agePossession'].unique().tolist()))

built_up_area = st.number_input('Built Up Area in sq/ft', min_value=500.0, value=500.0,step=1.0)

servant_room = float(st.selectbox('Servant Room',[0.0, 1.0]))

store_room = float(st.selectbox('Store Room',[0.0, 1.0]))

furnishing_type = st.selectbox('Furnishing Type',sorted(df['furnishing_type'].unique().tolist()))
luxury_category = st.selectbox('Luxury Category',sorted(df['luxury_category'].unique().tolist()))
floor_category = st.selectbox('Floor Category',sorted(df['floor_category'].unique().tolist()))

if st.button('Predict'):

    # form a dataframe
    data = [[property_type, sector, bedroom, bathroom, balcony, property_age, built_up_area, servant_room, store_room, furnishing_type, luxury_category, floor_category]]
    columns = ['property_type', 'sector', 'bedRoom', 'bathroom', 'balcony',
               'agePossession', 'built_up_area', 'servant room', 'store room',
               'furnishing_type', 'luxury_category', 'floor_category']

    # Convert to DataFrame
    one_df = pd.DataFrame(data, columns=columns)

    #st.dataframe(one_df)

    # predict
    base_price = np.expm1(pipeline.predict(one_df))[0]
    low = base_price - 0.05
    high = base_price + 0.05

    # display
    st.markdown(f"<h4 style='color: blue;'>The price of the flat is between {round(low, 2)} Cr and {round(high, 2)} Cr</h4>", unsafe_allow_html=True)