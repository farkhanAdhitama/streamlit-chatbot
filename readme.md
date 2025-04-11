# 🤖 Chatbot Streamlit

This is a simple chatbot application built with Streamlit and the Hugging Face Inference API. It allows users to interact with various open-source Large Language Models (LLMs) through a friendly and intuitive interface.

## ✨ Features

- **Multiple Model Support**  
  Choose from a variety of open-source LLMs, including:

  - meta-llama/Meta-Llama-3-8B-Instruct
  - mistralai/Mistral-7B-Instruct-v0.3
  - HuggingFaceH4/zephyr-7b-beta
  - microsoft/Phi-3.5-mini-instruct

- **Customizable Settings**

  - Set the maximum number of tokens for the model's response.
  - Adjust the top-p value for nucleus sampling.

- **Chat History**  
  View your entire conversation history directly in the app.

## ⚙️ How It Works

1. Chat Input  
   Users type questions or commands into the input box.

2. Model Response  
   The app sends the user input and chat history to the selected model via the Hugging Face Inference API.

3. Chat Display  
   The conversation is displayed in a chat-like interface, alternating between user messages and model responses.

## 🛠️ Installation

1. Clone the repository:
   git clone <repository-url>
   cd chatbot-streamlit

2. Create and activate a virtual environment:
   python -m venv venv
   source venv/bin/activate # On Windows: venv\Scripts\activate

3. Install dependencies:
   pip install -r requirements.txt

## 🚀 Usage

Run the Streamlit app:
streamlit run app.py

Open the app in your browser (localhost)

Use the sidebar to:

- Select a model to use.
- Configure the maximum token count and top-p value.
- Type your message and chat with the chatbot.

## 📁 Project Structure

```
chatbot-streamlit/  
├── app.py # Main Streamlit file (UI + chatbot logic)  
├── requirements.txt # List of Python dependencies  
└── .gitignore # Files and folders ignored by Git
```
