import streamlit as st
from app.sections import *
from dotenv import load_dotenv
import os
from app.pkg import Telebot, mail_sender
from app.models.models import Database
from streamlit_extras.customize_running import center_running
import time
from app.utils import images
import threading
load_dotenv()


def create_app():

    st.set_page_config(
        page_title="Esthetic Hair Turkey",
        page_icon="📝",
        layout="centered",
        initial_sidebar_state="collapsed",
    )

    TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
    CHAT_ID = os.getenv("CHAT_ID")
    logger = Telebot(token=TELEGRAM_TOKEN, chat_ids=[CHAT_ID, ])
    receiver_email = os.getenv("RECEIVER_EMAIL")
    ########### STAGE MANAGEMENT ###########

    if "stage" not in st.session_state:
        st.session_state["stage"] = 0

    if "user" not in st.session_state:
        st.session_state["user"] = {}

    ########### STAGE MANAGEMENT ###########
    if st.session_state["stage"] == 0:
        section_1()

    elif st.session_state["stage"] == 1:
        section_2()

    elif st.session_state["stage"] == 2:
        section_3()

    elif st.session_state["stage"] == 3:
        section_4()

    elif st.session_state["stage"] == 4:
        section_5()

    elif st.session_state["stage"] == 5:
        section_6()

    elif st.session_state["stage"] == 6:
        section_7()

    elif st.session_state["stage"] == 7:
        section_8()

    elif st.session_state["stage"] == 8:
        section_9()

    elif st.session_state["stage"] == 9:

        user = st.session_state.get("user")
        user_form = user.get('user_form_choice')
        name = user_form.get('name')
        email = user_form.get('email')
        phone = user_form.get('phone')
        country = user_form.get('country')
        gender = user.get('gender_choice')
        hair_type = user.get('hair_type_choice')
        hair_color = user.get('hair_color_choice')
        loss_time = user.get('loss_time_choice')
        any_treatment = user.get('any_treatment_choice')
        plan = user.get('plan_choice')
        medicines = user.get("medicine_choice").get("medicines")
        diseases = user.get("medicine_choice").get("diseases")
        image_list = user.get("upload_choice")
        message = f"""
        Name: {name}
        Email: {email}
        Phone: {phone}
        Country: {country}
        Gender: {gender}
        Hair Type: {hair_type}
        Hair Color: {hair_color}
        Loss Time: {loss_time}
        Any Treatment: {any_treatment}
        Plan: {plan}
        Medicines: {medicines}
        Diseases: {diseases}
        """
        with Database("contacts.sqlite3") as db:
            db.add("contacts", {
                "name": name,
                "email": email,
                "phone": phone,
                "country": country,
                "gender": gender,
                "hair_type": hair_type,
                "hair_color": hair_color,
                "loss_time": loss_time,
                "treatment": any_treatment,
                "plan": plan,
                "medicines": medicines,
                "diseases": diseases,
            })
        imgs = images(image_list)
        t1 = threading.Thread(target=logger.info, args=(message, ))
        t2 = threading.Thread(target=mail_sender, args=(
            receiver_email, name, phone, message, imgs))
        t1.start()
        t2.start()
        # logger.info(message)
        # mail_sender(receiver_email=receiver_email, name=name,
        #             phone=phone, body=message, imgs=imgs)
        center_running()
        time.sleep(1.5)
        section_10()

        t1.join()
        t2.join()

        st.session_state["stage"] = 0
