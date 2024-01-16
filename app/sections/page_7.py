import streamlit as st
from app.utils import buttons
from app.utils import get_text


def section_7():
    st.image(f"./app/assets/steps/{st.session_state.get('stage')+1}.png")
    st.header(f":gray[{get_text('Medicines & Diseases 💊 (Optional)')}]", divider="rainbow")
    medicines = st.text_area(get_text("Medicines"), placeholder=get_text("Medicines"))
    illness = st.text_area(get_text("Diseases"), placeholder=get_text("Diseases"))
    st.session_state["user"].update(
        {"medicine_choice": {"medicines": medicines, "diseases": illness}})
    buttons()
