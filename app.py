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

# Grab the key directly from the browser web link
query_params = st.query_params
if "key" in query_params:
    YOUR_SECRET_KEY = query_params["key"]
else:
    st.info("💡 To turn on the brain, add your key to the end of your browser link above like this: /?key=gsk_yourkey")
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
