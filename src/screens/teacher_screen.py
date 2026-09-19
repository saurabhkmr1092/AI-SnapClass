import time
import streamlit as st
from src.ui.base_layout import style_background_dashboard, style_base_layout
from src.components.header import header_dashboard
from src.database.db import check_teacher_exists,create_teacher,teacher_login


def teacher_screen():
    style_background_dashboard()
    style_base_layout()
    
    if"teacher_data" in st.session_state:
        teacher_dashboard()

    elif 'teacher_login_type' not in st.session_state or st.session_state.teacher_login_type=='login':
        teacher_screen_login()

    elif st.session_state.teacher_login_type == "register":
        teacher_screen_register()



def teacher_dashboard():
    teacher_data = st.session_state.teacher_data
    st.header(f"""Welcome, {teacher_data['name']}""")


def login_teacher(username,password):
    teacher = teacher_login(username,password)

    if teacher:
        st.session_state.user_role = 'teacher'
        st.session_state.teacher_data = teacher
        st.session_state.is_logged_in = True
        return True
    return False



def teacher_screen_login():
    c1,c2 = st.columns(2, vertical_alignment='center', gap="xxlarge")
    with c1:
        header_dashboard()

    with c2:

        if st.button("Home", type='secondary', key='loginbackbtn',icon=":material/home:",shortcut=" control+backspace"):
            st.session_state['login_type'] = None
            st.rerun()

    st.header("Login using password",text_alignment="center")
    st.space()

    teacher_username = st.text_input("Enter username", placeholder='@saurabh')
    teacher_pass = st.text_input("Enter password",type="password",placeholder='Enter your password')

    st.divider()

    btnc1,btnc2 = st.columns(2)
    with btnc1:
        if st.button('Login',icon=":material/passkey:",shortcut=" control+Enter",width='stretch'):
            if login_teacher(teacher_username,teacher_pass):
                st.toast("Welcome back!", icon=":material/thumb_up:")
                time.sleep(2)
                st.rerun()
            else:
                st.error("Invalid username and password")    



    with btnc2:
        if st.button('Register',icon=":material/passkey:",width='stretch',type='primary'):
            st.session_state.teacher_login_type = 'register'
            st.rerun()



def register_teacher(teacher_username, teacher_name, teacher_pass, confirm_pass):
    if not teacher_username or not teacher_name or not teacher_pass:
        return False, "All fields are mandatory!"
    if check_teacher_exists(teacher_username):
        return False, "Username already taken"
    if teacher_pass != confirm_pass:
        return False, "Password doesn't match"

    try:
        create_teacher(teacher_username,teacher_pass,teacher_name)
        return True, "Registered Successfully! Login Now"
    except Exception as e:
        return False, "Unexpected error"
    


def teacher_screen_register():
    c1,c2 = st.columns(2, vertical_alignment='center', gap="xxlarge")
    with c1:
        header_dashboard()
    with c2:
        if st.button("Home", type='secondary', key='loginbackbtn',icon=":material/home:",shortcut=" control+backspace"):
            st.session_state['login_type'] = None
            st.rerun()

    st.header("Register your teacher profile")

    st.space()

    teacher_username = st.text_input("Enter username", placeholder='@saurabh')
    teacher_name = st.text_input("Enter name", placeholder='Saurabh Kumar')
    teacher_pass = st.text_input("Enter password",type="password",placeholder='Enter your password')
    confirm_pass = st.text_input("Confirm password",type="password",placeholder='Confirm your password')


    st.divider()

    btnc1,btnc2 = st.columns(2)
    with btnc1:
        if st.button('Register Now',icon=":material/passkey:",shortcut=" control+Enter",width='stretch',type='primary'):
            success, message = register_teacher(teacher_username, teacher_name, teacher_pass, confirm_pass)
            if success:
                st.success(message)
                time.sleep(2)
                st.session_state.teacher_login_type = "login"
                st.rerun()
            else:
                st.error(message)

    with btnc2:
        if st.button('Login',icon=":material/passkey:",width='stretch'):
            st.session_state.teacher_login_type = 'login'
            st.rerun()


