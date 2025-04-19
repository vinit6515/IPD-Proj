# import streamlit as st
# import os
# from dotenv import load_dotenv
# from langchain.prompts import PromptTemplate
# from langchain.chains import ConversationChain
# from langchain.chains.conversation.memory import ConversationBufferMemory
# from langchain_groq import ChatGroq
# import PyPDF2

# # Load environment variables
# load_dotenv()

# # Set your Groq API Key here (directly or from .env file)
# groq_api_key = "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"

# # Path to the PDF file
# pdf_path = "dentist.pdf"

# # Function to extract text from the PDF
# def extract_pdf_text(pdf_path):
#     text = ""
#     try:
#         with open(pdf_path, "rb") as pdf_file:
#             reader = PyPDF2.PdfReader(pdf_file)
#             for page in reader.pages:
#                 text += page.extract_text()
#     except FileNotFoundError:
#         text = "Error: PDF file not found!"
#     return text

# # Function to limit the size of the knowledge base to avoid token limit
# def limit_knowledge_base(knowledge_base, max_tokens=1000):
#     """Limit the size of the knowledge base."""
#     tokens = knowledge_base.split()  # Simplified tokenization by splitting by spaces
#     return ' '.join(tokens[:max_tokens])  # Limit to max_tokens

# # Load knowledge base from the PDF
# def load_knowledge_base():
#     """Load domain-specific knowledge from the PDF and limit size."""
#     pdf_content = extract_pdf_text(pdf_path)
#     if pdf_content.strip():
#         limited_content = limit_knowledge_base(pdf_content)
#         return limited_content
#     else:
#         return "No domain knowledge available."

# # Function to get AI Doctor's response based on the user's input
# def get_doctor_response(disease, severity, medical_history, follow_up):
#     llm = ChatGroq(api_key=groq_api_key, model="gemma2-9b-it")  # Groq model

#     # Load and limit the knowledge base to avoid large input
#     knowledge_base = load_knowledge_base()

#     # Add the knowledge base to the prompt
#     template = f"""
#     You are an experienced doctor specializing in dental care. Use the following domain knowledge to assist:
#     {knowledge_base}

#     Based on the following patient details:
#     - Disease: {{disease}}
#     - Severity: {{severity}}
#     - Medical History: {{medical_history}}
#     - Follow-up Details: {{follow_up}}

#     Provide a concise output including:
#     1. Medications
#     2. Health tips
#     3. Rest recommendations
#     4. Dietary guidance
#     """

#     prompt = PromptTemplate(
#         input_variables=["disease", "severity", "medical_history", "follow_up"],
#         template=template,
#     )

#     # Get the response from the Groq model
#     response = llm.predict(
#         prompt.format(
#             disease=disease,
#             severity=severity,
#             medical_history=medical_history,
#             follow_up=follow_up,
#         )
#     )
#     return response.strip()

# # Function to reset the conversation and start a new one
# def refresh_app():
#     st.session_state.clear()
#     st.experimental_set_query_params()  # Triggering a page rerun

# # Initialize or reset the session state
# if 'conversation' not in st.session_state:
#     st.session_state['conversation'] = [{"role": "bot", "text": "Hello, I am your AI Doctor. What problem or disease are you experiencing?"}]
# if 'history' not in st.session_state:
#     st.session_state['history'] = []
# if 'stage' not in st.session_state:
#     st.session_state['stage'] = 0
# if 'user_input' not in st.session_state:
#     st.session_state['user_input'] = ""

# # Streamlit setup
# st.set_page_config(page_title="AI Doctor Chatbot", page_icon="🤖", layout="centered")

# # Add custom CSS for chat-like design
# st.markdown(
#     """
#     <style>
#     body {
#         background-color: #f7f9fc;
#         color: #333333;
#         font-family: Arial, sans-serif;
#     }
#     .chat-box {
#         background-color: #ffffff;
#         border-radius: 8px;
#         padding: 20px;
#         margin-bottom: 16px;
#         box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.1);
#     }
#     .user-text {
#         text-align: left;
#         font-weight: bold;
#         color: #4CAF50;
#     }
#     .bot-text {
#         text-align: left;
#         color: #555555;
#         margin-bottom: 10px;
#     }
#     .stTextInput {
#         margin-top: 20px;
#         padding: 10px;
#         border: 1px solid #dddddd;
#         border-radius: 8px;
#     }
#     .stButton > button {
#         margin: 0 10px;
#         padding: 8px 16px;
#         font-size: 14px;
#         border-radius: 6px;
#     }
#     </style>
#     """,
#     unsafe_allow_html=True,
# )

# st.title("AI Doctor Chatbot 🤖")

# # Add chat-like interaction
# chat_placeholder = st.container()
# st.session_state.user_input = st.text_input(
#     "Enter your response:", st.session_state.user_input, key="input_box"
# )

# # Stage-based logic for conversation flow
# if st.session_state.stage == 0 and st.session_state.user_input:
#     st.session_state.disease = st.session_state.user_input
#     st.session_state.conversation.append({"role": "user", "text": st.session_state.user_input})
#     st.session_state.conversation.append({"role": "bot", "text": "How severe is your condition? (Mild, Moderate, Severe)"})
#     st.session_state.stage = 1
#     st.session_state.user_input = ""

# elif st.session_state.stage == 1 and st.session_state.user_input:
#     st.session_state.severity = st.session_state.user_input
#     st.session_state.conversation.append({"role": "user", "text": st.session_state.user_input})
#     st.session_state.conversation.append({"role": "bot", "text": "Do you have any relevant medical history?"})
#     st.session_state.stage = 2
#     st.session_state.user_input = ""

# elif st.session_state.stage == 2 and st.session_state.user_input:
#     st.session_state.medical_history = st.session_state.user_input
#     st.session_state.conversation.append({"role": "user", "text": st.session_state.user_input})
#     st.session_state.conversation.append({"role": "bot", "text": "Any other symptoms or follow-up details?"})
#     st.session_state.stage = 3
#     st.session_state.user_input = ""

# elif st.session_state.stage == 3 and st.session_state.user_input:
#     st.session_state.follow_up = st.session_state.user_input
#     st.session_state.conversation.append({"role": "user", "text": st.session_state.user_input})

#     # Generate response using Groq-based model
#     response = get_doctor_response(
#         st.session_state.disease,
#         st.session_state.severity,
#         st.session_state.medical_history,
#         st.session_state.follow_up,
#     )
#     st.session_state.conversation.append({"role": "bot", "text": response})

#     # Add to history
#     st.session_state.history.append(
#         {
#             "disease": st.session_state.disease,
#             "severity": st.session_state.severity,
#             "medical_history": st.session_state.medical_history,
#             "follow_up": st.session_state.follow_up,
#             "response": response,
#         }
#     )
#     st.session_state.stage = 0
#     st.session_state.user_input = ""

# # Display the chat
# with chat_placeholder:
#     for message in st.session_state.conversation:
#         if message["role"] == "user":
#             st.markdown(f'<div class="chat-box user-text">You: {message["text"]}</div>', unsafe_allow_html=True)
#         else:
#             st.markdown(f'<div class="chat-box bot-text">Doctor: {message["text"]}</div>', unsafe_allow_html=True)

# # Add button to view past history
# if st.button("View Past History"):
#     if st.session_state.history:
#         for idx, memory in enumerate(st.session_state.history):
#             st.markdown(f"**Case {idx + 1}:**")
#             st.markdown(f"- **Disease:** {memory['disease']}")
#             st.markdown(f"- **Severity:** {memory['severity']}")
#             st.markdown(f"- **Medical History:** {memory['medical_history']}")
#             st.markdown(f"- **Follow-Up Details:** {memory['follow_up']}")
#             st.markdown(f"- **Advice/Response:** {memory['response']}")
#             st.markdown("---")
#     else:
#         st.markdown("No history available yet.")

# # Option to restart the conversation
# if st.button("Start New Chat"):
#     refresh_app()





















# import streamlit as st
# import os
# from dotenv import load_dotenv
# from langchain.prompts import PromptTemplate
# from langchain.chains import ConversationChain
# from langchain.chains.conversation.memory import ConversationBufferMemory
# from langchain_groq import ChatGroq
# import PyPDF2

# # Load environment variables
# load_dotenv()

# # Set your Groq API Key here (directly or from .env file)
# groq_api_key = "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"

# # Path to the PDF file
# pdf_path = "dentist.pdf"

# # Function to extract text from the PDF
# def extract_pdf_text(pdf_path):
#     text = ""
#     try:
#         with open(pdf_path, "rb") as pdf_file:
#             reader = PyPDF2.PdfReader(pdf_file)
#             for page in reader.pages:
#                 text += page.extract_text()
#     except FileNotFoundError:
#         text = "Error: PDF file not found!"
#     return text

# # Load knowledge base from the PDF
# def load_knowledge_base():
#     """Load domain-specific knowledge from the PDF."""
#     pdf_content = extract_pdf_text(pdf_path)
#     if pdf_content.strip():
#         return pdf_content
#     else:
#         return "No domain knowledge available."

# # Function to get AI Doctor's response based on the user's input
# def get_doctor_response(disease, severity, medical_history, follow_up):
#     llm = ChatGroq(api_key=groq_api_key, model="gemma2-9b-it")  # Groq model

#     # Load the knowledge base
#     knowledge_base = load_knowledge_base()

#     # Add the knowledge base to the prompt
#     template = f"""
#     You are an experienced dentist. Use the following dental knowledge to assist:
#     {knowledge_base}

#     The following details are provided by the patient:
#     - Disease: {{disease}}
#     - Severity: {{severity}}
#     - Medical History: {{medical_history}}
#     - Follow-up Details: {{follow_up}}

#     Only provide answers related to dental care, treatment, and advice. If the problem is not dental-related, inform the patient that you can only provide dental advice.

#     Please give:
#     1. Dental medications or treatments
#     2. Health tips related to oral care
#     3. Rest recommendations for dental recovery
#     4. Dietary guidance specific to dental health
#     """

#     prompt = PromptTemplate(
#         input_variables=["disease", "severity", "medical_history", "follow_up"],
#         template=template,
#     )

#     # Get the response from the Groq model
#     response = llm.predict(
#         prompt.format(
#             disease=disease,
#             severity=severity,
#             medical_history=medical_history,
#             follow_up=follow_up,
#         )
#     )
#     return response.strip()

# # Function to reset the conversation and start a new one
# def refresh_app():
#     st.session_state.clear()
#     st.experimental_set_query_params()  # Triggering a page rerun

# # Initialize or reset the session state
# if 'conversation' not in st.session_state:
#     st.session_state['conversation'] = [{"role": "bot", "text": "Hello, I am your AI Dentist. What dental problem are you experiencing?"}]
# if 'history' not in st.session_state:
#     st.session_state['history'] = []
# if 'stage' not in st.session_state:
#     st.session_state['stage'] = 0
# if 'user_input' not in st.session_state:
#     st.session_state['user_input'] = ""

# # Streamlit setup
# st.set_page_config(page_title="AI Dentist Chatbot", page_icon="🦷", layout="centered")

# # Add custom CSS for a dentist specialist design
# st.markdown(
#     """
#     <style>
#     body {
#         background-color: #e0f7fa;
#         color: #005b6c;
#         font-family: 'Helvetica Neue', sans-serif;
#     }
#     .chat-box {
#         background-color: #ffffff;
#         border-radius: 8px;
#         padding: 20px;
#         margin-bottom: 16px;
#         box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
#     }
#     .user-text {
#         text-align: left;
#         font-weight: bold;
#         color: #00838f;
#     }
#     .bot-text {
#         text-align: left;
#         color: #00796b;
#         margin-bottom: 10px;
#     }
#     .stTextInput {
#         margin-top: 20px;
#         padding: 10px;
#         border: 1px solid #00796b;
#         border-radius: 8px;
#     }
#     .stButton > button {
#         margin: 0 10px;
#         padding: 10px 20px;
#         font-size: 14px;
#         border-radius: 6px;
#         background-color: #00796b;
#         color: white;
#     }
#     .stButton > button:hover {
#         background-color: #004d40;
#     }
#     .stTextInput > input {
#         border-radius: 6px;
#         border: 1px solid #00796b;
#     }
#     </style>
#     """,
#     unsafe_allow_html=True,
# )

# st.title("AI Dentist Chatbot 🦷")

# # Add chat-like interaction
# chat_placeholder = st.container()
# st.session_state.user_input = st.text_input(
#     "Enter your response:", st.session_state.user_input, key="input_box"
# )

# # Stage-based logic for conversation flow
# if st.session_state.stage == 0 and st.session_state.user_input:
#     st.session_state.disease = st.session_state.user_input
#     st.session_state.conversation.append({"role": "user", "text": st.session_state.user_input})
#     st.session_state.conversation.append({"role": "bot", "text": "How severe is your dental condition? (Mild, Moderate, Severe)"})
#     st.session_state.stage = 1
#     st.session_state.user_input = ""

# elif st.session_state.stage == 1 and st.session_state.user_input:
#     st.session_state.severity = st.session_state.user_input
#     st.session_state.conversation.append({"role": "user", "text": st.session_state.user_input})
#     st.session_state.conversation.append({"role": "bot", "text": "Do you have any relevant medical history?"})
#     st.session_state.stage = 2
#     st.session_state.user_input = ""

# elif st.session_state.stage == 2 and st.session_state.user_input:
#     st.session_state.medical_history = st.session_state.user_input
#     st.session_state.conversation.append({"role": "user", "text": st.session_state.user_input})
#     st.session_state.conversation.append({"role": "bot", "text": "Any other symptoms or follow-up details?"})
#     st.session_state.stage = 3
#     st.session_state.user_input = ""

# elif st.session_state.stage == 3 and st.session_state.user_input:
#     st.session_state.follow_up = st.session_state.user_input
#     st.session_state.conversation.append({"role": "user", "text": st.session_state.user_input})

#     # Generate response using Groq-based model
#     response = get_doctor_response(
#         st.session_state.disease,
#         st.session_state.severity,
#         st.session_state.medical_history,
#         st.session_state.follow_up,
#     )
#     st.session_state.conversation.append({"role": "bot", "text": response})

#     # Add to history
#     st.session_state.history.append(
#         {
#             "disease": st.session_state.disease,
#             "severity": st.session_state.severity,
#             "medical_history": st.session_state.medical_history,
#             "follow_up": st.session_state.follow_up,
#             "response": response,
#         }
#     )
#     st.session_state.stage = 0
#     st.session_state.user_input = ""

# # Display the chat
# with chat_placeholder:
#     for message in st.session_state.conversation:
#         if message["role"] == "user":
#             st.markdown(f'<div class="chat-box user-text">You: {message["text"]}</div>', unsafe_allow_html=True)
#         else:
#             st.markdown(f'<div class="chat-box bot-text">Dentist: {message["text"]}</div>', unsafe_allow_html=True)

# # Add button to view past history
# if st.button("View Past History"):
#     if st.session_state.history:
#         for idx, memory in enumerate(st.session_state.history):
#             st.markdown(f"**Case {idx + 1}:**")
#             st.markdown(f"- **Disease:** {memory['disease']}")
#             st.markdown(f"- **Severity:** {memory['severity']}")
#             st.markdown(f"- **Medical History:** {memory['medical_history']}")
#             st.markdown(f"- **Follow-Up Details:** {memory['follow_up']}")
#             st.markdown(f"- **Response:** {memory['response']}")
#             st.markdown("---")
#     else:
#         st.markdown("No history available yet.")
















# import streamlit as st
# import os
# from dotenv import load_dotenv
# from langchain.prompts import PromptTemplate
# from langchain.chains import ConversationChain
# from langchain.chains.conversation.memory import ConversationBufferMemory
# from langchain_groq import ChatGroq
# import PyPDF2

# # Load environment variables
# load_dotenv()

# # Set your Groq API Key here (directly or from .env file)
# groq_api_key = "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"

# # Path to the PDF file
# pdf_path = "dentist.pdf"

# # Function to extract text from the PDF
# def extract_pdf_text(pdf_path):
#     text = ""
#     try:
#         with open(pdf_path, "rb") as pdf_file:
#             reader = PyPDF2.PdfReader(pdf_file)
#             for page in reader.pages:
#                 text += page.extract_text()
#     except FileNotFoundError:
#         text = "Error: PDF file not found!"
    
#     # Limit text to a reasonable size to avoid token limit overflow
#     return text[:1000]  # Limit extracted text to 1000 characters

# # Load knowledge base from the PDF
# def load_knowledge_base():
#     """Load domain-specific knowledge from the PDF."""
#     pdf_content = extract_pdf_text(pdf_path)
#     if pdf_content.strip():
#         return pdf_content
#     else:
#         return "No domain knowledge available."

# # Function to get AI Doctor's response based on the user's input
# def get_doctor_response(disease, severity, medical_history, follow_up):
#     llm = ChatGroq(api_key=groq_api_key, model="gemma2-9b-it")  # Groq model

#     # Load the knowledge base
#     knowledge_base = load_knowledge_base()

#     # Add the knowledge base to the prompt
#     template = f"""
#     You are an only an experienced expert dentist. You are unable to suggest any advice other than dental problems. Use the following dental knowledge to assist:
#     {knowledge_base}

#     The following details are provided by the patient:
#     - Disease: {{disease}}
#     - Severity: {{severity}}
#     - Medical History: {{medical_history}}
#     - Follow-up Details: {{follow_up}}

#     Only provide answers related to dental care, treatment, and advice. If the problem is not dental-related, inform the patient that you can only provide dental advice.

#     Please give:
#     1. Dental medications or treatments
#     2. Health tips related to oral care
#     3. Rest recommendations for dental recovery
#     4. Dietary guidance specific to dental health
#     """

#     prompt = PromptTemplate(
#         input_variables=["disease", "severity", "medical_history", "follow_up"],
#         template=template,
#     )

#     # Get the response from the Groq model
#     response = llm.predict(
#         prompt.format(
#             disease=disease,
#             severity=severity,
#             medical_history=medical_history,
#             follow_up=follow_up,
#         )
#     )
#     return response.strip()

# # Function to reset the conversation and start a new one
# def refresh_app():
#     st.session_state.clear()
#     st.experimental_set_query_params()  # Triggering a page rerun

# # Initialize or reset the session state
# if 'conversation' not in st.session_state:
#     st.session_state['conversation'] = [{"role": "bot", "text": "Hello, I am your AI Dentist. What dental problem are you experiencing?"}]
# if 'history' not in st.session_state:
#     st.session_state['history'] = []
# if 'stage' not in st.session_state:
#     st.session_state['stage'] = 0
# if 'user_input' not in st.session_state:
#     st.session_state['user_input'] = ""

# # Streamlit setup
# st.set_page_config(page_title="AI Dentist Chatbot", page_icon="🦷", layout="centered")

# # Add custom CSS for a dentist specialist design
# st.markdown(
#     """
#     <style>
#     body {
#         background-color: #e0f7fa;
#         color: #005b6c;
#         font-family: 'Helvetica Neue', sans-serif;
#     }
#     .chat-box {
#         background-color: #ffffff;
#         border-radius: 8px;
#         padding: 20px;
#         margin-bottom: 16px;
#         box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
#     }
#     .user-text {
#         text-align: left;
#         font-weight: bold;
#         color: #00838f;
#     }
#     .bot-text {
#         text-align: left;
#         color: #00796b;
#         margin-bottom: 10px;
#     }
#     .stTextInput {
#         margin-top: 20px;
#         padding: 10px;
#         border: 1px solid #00796b;
#         border-radius: 8px;
#     }
#     .stButton > button {
#         margin: 0 10px;
#         padding: 10px 20px;
#         font-size: 14px;
#         border-radius: 6px;
#         background-color: #00796b;
#         color: white;
#     }
#     .stButton > button:hover {
#         background-color: #004d40;
#     }
#     .stTextInput > input {
#         border-radius: 6px;
#         border: 1px solid #00796b;
#     }
#     </style>
#     """,
#     unsafe_allow_html=True,
# )

# st.title("AI Dentist Chatbot 🦷")

# # Add chat-like interaction
# chat_placeholder = st.container()
# st.session_state.user_input = st.text_input(
#     "Enter your response:", st.session_state.user_input, key="input_box"
# )

# # Stage-based logic for conversation flow
# if st.session_state.stage == 0 and st.session_state.user_input:
#     st.session_state.disease = st.session_state.user_input
#     st.session_state.conversation.append({"role": "user", "text": st.session_state.user_input})
#     st.session_state.conversation.append({"role": "bot", "text": "How severe is your dental condition? (Mild, Moderate, Severe)"})
#     st.session_state.stage = 1
#     st.session_state.user_input = ""

# elif st.session_state.stage == 1 and st.session_state.user_input:
#     st.session_state.severity = st.session_state.user_input
#     st.session_state.conversation.append({"role": "user", "text": st.session_state.user_input})
#     st.session_state.conversation.append({"role": "bot", "text": "Do you have any relevant medical history?"})
#     st.session_state.stage = 2
#     st.session_state.user_input = ""

# elif st.session_state.stage == 2 and st.session_state.user_input:
#     st.session_state.medical_history = st.session_state.user_input
#     st.session_state.conversation.append({"role": "user", "text": st.session_state.user_input})
#     st.session_state.conversation.append({"role": "bot", "text": "Any other symptoms or follow-up details?"})
#     st.session_state.stage = 3
#     st.session_state.user_input = ""

# elif st.session_state.stage == 3 and st.session_state.user_input:
#     st.session_state.follow_up = st.session_state.user_input
#     st.session_state.conversation.append({"role": "user", "text": st.session_state.user_input})

#     # Generate response using Groq-based model
#     response = get_doctor_response(
#         st.session_state.disease,
#         st.session_state.severity,
#         st.session_state.medical_history,
#         st.session_state.follow_up,
#     )
#     st.session_state.conversation.append({"role": "bot", "text": response})

#     # Add to history
#     st.session_state.history.append(
#         {
#             "disease": st.session_state.disease,
#             "severity": st.session_state.severity,
#             "medical_history": st.session_state.medical_history,
#             "follow_up": st.session_state.follow_up,
#             "response": response,
#         }
#     )
#     st.session_state.stage = 0
#     st.session_state.user_input = ""

# # Display the chat
# with chat_placeholder:
#     for message in st.session_state.conversation:
#         if message["role"] == "user":
#             st.markdown(f'<div class="chat-box user-text">You: {message["text"]}</div>', unsafe_allow_html=True)
#         else:
#             st.markdown(f'<div class="chat-box bot-text">Dentist: {message["text"]}</div>', unsafe_allow_html=True)

# # Add button to view past history
# if st.button("View Past History"):
#     if st.session_state.history:
#         for idx, memory in enumerate(st.session_state.history):
#             st.markdown(f"**Case {idx + 1}:**")
#             st.markdown(f"- **Disease:** {memory['disease']}")
#             st.markdown(f"- **Severity:** {memory['severity']}")
#             st.markdown(f"- **Medical History:** {memory['medical_history']}")
#             st.markdown(f"- **Follow-Up Details:** {memory['follow_up']}")
#             st.markdown(f"- **Response:** {memory['response']}")
#             st.markdown("---")
#     else:
#         st.write("No history available.")



















import streamlit as st
import os
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain.chains import ConversationChain
from langchain.chains.conversation.memory import ConversationBufferMemory
from langchain_groq import ChatGroq
import PyPDF2

# Load environment variables
load_dotenv()

# Set your Groq API Key here (directly or from .env file)
groq_api_key = "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"

# Path to the PDF file
pdf_path = "dentist.pdf"

# Function to extract text from the PDF
def extract_pdf_text(pdf_path):
    text = ""
    try:
        with open(pdf_path, "rb") as pdf_file:
            reader = PyPDF2.PdfReader(pdf_file)
            for page in reader.pages:
                text += page.extract_text()
    except FileNotFoundError:
        text = "Error: PDF file not found!"
    return text[:1000]  # Limit extracted text to 1000 characters

# Load knowledge base from the PDF
def load_knowledge_base():
    pdf_content = extract_pdf_text(pdf_path)
    return pdf_content if pdf_content.strip() else "No domain knowledge available."

# Function to generate dynamic follow-up questions
def generate_question(stage, disease=None, severity=None, medical_history=None):
    llm = ChatGroq(api_key=groq_api_key, model="gemma2-9b-it")  # Groq model
    prompt = f"""
    You are an experienced dentist AI assistant. Based on the patient's details so far:
    - Disease: {disease or "Not specified"}
    - Severity: {severity or "Not specified"}
    - Medical History: {medical_history or "Not specified"}

    Generate the next most relevant question to gather additional details about the patient's dental condition.
    Only ask one question.
    """
    return llm.predict(prompt).strip()


# Function to get AI Dentist's response
def get_doctor_response(disease, severity, medical_history, follow_up):
    llm = ChatGroq(api_key=groq_api_key, model="gemma2-9b-it")
    knowledge_base = load_knowledge_base()
    
    template = f"""
    You are an only an experienced expert dentist. You are unable to suggest any advice other than dental problems. Use the following dental knowledge to assist:
    {knowledge_base}

    The following details are provided by the patient:
    - Disease: {{disease}}
    - Severity: {{severity}}
    - Medical History: {{medical_history}}
    - Follow-up Details: {{follow_up}}

    Only provide answers related to dental care, treatment, and advice. If the problem is not dental-related, inform the patient that you can only provide dental advice.

    Please give:
    1. Dental medications or treatments
    2. Health tips related to oral care
    3. Rest recommendations for dental recovery
    4. Dietary guidance specific to dental health
    """
    prompt = PromptTemplate(
        input_variables=["disease", "severity", "medical_history", "follow_up"],
        template=template,
    )
    response = llm.predict(
        prompt.format(
            disease=disease,
            severity=severity,
            medical_history=medical_history,
            follow_up=follow_up,
        )
    )
    return response.strip()

# Streamlit setup
st.set_page_config(page_title="AI Dentist Chatbot", page_icon="🦷", layout="centered")
st.markdown("""
    <style>
    body {
        background-color: #e0f7fa;
        color: #005b6c;
        font-family: 'Helvetica Neue', sans-serif;
    }
    .chat-box {
        background-color: #ffffff;
        border-radius: 8px;
        padding: 20px;
        margin-bottom: 16px;
        box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
    }
    .user-text {
        text-align: left;
        font-weight: bold;
        color: #00838f;
    }
    .bot-text {
        text-align: left;
        color: #00796b;
        margin-bottom: 10px;
    }
    .stTextInput {
        margin-top: 20px;
        padding: 10px;
        border: 1px solid #00796b;
        border-radius: 8px;
    }
    .stButton > button {
        margin: 0 10px;
        padding: 10px 20px;
        font-size: 14px;
        border-radius: 6px;
        background-color: #00796b;
        color: white;
    }
    .stButton > button:hover {
        background-color: #004d40;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("AI Dentist Chatbot 🦷")

# Initialize session states
if 'conversation' not in st.session_state:
    st.session_state['conversation'] = [{"role": "bot", "text": "Hello, I am your AI Dentist. What dental problem are you experiencing?"}]
if 'history' not in st.session_state:
    st.session_state['history'] = []
if 'stage' not in st.session_state:
    st.session_state['stage'] = 0
if 'user_input' not in st.session_state:
    st.session_state['user_input'] = ""

# Add chat-like interaction
chat_placeholder = st.container()
st.session_state.user_input = st.text_input("Enter your response:", st.session_state.user_input, key="input_box")

# Stage-based conversation flow
if st.session_state.stage == 0 and st.session_state.user_input:
    st.session_state.disease = st.session_state.user_input
    st.session_state.conversation.append({"role": "user", "text": st.session_state.user_input})
    next_question = generate_question(stage=1, disease=st.session_state.disease)
    st.session_state.conversation.append({"role": "bot", "text": next_question})
    st.session_state.stage = 1
    st.session_state.user_input = ""

elif st.session_state.stage == 1 and st.session_state.user_input:
    st.session_state.severity = st.session_state.user_input
    st.session_state.conversation.append({"role": "user", "text": st.session_state.user_input})
    next_question = generate_question(stage=2, disease=st.session_state.disease, severity=st.session_state.severity)
    st.session_state.conversation.append({"role": "bot", "text": next_question})
    st.session_state.stage = 2
    st.session_state.user_input = ""

elif st.session_state.stage == 2 and st.session_state.user_input:
    st.session_state.medical_history = st.session_state.user_input
    st.session_state.conversation.append({"role": "user", "text": st.session_state.user_input})
    next_question = generate_question(stage=3, disease=st.session_state.disease, severity=st.session_state.severity, medical_history=st.session_state.medical_history)
    st.session_state.conversation.append({"role": "bot", "text": next_question})
    st.session_state.stage = 3
    st.session_state.user_input = ""

elif st.session_state.stage == 3 and st.session_state.user_input:
    st.session_state.follow_up = st.session_state.user_input
    st.session_state.conversation.append({"role": "user", "text": st.session_state.user_input})
    response = get_doctor_response(
        st.session_state.disease,
        st.session_state.severity,
        st.session_state.medical_history,
        st.session_state.follow_up,
    )
    st.session_state.conversation.append({"role": "bot", "text": response})
    st.session_state.history.append({
        "disease": st.session_state.disease,
        "severity": st.session_state.severity,
        "medical_history": st.session_state.medical_history,
        "follow_up": st.session_state.follow_up,
        "response": response,
    })
    st.session_state.stage = 0
    st.session_state.user_input = ""

# Display chat
with chat_placeholder:
    for message in st.session_state.conversation:
        if message["role"] == "user":
            st.markdown(f'<div class="chat-box user-text">You: {message["text"]}</div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="chat-box bot-text">Dentist: {message["text"]}</div>', unsafe_allow_html=True)

# Button to view history
if st.button("View Past History"):
    if st.session_state.history:
        for idx, memory in enumerate(st.session_state.history):
            st.markdown(f"**Case {idx + 1}:**")
            st.markdown(f"- **Disease:** {memory['disease']}")
            st.markdown(f"- **Severity:** {memory['severity']}")
            st.markdown(f"- **Medical History:** {memory['medical_history']}")
            st.markdown(f"- **Follow-Up Details:** {memory['follow_up']}")
            st.markdown(f"- **Response:** {memory['response']}")
            st.markdown("---")
    else:
        st.write("No history available.")
