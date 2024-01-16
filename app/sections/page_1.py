import streamlit as st
from app.utils import increase_stage
from streamlit_image_select import image_select
from app.utils import get_text


def section_1():
    st.image(f"./app/assets/steps/{st.session_state.get('stage')+1}.png")
    st.header(f":gray[{get_text('Gender ⚥')}]", divider="rainbow")
    captions = [get_text("Man"), get_text("Woman")]
    st.markdown("""
                <style>
                .image.selected{
                    object-fit:contain;
                }
                </style>
                """, unsafe_allow_html=True)
    i = image_select(
        label=get_text("Please select your gender.."),
        images=[
            "./app/assets/1.jpg",
            "./app/assets/2.jpg",
        ],
        captions=captions,
        use_container_width=True,
        return_value="index",
    )
    if i == 0:
        gender = "Man"
    else:
        gender = "Woman"
    st.session_state["user"].update({"gender_choice": gender})
    _, col2 = st.columns(2)
    col2.button(label=get_text("Next"), use_container_width=True,
                type="primary", on_click=increase_stage)
