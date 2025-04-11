import streamlit as st
from huggingface_hub import InferenceClient


# Function to create InferenceClient dynamically based on model selection
def get_client(model_name):
    return InferenceClient(model_name)

# Chat response function
def respond(message, history, max_tokens, top_p, model_name):
    system_message = "You are a friendly Chatbot."
    client = get_client(model_name)

    messages = [{"role": "system", "content": system_message}]
    for user_msg, bot_msg in history:
        if user_msg:
            messages.append({"role": "user", "content": user_msg})
        if bot_msg:
            messages.append({"role": "assistant", "content": bot_msg})

    messages.append({"role": "user", "content": message})

    response = client.chat_completion(
        messages,
        max_tokens=max_tokens,
        top_p=top_p,
        stream=False,
    )

    return response.choices[0].message["content"]


# Streamlit UI
st.title("🤖 Chatbot")
st.markdown(
    "This is a simple chatbot application built with Streamlit and Hugging Face Inference API."
)

# Session state untuk menyimpan history chat
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Sidebar untuk konfigurasi
st.sidebar.title("Settings")
model_name = st.sidebar.selectbox(
    "Choose a Model",
    [
        "meta-llama/Meta-Llama-3-8B-Instruct",
        "mistralai/Mistral-7B-Instruct-v0.3",
        "HuggingFaceH4/zephyr-7b-beta",
        "microsoft/Phi-3.5-mini-instruct",
    ],
    index=0,
)

max_tokens = st.sidebar.slider("Max new tokens", 1, 2048, 512, 1)
top_p = st.sidebar.slider("Top-p (nucleus sampling)", 0.1, 1.0, 0.95, 0.05)

# Chat input dari user
user_input = st.chat_input("Ask anything...")

# Tampilkan chat history
for user_msg, bot_msg in st.session_state.chat_history:
    with st.chat_message("user"):
        st.markdown(user_msg)
    with st.chat_message("assistant"):
        st.markdown(bot_msg)

# Ketika ada input baru
if user_input:
    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):
        response = respond(
            user_input,
            st.session_state.chat_history,
            max_tokens,
            top_p,
            model_name,
        )
        st.markdown(response)

    # Simpan ke session state
    st.session_state.chat_history.append((user_input, response))
