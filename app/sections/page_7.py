import streamlit as st
from app.utils import buttons


def section_7():
    st.image(f"./app/assets/steps/{st.session_state.get('stage')+1}.png")
    st.header(":gray[Medicines & Diseases 💊 (Optional)]", divider="rainbow")
    medicines = st.text_area("Medicines", placeholder="Medicines..")
    illness = st.text_area("Diseases", placeholder="Diseases..")
    st.session_state["user"].update(
        {"medicine_choice": {"medicines": medicines, "diseases": illness}})
    buttons()
