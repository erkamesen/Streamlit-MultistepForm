import streamlit as st
import time
from app.utils import get_text, get_language_code


def section_0():
    progress_text = get_text("Operation in progress. Please wait.")

    col1, col2 = st.columns(2)
    col1.image("./app/assets/man/9.sayfa/1.png")
    col2.title(get_text("Hair Transplantation Planning Consultation"))

    my_bar = col2.progress(0, text=progress_text)

    for percent_complete in range(100):
        time.sleep(0.02)
        my_bar.progress(percent_complete + 1, text=progress_text)
    my_bar.empty()
    st.session_state.get("user").update({"language_code":get_language_code()})
    st.session_state["stage"] += 1
    st.rerun()
