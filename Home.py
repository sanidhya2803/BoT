import streamlit as st
import requests

st.set_page_config(
    page_icon="♾️",
    page_title="Bot",
    layout="centered",
    initial_sidebar_state="expanded"
)

if "active_user" not in st.session_state:
    st.session_state.active_user = False

if "user" not in st.session_state:
    st.session_state.user = None

st.markdown("""
<style>
/* Hide default multipage sidebar navigation */
[data-testid="stSidebarNav"] {
    display: none;
}
</style>
""", unsafe_allow_html=True)

st.title("♾️ Welcome to BoT")
st.caption("---")
st.subheader("✨ What you can do")

# Create 3 columns (grid row)

col1, col2, col3 = st.columns(3, gap="medium",)

with col1:
    st.button("💬 Chat", use_container_width=True)
    st.caption("Ask anything from AI",text_alignment="center")

with col2:
    st.button("📄 Upload File", use_container_width=True)
    st.caption("Analyze PDFs, CSVs",text_alignment="center")

with col3:
    st.button("📊 Insights", use_container_width=True)
    st.caption("Get data insights instantly",text_alignment="center")

# Second row
col4, col5, col6 = st.columns(3, gap="medium")

with col4:
    st.button("🧠 AI Help", use_container_width=True)
    st.caption("Smart suggestions",text_alignment="center")

with col5:
    st.button("⚡ Fast Response", use_container_width=True)
    st.caption("Quick answers",text_alignment="center")

with col6:
    st.button("🔒 Secure", use_container_width=True)
    st.caption("Your data is safe",text_alignment="center")
st.button("Get Started",width="stretch",icon="🚀")


st.caption("---")

# ---------------------ChatBot---------------------

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

col1,col2 = st.columns([10,1],gap="xxsmall")
with col1:
    user_input = st.chat_input("Enter your query...",disabled=not st.session_state.active_user)
with col2:
    upload_file = st.button("🔗",use_container_width="True",disabled= not st.session_state.active_user)

if upload_file:
    file = st.file_uploader("Upload your file",["txt","csv","xlsx","pdf","docs"])
    if file:
        response = requests.post(
            url="https://bot-wylh.onrender.com/file_upload",
            files={"file":(file.name, file, file.type)}
        )
        result = response.json()
      
if user_input:
    st.session_state.messages.append({
        "role":"user",
        "content":user_input
    })

    response = requests.post(
        url="https://bot-wylh.onrender.com/history_chat",
        json = {"messages":st.session_state.messages}
    )
    if response.text:
        result = response.json()
    else:
        st.error("Server is waking up, please try again in 30 seconds!")
        st.stop()
    
    if result.get("response"):
        bot_reply = result.get("response")
    elif result.get("error"):
        bot_reply = result.get("error")
    elif result.get("detail"):
        bot_reply = result.get("detail")[0]["msg"]
    else:
        bot_reply = "Something went wrong"
    
    st.session_state.messages.append({
        "role":"assistant",
        "content":bot_reply
    })
    
    st.rerun()



# col1,col2,col3 = st.columns([10,1,1],gap="small")
# with col1:
#     input = st.text_input("",label_visibility="collapsed",placeholder="Ask Anything...")
# with col2:
#     file = st.button("🔗")
# with col3:
#     send = st.button("➤",disabled=not input)

# if file:
#     st.file_uploader("",["pdf","csv","xlsx","doc","txt"])

# if send:
#     response = requests.post(
#         url="http://127.0.0.1:8000/chat",
#         json = {"message":input}
#     )

#     result = response.json()

#     st.write(result["message"])


# ---------------------SIDEBAR---------------------

col1,col2,col3 = st.sidebar.tabs(["⚡ Quick", "🎯 Guide", "⚙️ Info"])
with col1:    
    st.markdown("### ⚡ Quick Prompts")
    st.write("💬 Explain Python basics")
    st.write("📊 Give data insights")
    st.write("🧠 AI vs ML difference")
    st.write("✍️ Summarize text")
    st.write("📈 Business ideas")
    st.write("🧑‍💻 Debug my code")
with col2:
    st.markdown("### 🎯 How to Use")
    st.write("1. Type your question below")
    st.write("2. Use clear instructions")
    st.write("3. Upload file if needed")
    st.write("4. Try quick prompts")
    st.markdown("### 💡 Tips")
    st.write("✔ Ask specific questions")
    st.write("✔ Use keywords")
    st.write("✔ Keep it simple")
with col3:
    st.markdown("### ⚙️ Features")
    st.write("⚡ Fast responses")
    st.write("🧠 AI-powered answers")
    st.write("📂 File support")
    st.write("🔒 Secure usage")
    st.markdown("### ℹ️ About")
    st.write("This is a basic AI chatbot UI")
    st.write("Built using Streamlit")

st.sidebar.title("")

st.sidebar.caption("---")

col1,col2 = st.sidebar.columns([5,5],gap="small")


if not st.session_state.active_user:
    with col1:
        if st.button("Register",use_container_width=True):
            st.switch_page("pages/1_Register.py")
    with col2:
        if st.button("Login",use_container_width=True):
            st.switch_page("pages/2_Login.py")

else:
    if st.sidebar.button("Logout",use_container_width=True):
        st.session_state.active_user = False
        st.session_state.user = None

        st.rerun()
    

st.sidebar.caption("---")

if st.session_state.active_user:
    col1,col2,col3 = st.sidebar.columns([1,3,1],gap="xsmall")
    with col1:
        st.button("",icon="👤",use_container_width=True)
    with col2:
        st.button(st.session_state.user,use_container_width=True) 
    with col3:
        if st.button("",icon="⚙️",use_container_width=True):
            st.switch_page("pages/3_Settings.py")
