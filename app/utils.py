import streamlit as st
import base64
import re
import cv2
import numpy as np
import tempfile
import json


def increase_stage():
    st.session_state["stage"] += 1


def decrease_stage():
    st.session_state["stage"] -= 1


def buttons():
    col1, col2 = st.columns(2)
    col1.button(label=get_text("Back"), use_container_width=True,
                type="primary", on_click=decrease_stage)
    col2.button(label=get_text("Next"), use_container_width=True,
                type="primary", on_click=increase_stage)


def get_image(path):
    image = path
    file_ = open(image, "rb")
    contents = file_.read()
    data_url = base64.b64encode(contents).decode("utf-8")
    file_.close()
    return data_url


def check_email(email):
    if email:
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        if (re.fullmatch(regex, email)):
            return True

        else:
            return False


def get_value(primary, secondary):
    user = st.session_state["user"]
    try:
        return user.get("user_form_choice").get(primary, secondary)
    except AttributeError:
        pass


def images(image_list: list):
    response_list = []
    for uploaded in image_list:
        bytes_data = uploaded.read()
        cv2_img = cv2.imdecode(np.frombuffer(
            bytes_data, np.uint8), cv2.IMREAD_COLOR)
        with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as temp_img:
            temp_img_path = temp_img.name
            cv2.imwrite(temp_img_path, cv2_img)
            response_list.append(cv2_img)
    return response_list


def get_language_code():
    try:
        return st.experimental_get_query_params().get("language")[0]
    except:
        return 


def get_text(sentence):
    language = get_language_code()
    if not language or language == "en":
        return sentence
    else:
        with open("./app/language.json", "r") as f:
            content = json.load(f)
        resp = content.get(language).get(sentence)
        return resp
