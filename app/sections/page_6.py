import streamlit as st
from app.utils import buttons
from streamlit_image_select import image_select
from app.utils import get_text


def section_6():
    st.image(f"./app/assets/steps/{st.session_state.get('stage')+1}.png")
    st.header(f":gray[{get_text('Plan 📅')}]", divider="rainbow")
    captions = [get_text("Now"), get_text("in a month"), get_text("in 3 months"), get_text("not planned")]
    i = image_select(
        label=get_text("The best time for you is the best time for us 😊"),
        images=[
            "./app/assets/woman/page7/1.png",
            "./app/assets/woman/page7/3.png",
            "./app/assets/woman/page7/2.png",
            "./app/assets/woman/page6/2.png",
        ],
        captions=captions,
        return_value="index",
    )
    if i == 0:
        plan = "Now"
    elif i == 1:
        plan = "in a month"
    elif i == 2:
        plan = "in 3 months"
    else:
        plan = "not planned"
    st.session_state["user"].update({"plan_choice": plan})
    buttons()
