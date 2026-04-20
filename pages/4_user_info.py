import streamlit as st

if not st.session_state.active_user:
  st.warning("Please login to access this page!!")
else:
  st.subheader(f"Name {None}")
  st.subheader(f"Email {None}")
  st.subheader(f"Age {None}")
  
