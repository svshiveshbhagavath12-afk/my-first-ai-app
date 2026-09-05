import os
import streamlit as st

try:
    import groq
except ImportError:
    os.system("pip install groq")
    import groq

from groq import Groq

st.set_page_config(page_title="My Custom AI Tool", page_icon="🤖")
st.title("🤖 My Live AI Assistant")
st.write("Ask your AI anything! Your cloud brain is now fully awake.")

# Safe mode: Reads from Streamlit's hidden vault
if "GROQ_API_KEY" in st.secrets:
    YOUR_SECRET_KEY = st.secrets["GROQ_API_KEY"]
else:
    st.error("Please add your GROQ_API_KEY inside your Streamlit Secrets box!")
    st.stop()

user_input = st.text_input("Ask your AI anything:", placeholder="Type your question here...")

if st.button("Generate AI Response"):
    if user_input:
        with st.spinner("Thinking..."):
            try:
                client = Groq(api_key=YOUR_SECRET_KEY)
                completion = client.chat.completions.create(
                    model="llama3-8b-8192",
                    messages=[{"role": "user", "content": user_input}],
                )
                st.success("AI Response:")
                st.write(completion.choices.message.content)
            except Exception as e:
                st.error(f"An error occurred: {e}")
    else:
        st.warning("Please type a message first!")
