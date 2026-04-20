import streamlit as st
import requests

st.title("🪪 User Information")

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
