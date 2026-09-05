import streamlit as st

st.set_page_config(page_title="My First AI Tool", page_icon="🤖")
st.title("🤖 My First AI Assistant")
st.write("Welcome to your custom web app! Your interface is completely live.")

user_input = st.text_input("Ask your AI anything:", placeholder="Type a message here...")

if st.button("Send to AI"):
    if user_input:
        st.success(f"Success! Your interface works perfectly. It read your text: '{user_input}'")
    else:
        st.warning("Please type a message first!")




