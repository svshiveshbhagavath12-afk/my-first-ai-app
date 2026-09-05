import os
import streamlit as st

# Force Streamlit to install the groq library automatically
try:
    import groq
except ImportError:
    os.system("pip install groq")
    import groq

from groq import Groq

# Set up the web page layout
st.set_page_config(page_title="My Custom AI Tool", page_icon="🤖")
st.title("🤖 My Live AI Assistant")
st.write("Ask your AI anything! Your cloud brain is now fully awake.")

#gsk_egpVYuVM6mE6LUi7WtQmWGdyb3FYmdQgYiLw5dawcZn6aMFN8lx!
YOUR_SECRET_KEY = "gsk_YOUR_KEY_HERE"  

# Create the text input field
user_input = st.text_input("Ask your AI anything:", placeholder="Type your question here...")

if st.button("Generate AI Response"):
    if user_input:
        with st.spinner("Thinking..."):
            try:
                # Link to Groq using your hardcoded key directly
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
