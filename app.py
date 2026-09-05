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
import streamlit as st
from groq import Groq

# Set up the web page
st.set_page_config(page_title="My Custom AI Tool", page_icon="🤖")
st.title("🤖 My Live AI Assistant")
st.write("Ask your AI anything! Powered by Groq's super-fast cloud brain.")

# Securely grab your secret Groq API Key from Streamlit settings
if "GROQ_API_KEY" in st.secrets:
    client = Groq(api_key=st.secrets["GROQ_API_KEY"])
else:
    st.error("Please add your GROQ_API_KEY inside your Streamlit Advanced Secrets!")
    st.stop()

# Create the text input field
user_input = st.text_input("Ask your AI anything:", placeholder="Type your question here...")

if st.button("Generate AI Response"):
    if user_input:
        with st.spinner("Thinking..."):
            try:
                # Call Groq's smart, free llama model
                completion = client.chat.completions.create(
                    model="llama3-8b-8192",
                    messages=[{"role": "user", "content": user_input}],
                )
                
                # Show the real answer on screen
                st.success("AI Response:")
                st.write(completion.choices[0].message.content)
            except Exception as e:
                st.error(f"An error occurred: {e}")
    else:
        st.warning("Please type a message first!")




