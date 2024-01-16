import streamlit as st
from streamlit_image_select import image_select
from app.utils import buttons
from app.utils import get_text


def section_3():
    st.image(f"./app/assets/steps/{st.session_state.get('stage')+1}.png")
    st.header(f":gray[{get_text('Hair Color 🎨')}]", divider="rainbow")
    captions = [get_text("Blond"), get_text("Brown"), get_text("Ginger"), get_text("Black")]
    i = image_select(
        label=get_text("Please select your hair colour.."),
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
    if i == 0:
        color = "Blond"
    elif i == 1:
        color = "Brown"
    elif i == 2:
        color = "Ginger"
    else:
        color = "Black"
        
    st.session_state.get("user").update({"hair_color_choice": color})
    buttons()
