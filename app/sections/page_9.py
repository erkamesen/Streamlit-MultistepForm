import streamlit as st
from app.utils import check_email, decrease_stage, get_value


country_codes = {}


with open("countries.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        parts = line.strip().split(" ")
        if len(parts) == 2:
            country_name, country_code = parts
            country_codes[country_name] = country_code

country_list = list(country_codes.keys())
country_list.insert(0, "Choose Your Country")


def section_9():
    name_value = get_value("name", "")
    email_value = get_value("email", "")
    phone_value = get_value("phone", "")
    st.image(f"./app/assets/steps/{st.session_state.get('stage')+1}.png")
    st.header(":gray[Form 📝]", divider="rainbow")

    selected_country = st.selectbox('Select Country:', country_list, index=0)
    if selected_country != "Choose Your Country":

        name = st.text_input(
            label="Name:", placeholder="John Doe", value=name_value)
        if not phone_value:
            phone = st.text_input(
                label="Phone:", value=country_codes.get(selected_country))
        else:
            phone = st.text_input(
                label="Phone:", value=phone_value)
        email = st.text_input(
            label="E-posta:", placeholder="johndoe@mail.com", value=email_value)

        def submit():
            if not name:
                st.toast(
                    "Please enter your name..!"
                )
            elif not phone.startswith("+") or len(phone.replace(" ", "").strip()) < 8:
                st.toast(
                    "Please enter your phone number with Country Code!!!!")
            elif not check_email(email):
                st.toast("Please enter valid email..")
            else:
                st.session_state["stage"] += 1

        st.session_state["user"].update(
            {"user_form_choice": {"name": name, "email": email, "phone": phone, "country": selected_country}})
        col1, col2 = st.columns(2)
        col1.button("Back", on_click=decrease_stage,
                    type="primary", use_container_width=True)
        col2.button("Submit", on_click=submit,
                    type="secondary", use_container_width=True)
