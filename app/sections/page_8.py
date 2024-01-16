import streamlit as st
from app.utils import buttons


def section_8():
    st.image(f"./app/assets/steps/{st.session_state.get('stage')+1}.png")
    st.header(":gray[Upload Pictures 📷 (Optional)]", divider="rainbow")
    files = st.file_uploader("Upload File", type=[
        "png", "jpg", "webp", "jpeg"],
        accept_multiple_files=True)
    if files:
        image_count = len(files)
        st.write(f"Number of Uploaded Files: {image_count}")

        cols = st.columns(6)
        for index, file in enumerate(files):
            cols[index].image(file)
    st.session_state["user"].update({"upload_choice": files})
    buttons()
