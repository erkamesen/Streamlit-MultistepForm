import streamlit as st
from streamlit_image_select import image_select
from app.utils import buttons
from app.utils import get_text


def section_2():
    st.image(f"./app/assets/steps/{st.session_state.get('stage')+1}.png")
    st.header(f":gray[{get_text('Hair Type 🦱')}]", divider="rainbow")
    gender = st.session_state.get("user").get("gender_choice")
    captions = ["0", "1", "2", "3", "4", "5"]
    i = image_select(
        label=get_text("The parts of your hair that are falling out will help us to make a faster consultation.."),
        images=[
            f"./app/assets/{gender.lower()}/page2/1.png",
            f"./app/assets/{gender.lower()}/page2/2.png",
            f"./app/assets/{gender.lower()}/page2/3.png",
            f"./app/assets/{gender.lower()}/page2/4.png",
            f"./app/assets/{gender.lower()}/page2/5.png",
            f"./app/assets/{gender.lower()}/page2/6.png",
        ],
        use_container_width=True,
        captions=captions,
        key=0,
        return_value="index"
    )
    st.session_state.get("user").update({"hair_type_choice": captions[i]})
    buttons()
