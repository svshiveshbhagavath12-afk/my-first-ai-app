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
st.write("Welcome! Paste your Groq API key below to turn on the cloud brain.")

# 1. Create a password input box directly on the screen
user_key = st.text_input("Enter your Groq API Key (starts with gsk_):", type="password")

# 2. Create the main text box for chatting
user_input = st.text_input("Ask your AI anything:", placeholder="Type your question here...")

if st.button("Generate AI Response"):
    if not user_key:
        st.warning("⚠️ Please paste your Groq API key into the password box first!")
    elif not user_input:
        st.warning("⚠️ Please type a question or prompt first!")
    else:
        with st.spinner("Thinking..."):
            try:
                # Fire up the AI using the key provided on screen
                client = Groq(api_key=user_key.strip())
                
                # Using the fresh OpenAI/GPT-OSS model format
                completion = client.chat.completions.create(
                    model="openai/gpt-oss-20b",
                    messages=[{"role": "user", "content": user_input}],
                )
                
                # Safe unpack strategy that handles all response layouts perfectly
                if hasattr(completion, 'choices') and completion.choices:
                    choice = completion.choices[0]
                    if hasattr(choice, 'message'):
                        answer = choice.message.content
                    elif isinstance(choice, dict) and 'message' in choice:
                        answer = choice['message']['content']
                    else:
                        answer = str(choice)
                else:
                    answer = str(completion)
                
                # Display the successful answer
                st.success("AI Response:")
                st.write(answer)
                
            except Exception as e:
                st.error(f"❌ Connection failed: {e}")
