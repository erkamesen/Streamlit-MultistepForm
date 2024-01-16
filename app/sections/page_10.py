import streamlit as st
from app.utils import get_text


def section_10():
    st.balloons()
    st.header(get_text("Form Completed ✅"), divider="rainbow")
    st.write(get_text("Our team will contact you as soon as possible."))
    col1, col2 = st.columns(2)

    col1.image("./app/assets/man/page7/5.png", use_column_width=True)
    col2.write(get_text("You can follow us.."))
    c1, c2, c3 = col2.columns(3)

    c1.markdown("[![Test](https://www.infini.tw/wp-content/uploads/2020/03/instagram-icon-50x50.png)](https://instagram.com/esthetichairturkey/)")
    c2.markdown("[![Test](https://www.infini.tw/wp-content/uploads/2020/03/facebook-icon-50x50.png)](https://www.facebook.com/esthetichairturkey)")
    c3.markdown("[![Test](https://i0.wp.com/sancaseattle.org/wp-content/uploads/2019/03/youtube-circle-icon-50x50.png?fit=50%2C50&ssl=1)](https://www.youtube.com/esthetichairturkeyistanbul)")

