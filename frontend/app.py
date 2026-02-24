
import streamlit as st
import requests
import base64

st.title("🚢 Titanic Dataset Chat Agent")

if "messages" not in st.session_state:
    st.session_state.messages = []

user_input = st.chat_input("Ask something about Titanic...")

if user_input:

    st.session_state.messages.append(("user", user_input))
    response = requests.post(
        "https://titanic-chat-agent-xi4i.onrender.com/ask",
        json={"question": user_input}
    )

    data = response.json()

    st.session_state.messages.append(("bot", data))

for role, msg in st.session_state.messages:

    if role == "user":
        st.chat_message("user").write(msg)
    else:
        st.chat_message("assistant").write(msg["answer"])

        if msg["image"]:
            st.image(base64.b64decode(msg["image"]))

