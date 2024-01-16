import streamlit as st
from app.utils import buttons
from streamlit_image_select import image_select


def section_6():
    st.image(f"./app/assets/steps/{st.session_state.get('stage')+1}.png")
    st.header(":gray[Plan 📅]", divider="rainbow")
    captions = ["Hemen", "in a month", "in 3 months", "not planned"]
    i = image_select(
        label="The best time for you is the best time for us 😊",
        images=[
            "./app/assets/woman/page7/1.png",
            "./app/assets/woman/page7/3.png",
            "./app/assets/woman/page7/2.png",
            "./app/assets/woman/page6/2.png",
        ],
        captions=captions,
        return_value="index",
    )
    st.session_state["user"].update({"plan_choice": captions[i]})
    buttons()
