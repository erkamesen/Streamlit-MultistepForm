import streamlit as st
from app.utils import buttons
from streamlit_image_select import image_select
from app.utils import get_text


def section_4():
    st.image(f"./app/assets/steps/{st.session_state.get('stage')+1}.png")
    st.header(f":gray[{get_text('Hair Loss Time ⏲️')}]", divider="rainbow")
    captions = [get_text("1 - 3 Years"), get_text("3 - 6 Years"), get_text("6 - 12+ Years")]
    i = image_select(
        label=get_text("Year.."),
        images=[
            "./app/assets/man/page4/1.png",
            "./app/assets/man/page4/2.png",
            "./app/assets/man/page4/3.png",

        ],

        captions=captions,
        return_value="index"
    )
    if i == 0:
        year = "1 - 3 Years"
    elif i == 1:
        year = "3 - 6 Years"
    else:
        year = "6 - 12+ Years"
        
    st.session_state["user"].update({"loss_time_choice": year})
    buttons()
