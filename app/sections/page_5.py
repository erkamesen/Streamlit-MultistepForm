import streamlit as st
from app.utils import buttons
from streamlit_image_select import image_select


def section_5():
    st.image(f"./app/assets/steps/{st.session_state.get('stage')+1}.png")
    st.header(":gray[Treatment]", divider="rainbow")
    captions = ["Yes", "No"]
    i = image_select(
        label="Have you ever had a procedure such as hair transplantation?",
        images=[
            "./app/assets/man/page5/2.png",
            "./app/assets/man/page5/1.png",
        ],
        captions=captions,
        return_value="index"
    )
    st.session_state["user"].update({"any_treatment_choice": captions[i]})
    buttons()
