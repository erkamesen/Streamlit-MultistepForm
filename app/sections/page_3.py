import streamlit as st
from streamlit_image_select import image_select
from app.utils import buttons


def section_3():
    st.image(f"./app/assets/steps/{st.session_state.get('stage')+1}.png")
    st.header(":gray[Hair Color 🎨]", divider="rainbow")
    captions = ["Blond", "Brown", "Ginger", "Black"]
    i = image_select(
        label="Please select your hair colour..",
        images=[
            "./app/assets/man/page3/1.png",
            "./app/assets/man/page3/2.png",
            "./app/assets/man/page3/3.png",
            "./app/assets/man/page3/4.png",

        ],
        use_container_width=True,
        captions=captions,
        return_value="index"
    )
    st.session_state.get("user").update({"hair_color_choice": captions[i]})
    buttons()
