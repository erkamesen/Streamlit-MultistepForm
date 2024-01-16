import streamlit as st
from app.utils import buttons
from streamlit_image_select import image_select


def section_4():
    st.image(f"./app/assets/steps/{st.session_state.get('stage')+1}.png")
    st.header(":gray[Hair Loss Time ⏲️]", divider="rainbow")
    captions = ["1 - 3 Years", "3 - 6 Years", "6 - 12+ Years"]
    i = image_select(
        label="Year..",
        images=[
            "./app/assets/man/page4/1.png",
            "./app/assets/man/page4/2.png",
            "./app/assets/man/page4/3.png",

        ],

        captions=captions,
        return_value="index"
    )
    st.session_state["user"].update({"loss_time_choice": captions[i]})
    buttons()
