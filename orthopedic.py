# import streamlit as st
# import os
# from dotenv import load_dotenv
# from langchain.prompts import PromptTemplate
# from langchain.chains.conversation.memory import ConversationBufferMemory
# from langchain_groq import ChatGroq

# # Load environment variables
# load_dotenv()

# # Set your Groq API Key here
# groq_api_key = "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"

# # Function to get AI Orthopaedic Doctor's response
# def get_doctor_response(disease, severity, medical_history, follow_up):
#     llm = ChatGroq(api_key=groq_api_key, model="gemma2-9b-it")  # Groq model
#     template = """
#     You are an experienced orthopaedic doctor. Based on the following patient details:
#     - Disease: {disease}
#     - Severity: {severity}
#     - Medical History: {medical_history}
#     - Follow-up Details: {follow_up}

#     Provide:
#     1. Orthopaedic medications
#     2. Health tips specific to bone and joint care
#     3. Rest and recovery recommendations
#     4. Dietary guidance for bone health
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

# # Define a function to reset the conversation and start a new one
# def refresh_app():
#     st.session_state.clear()
#     st.experimental_set_query_params()

# # Initialize or reset the session state
# if 'conversation' not in st.session_state:
#     st.session_state['conversation'] = [{"role": "bot", "text": "Hello, I am your AI Orthopaedic Doctor. What bone or joint problem are you experiencing?"}]
# if 'history' not in st.session_state:
#     st.session_state['history'] = []
# if 'stage' not in st.session_state:
#     st.session_state['stage'] = 0
# if 'user_input' not in st.session_state:
#     st.session_state['user_input'] = ""

# # Streamlit setup
# st.set_page_config(page_title="AI Orthopaedic Doctor Chatbot", page_icon="🦴", layout="centered")

# # Add custom CSS for orthopaedic design
# st.markdown(
#     """
#     <style>
#     body {
#         background-color: #f5f5f5;
#         color: #333333;
#         font-family: 'Arial', sans-serif;
#     }
#     .chat-box {
#         background-color: #ffffff;
#         border: 2px solid #87CEEB;
#         border-radius: 10px;
#         padding: 20px;
#         margin-bottom: 20px;
#         box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
#     }
#     .user-text {
#         font-weight: bold;
#         color: #4682B4;
#     }
#     .bot-text {
#         color: #00688B;
#     }
#     .stTextInput {
#         margin-top: 20px;
#         padding: 10px;
#         border: 2px solid #4682B4;
#         border-radius: 10px;
#     }
#     .stButton > button {
#         margin: 10px 0;
#         padding: 12px 24px;
#         font-size: 16px;
#         border-radius: 8px;
#         background-color: #4682B4;
#         color: white;
#         border: none;
#     }
#     .stButton > button:hover {
#         background-color: #5A9BD6;
#     }
#     </style>
#     """,
#     unsafe_allow_html=True,
# )

# st.title("AI Orthopaedic Doctor Chatbot 🦴")

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
#     st.session_state.conversation.append({"role": "bot", "text": "Do you have any relevant medical history related to bones or joints?"})
#     st.session_state.stage = 2
#     st.session_state.user_input = ""

# elif st.session_state.stage == 2 and st.session_state.user_input:
#     st.session_state.medical_history = st.session_state.user_input
#     st.session_state.conversation.append({"role": "user", "text": st.session_state.user_input})
#     st.session_state.conversation.append({"role": "bot", "text": "Any other symptoms or details you'd like to share?"})
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
#             st.markdown(f'<div class="chat-box bot-text">Orthopaedic Doctor: {message["text"]}</div>', unsafe_allow_html=True)

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











# import streamlit as st
# import os
# from dotenv import load_dotenv
# from langchain.prompts import PromptTemplate
# from langchain_groq import ChatGroq

# # Load environment variables
# load_dotenv()

# # Set your Groq API Key here (directly or from .env file)
# groq_api_key = "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"

# # Function to dynamically generate follow-up questions
# def generate_question(stage, disease=None, severity=None, medical_history=None):
#     llm = ChatGroq(api_key=groq_api_key, model="gemma2-9b-it")  # Groq model
#     prompt = f"""
#     You are an experienced orthopaedic doctor AI assistant. Based on the patient's details so far:
#     - Bone or Joint Problem: {disease or "Not specified"}
#     - Severity: {severity or "Not specified"}
#     - Medical History: {medical_history or "Not specified"}

#     Generate the next most relevant question to gather additional details about the patient's bone or joint condition.
#     Only ask one question.
#     """
#     return llm.predict(prompt).strip()

# # Function to get AI Orthopaedic Doctor's response
# def get_doctor_response(disease, severity, medical_history, follow_up):
#     llm = ChatGroq(api_key=groq_api_key, model="gemma2-9b-it")
#     template = """
#     You are an experienced orthopaedic doctor. Based on the following patient details:
#     - Bone or Joint Problem: {disease}
#     - Severity: {severity}
#     - Medical History: {medical_history}
#     - Follow-up Details: {follow_up}

#     Provide a concise output including:
#     1. Recommended medications for orthopaedic issues
#     2. Bone/joint-specific health tips
#     3. Rest and recovery suggestions
#     4. Dietary guidance for bone health
#     """
    
#     prompt = PromptTemplate(
#         input_variables=["disease", "severity", "medical_history", "follow_up"],
#         template=template,
#     )
#     response = llm.predict(
#         prompt.format(
#             disease=disease,
#             severity=severity,
#             medical_history=medical_history,
#             follow_up=follow_up,
#         )
#     )
#     return response.strip()

# # Streamlit setup
# st.set_page_config(page_title="AI Orthopaedic Doctor Chatbot", page_icon="🦴", layout="centered")
# st.markdown("""
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
#         color: #1E90FF;
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
#     """, unsafe_allow_html=True)

# st.title("AI Orthopaedic Doctor Chatbot 🦴")

# # Initialize session states
# if 'conversation' not in st.session_state:
#     st.session_state['conversation'] = [{"role": "bot", "text": "Hello, I am your AI Orthopaedic Doctor. What bone or joint problem are you experiencing?"}]
# if 'history' not in st.session_state:
#     st.session_state['history'] = []
# if 'stage' not in st.session_state:
#     st.session_state['stage'] = 0
# if 'user_input' not in st.session_state:
#     st.session_state['user_input'] = ""

# # Chat-like interaction
# chat_placeholder = st.container()
# st.session_state.user_input = st.text_input("Enter your response:", st.session_state.user_input, key="input_box")

# # Stage-based conversation flow
# if st.session_state.stage == 0 and st.session_state.user_input:
#     st.session_state.disease = st.session_state.user_input
#     st.session_state.conversation.append({"role": "user", "text": st.session_state.user_input})
#     next_question = generate_question(stage=1, disease=st.session_state.disease)
#     st.session_state.conversation.append({"role": "bot", "text": next_question})
#     st.session_state.stage = 1
#     st.session_state.user_input = ""

# elif st.session_state.stage == 1 and st.session_state.user_input:
#     st.session_state.severity = st.session_state.user_input
#     st.session_state.conversation.append({"role": "user", "text": st.session_state.user_input})
#     next_question = generate_question(stage=2, disease=st.session_state.disease, severity=st.session_state.severity)
#     st.session_state.conversation.append({"role": "bot", "text": next_question})
#     st.session_state.stage = 2
#     st.session_state.user_input = ""

# elif st.session_state.stage == 2 and st.session_state.user_input:
#     st.session_state.medical_history = st.session_state.user_input
#     st.session_state.conversation.append({"role": "user", "text": st.session_state.user_input})
#     next_question = generate_question(stage=3, disease=st.session_state.disease, severity=st.session_state.severity, medical_history=st.session_state.medical_history)
#     st.session_state.conversation.append({"role": "bot", "text": next_question})
#     st.session_state.stage = 3
#     st.session_state.user_input = ""

# elif st.session_state.stage == 3 and st.session_state.user_input:
#     st.session_state.follow_up = st.session_state.user_input
#     st.session_state.conversation.append({"role": "user", "text": st.session_state.user_input})
#     response = get_doctor_response(
#         st.session_state.disease,
#         st.session_state.severity,
#         st.session_state.medical_history,
#         st.session_state.follow_up,
#     )
#     st.session_state.conversation.append({"role": "bot", "text": response})
#     st.session_state.history.append({
#         "disease": st.session_state.disease,
#         "severity": st.session_state.severity,
#         "medical_history": st.session_state.medical_history,
#         "follow_up": st.session_state.follow_up,
#         "response": response,
#     })
#     st.session_state.stage = 0
#     st.session_state.user_input = ""

# # Display chat
# with chat_placeholder:
#     for message in st.session_state.conversation:
#         if message["role"] == "user":
#             st.markdown(f'<div class="chat-box user-text">You: {message["text"]}</div>', unsafe_allow_html=True)
#         else:
#             st.markdown(f'<div class="chat-box bot-text">Orthopaedic Doctor: {message["text"]}</div>', unsafe_allow_html=True)

# # Button to view history
# if st.button("View Past History"):
#     if st.session_state.history:
#         for idx, memory in enumerate(st.session_state.history):
#             st.markdown(f"**Case {idx + 1}:**")
#             st.markdown(f"- **Bone/Joint Problem:** {memory['disease']}")
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
from langchain_groq import ChatGroq

# Load environment variables
load_dotenv()

# Set your Groq API Key here (directly or from .env file)
groq_api_key = "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"

# Function to dynamically generate follow-up questions
def generate_question(stage, disease=None, severity=None, medical_history=None):
    llm = ChatGroq(api_key=groq_api_key, model="gemma2-9b-it")  # Groq model
    prompt = f"""
    You are an experienced orthopedic doctor AI assistant. Based on the patient's details so far:
    - Orthopaedic Issue: {disease or "Not specified"}
    - Severity: {severity or "Not specified"}
    - Medical History: {medical_history or "Not specified"}

    Generate the next most relevant question to gather additional details about the patient's condition.
    Only ask one question.
    """
    return llm.predict(prompt).strip()

# Function to get AI Doctor's response based on the user's input
def get_doctor_response(disease, severity, medical_history, follow_up):
    llm = ChatGroq(api_key=groq_api_key, model="gemma2-9b-it")
    # template = """
    # You are an experienced orthopaedic doctor. Based on the following patient details:
    # - Orthopaedic Issue: {disease}
    # - Severity: {severity}
    # - Medical History: {medical_history}
    # - Follow-up Details: {follow_up}

    # Provide a concise output including:
    # 1. Recommended Medications
    # 2. Physiotherapy or Exercises
    # 3. Rest or Activity Guidelines
    # 4. Dietary Guidance for Bone Health
    # """
    
    template = f"""
    You are an only an experienced orthopedic doctor. You are unable to suggest any advice other than orthopedic problems. 

    The following details are provided by the patient:
    - Orthopaedic Issue: {disease}
    - Severity: {severity}
    - Medical History: {medical_history}
    - Follow-up Details: {follow_up}

    Only provide answers related to orthopedic care, treatment, and advice. If the problem is not orthopedic-related, inform the patient that you can only provide orthopedic advice.

    Provide a concise output including:
    1. Recommended Medications
    2. Physiotherapy or Exercises
    3. Rest or Activity Guidelines
    4. Dietary Guidance for Bone Health
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
st.set_page_config(page_title="Orthopaedic AI Doctor Chatbot", page_icon="🦴", layout="centered")

# CSS styling for the orthopaedic theme
st.markdown("""
    <style>
    body {
        background-color: #eef2f3;
        color: #333333;
        font-family: Arial, sans-serif;
    }
    .chat-box {
        background-color: #ffffff;
        border-radius: 12px;
        padding: 20px;
        margin-bottom: 16px;
        box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
        border-left: 5px solid #1E90FF;
    }
    .user-text {
        text-align: left;
        font-weight: bold;
        color: #007BFF;
    }
    .bot-text {
        text-align: left;
        color: #444444;
        font-size: 16px;
        line-height: 1.5;
    }
    .stTextInput {
        margin-top: 20px;
        padding: 12px;
        border: 1px solid #cccccc;
        border-radius: 12px;
        font-size: 14px;
        background-color: #fdfdfd;
    }
    .stButton > button {
        margin: 0 10px;
        padding: 10px 18px;
        font-size: 14px;
        border-radius: 8px;
        background-color: #007BFF;
        color: white;
        border: none;
        cursor: pointer;
        transition: background-color 0.3s ease;
    }
    .stButton > button:hover {
        background-color: #0056b3;
    }
    h1 {
        color: #1E90FF;
        font-size: 32px;
        margin-bottom: 20px;
    }
    .history-box {
        background-color: #f8f9fa;
        padding: 10px;
        border: 1px solid #e6e6e6;
        border-radius: 10px;
        margin-bottom: 10px;
        font-size: 14px;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("Orthopaedic AI Doctor Chatbot 🦴")

# Initialize session states
if 'conversation' not in st.session_state:
    st.session_state['conversation'] = [{"role": "bot", "text": "Hello, I am your Orthopaedic AI Doctor. What orthopaedic issue are you experiencing?"}]
if 'history' not in st.session_state:
    st.session_state['history'] = []
if 'stage' not in st.session_state:
    st.session_state['stage'] = 0
if 'user_input' not in st.session_state:
    st.session_state['user_input'] = ""

# Chat-like interaction
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
            st.markdown(f'<div class="chat-box bot-text">Doctor: {message["text"]}</div>', unsafe_allow_html=True)

# Button to view history
if st.button("View Past History"):
    if st.session_state.history:
        for idx, memory in enumerate(st.session_state.history):
            st.markdown(f"**Case {idx + 1}:**")
            st.markdown(f"- **Orthopaedic Issue:** {memory['disease']}")
            st.markdown(f"- **Severity:** {memory['severity']}")
            st.markdown(f"- **Medical History:** {memory['medical_history']}")
            st.markdown(f"- **Follow-Up Details:** {memory['follow_up']}")
            st.markdown(f"- **Response:** {memory['response']}")
            st.markdown("---")
    else:
        st.write("No history available.")
