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
    st.write(type(result))
    if "message" in result:
      st.write("Fahhaaaaa!!")
    st.subheader(f"Name {result['message']['name']}")
    st.subheader(f"Email {result["message"]["email"]}")
    st.subheader(f"Age {result["message"]["age"]}")
  except Exception as e:
     st.write(e)
