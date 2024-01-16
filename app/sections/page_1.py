import streamlit as st
from app.utils import increase_stage
from streamlit_image_select import image_select


def section_1():
    st.image(f"./app/assets/steps/{st.session_state.get('stage')+1}.png")
    st.header(":gray[Gender ⚥]", divider="rainbow")
    captions = ["Man", "Woman"]
    st.markdown("""
                <style>
                .image.selected{
                    object-fit:contain;
                }
                </style>
                """, unsafe_allow_html=True)
    i = image_select(
        label="Please select your gender..",
        images=[
            "./app/assets/1.jpg",
            "./app/assets/2.jpg",
        ],
        captions=captions,
        use_container_width=True,
        return_value="index",
    )

    st.session_state["user"].update({"gender_choice": captions[i]})
    _, col2 = st.columns(2)
    col2.button(label="Next", use_container_width=True,
                type="primary", on_click=increase_stage)
