import streamlit as st
from datetime import date
import requests

st.title("Create New Account ")

email = st.text_input("Enter your email",placeholder="Only '@gmail.com' domain allowed!!")
name = st.text_input("Enter your name",placeholder="Eg. Tony Stark")
dob = st.date_input("Enter your date of birth",min_value=date(1926,1,1))
age = date.today().year - dob.year
st.write("Age: ",age)
password = st.text_input(f"Enter your password ",placeholder="Eg. Password@123",type="password")
st.caption("First letter must be *Upercase* and contains at least one *Character*, *Number*, *Special* character")


col1,col2 = st.columns([2,10],gap="xxsmall")
with col1:
    submit = st.button("Submit")

with col2:
    if st.button("Already have account?"):
        st.switch_page("pages/2_Login.py")


if submit:
    response = requests.post(
        url="https://your-app.onrender.com/register_user",            
        json={"email":email,"name":name,"age":age,"password":password}
        )

    result = response.json()

    if "message" in result:
        st.success(result["message"])
    elif "error" in result:
        st.error(result["error"])
    elif "detail" in result:
        for err in result["detail"]:
            st.error(err["msg"])
    else:
        st.write(result)
