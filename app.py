import os
import streamlit as st

# Automatically handle package installation
try:
    import groq
except ImportError:
    os.system("pip install groq")
    import groq

from groq import Groq

# Set up the web page layout
st.set_page_config(page_title="My Custom AI Tool", page_icon="🤖")
st.title("🤖 My Live AI Assistant")
st.write("Welcome! Type a message below to chat with my live cloud application.")

# Read securely from the system environment variable we just created!
YOUR_SECRET_KEY = os.environ.get("GROQ_API_KEY")

if not YOUR_SECRET_KEY:
    st.error("Missing system credentials. Please check the backend configuration vault.")
    st.stop()

# Create the main text box for chatting
user_input = st.text_input("Ask my AI anything:", placeholder="Type your question here...")

if st.button("Generate AI Response"):
    if user_input:
        with st.spinner("Thinking..."):
            try:
                # Link to the AI using the secure background key
                client = Groq(api_key=YOUR_SECRET_KEY)
                
                completion = client.chat.completions.create(
                    model="openai/gpt-oss-20b",
                    messages=[{"role": "user", "content": user_input}],
                )
                
                # Safely read and display the text response layout
                if hasattr(completion, 'choices') and completion.choices:
                    choice = completion.choices
                    if hasattr(choice, 'message'):
                        answer = choice.message.content
                    elif isinstance(choice, dict) and 'message' in choice:
                        answer = choice['message']['content']
                    else:
                        answer = str(choice)
                else:
                    answer = str(completion)
                
                st.success("AI Response:")
                st.write(answer)
                
            except Exception as e:
                st.error(f"❌ Connection failed: {e}")
    else:
        st.warning("⚠️ Please type a question or prompt first!")
