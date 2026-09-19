import streamlit as st
from src.ui.base_layout import style_background_dashboard,style_base_layout
from src.components.header import header_dashboard


def student_screen():
    style_background_dashboard()
    style_base_layout()

    c1,c2 = st.columns(2, gap="xxlarge",vertical_alignment='center')

    with c1:
        header_dashboard()
    with c2:
        if st.button("Home",shortcut="control+backspace",icon=":material/home:",type='secondary'):
            st.session_state['login_type'] = None
            st.rerun()

    st.header("Login with FaceID",text_alignment="center")
    st.space()

    st.camera_input("Position your face in the center")
    