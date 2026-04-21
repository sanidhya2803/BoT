import streamlit as st
import requests

st.title("🪪 User Information")
st.subheader("")

if "email" not in st.session_state:
  st.session_state.email = None

if not st.session_state.active_user:
  st.warning("Please login to access this page!!")
else:
  try:
    response = requests.get(
      url="https://bot-wylh.onrender.com/user_info",
      params = {"email":st.session_state.email}
    )

    result = response.json()
    
    if "message" in result:
      col1,col2 = st.columns(2,gap="small")
      col3,col4 = st.columns(2,gap="small")
      col5,col6 = st.columns(2,gap="small")
      with col1:
        st.code('print("Name")')
      with col2:
        st.code(result['message']['name'])
      with col3:
        st.code('print("Email")')
      with col4:
        st.code(result["message"]["email"])
      with col5:
        st.code('print("Age")')
      with col6:
        st.code(result["message"]["age"])
  except Exception as e:
     st.write(e)

update = st.button("Update")
if update:  
  name = None
  age = None  
  
  option = st.multiselect("Select the fields you want to update",["Name","Age"])
  
  if "Name" in option:
    name = st.text_input("Enter your Name",key="name")
  if "Age" in option:
    age = st.number_input("Enter your age",key="age")
  
  if st.button("Done"):
    response = requests.patch(
      url="https://bot-wylh.onrender.com/update_user",
      params = {"email":st.session_state.email},
      json = {"name":name,"age":age}
    )

    result = response.json()
    if "message" in result:
      st.success(result["message"])
    else:
      st.error("Any issue occured!!")
