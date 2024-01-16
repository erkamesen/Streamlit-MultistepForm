import streamlit as st
from app.utils import buttons
from streamlit_image_select import image_select
from app.utils import get_text


def section_5():
    st.image(f"./app/assets/steps/{st.session_state.get('stage')+1}.png")
    st.header(f":gray[{get_text('Treatment 💉')}]", divider="rainbow")
    captions = [get_text("Yes"), get_text("No")]
    i = image_select(
        label=get_text("Have you ever had a procedure such as hair transplantation?"),
        images=[
            "./app/assets/man/page5/2.png",
            "./app/assets/man/page5/1.png",
        ],
        captions=captions,
        return_value="index"
    )
    if i == 0:
        treatment = "Yes"
    else:
        treatment = "No"
    st.session_state["user"].update({"any_treatment_choice": treatment})
    buttons()
