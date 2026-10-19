import streamlit as st

st.set_page_config(
    page_title="Gurgaon Real Estate Analytics App",
    page_icon="👋",
)

st.title("Gurgaon Real Estate Analytics App")
st.write("Choose a tool to get started.")

st.page_link("pages/1_PricePredictor.py")
st.page_link("pages/2_AnalysisApp.py")