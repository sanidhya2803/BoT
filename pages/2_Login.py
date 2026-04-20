import streamlit as st
import requests

st.title("User Login")

email = st.text_input("Enter your email",placeholder="Eg. user123@gmail.com")
password = st.text_input("Enter your password",placeholder="Eg. Password@1234")

col1,col2 = st.columns([2,10],gap="xxsmall")
valid = False
if email and password:
    valid = True

flag = False
with col1:
    if st.button("Submit",disabled=not valid):

        response = requests.post(
            url="https://bot-wylh.onrender.com/login_user",
            json = {"email":email,"password":password}
        )

        if response.text:
            result = response.json()
            flag = True
        else:
            st.error("Server is waking up, please try again in 30 seconds!")
            st.stop()
    
    

with col2:
    if st.button("Don't have account?"):
        st.switch_page("pages/1_Register.py")

if flag:
    if "user" in result:    
        st.success(f"Hello {result["user"]["name"]}")

        st.session_state.user = result["user"]["name"]
        st.session_state.age = result["user"]["age"]
        st.session_state.active_user = True
    elif "error" in result:
        st.error(result["error"])
    elif "detail" in result:
        st.error(result["detail"][0]["msg"])
