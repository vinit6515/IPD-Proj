# import streamlit as st
# from langchain.prompts import PromptTemplate
# from langchain.llms import CTransformers

# ## Function to get a doctor's response from the Falcon model
# def getDoctorResponse(disease, severity, medical_history):
#     ### Falcon model setup
    
#     llm=CTransformers(
#         model='models\llama-2-7b-chat.ggmlv3.q8_0.bin',
#         model_type='llama',
#         config={"max_new_tokens": 512, "temperature": 0.3})


#     ## Prompt Template
#     template = """
#         You are a doctor. A patient has the following details:
#         Disease: {disease}
#         Severity: {severity}
#         Medical History: {medical_history}
        
#         Provide advice including:
#         1. Medications
#         2. Health tips
#         3. Rest recommendations
#         4. Dietary guidance
#     """
#     prompt = PromptTemplate(
#         input_variables=["disease", "severity", "medical_history"], template=template
#     )

#     ## Generate the doctor's response from the Falcon model
#     response = llm(
#         prompt.format(disease=disease, severity=severity, medical_history=medical_history)
#     )
#     return response

# st.set_page_config(page_title="AI Doctor Chatbot", page_icon="🤖", layout="centered")

# st.header("AI Doctor Chatbot 🤖")
# st.write("Hello, I am an AI Doctor. How can I help you?")

# if "history" not in st.session_state:
#     st.session_state.history = ""

# disease = st.text_input("Enter your disease:")
# severity = st.selectbox("Select the severity level:", ["Mild", "Moderate", "Severe"], index=0)
# medical_history = st.text_area("Provide any relevant medical history:")

# submit = st.button("Get Advice")

# if submit and disease:
#     # Append user input to the conversation history
#     st.session_state.history += f"You: I have {disease} with {severity} severity.\n"
#     st.session_state.history += f"Medical History: {medical_history}\n"

#     # Get the doctor's response
#     doctor_response = getDoctorResponse(disease, severity, medical_history)

#     # Append bot response to conversation history
#     st.session_state.history += f"AI Doctor: {doctor_response.strip()}\n"

#     # Display conversation history
#     st.text_area("Conversation", st.session_state.history, height=400)



# import streamlit as st
# from langchain.prompts import PromptTemplate
# from langchain.llms import CTransformers

# # Function to get AI Doctor's response
# def getDoctorResponse(disease, severity, medical_history, follow_up):
#     llm=CTransformers(
#         model='models\llama-2-7b-chat.ggmlv3.q8_0.bin',
#         model_type='llama',
#         config={"max_new_tokens": 256, "temperature": 0.7},
#     )

#     template = """
#     You are an experienced doctor. Based on the following patient details:
#     - Disease: {disease}
#     - Severity: {severity}
#     - Medical History: {medical_history}
#     - Follow-up Answers: {follow_up}

#     Provide the following:
#     1. Medications
#     2. Health tips
#     3. Rest recommendations
#     4. Dietary guidance
#     """
#     prompt = PromptTemplate(
#         input_variables=["disease", "severity", "medical_history", "follow_up"],
#         template=template,
#     )

#     response = llm(
#         prompt.format(
#             disease=disease,
#             severity=severity,
#             medical_history=medical_history,
#             follow_up=follow_up,
#         )
#     )
#     return response

# # Streamlit setup
# st.set_page_config(page_title="AI Doctor Chatbot", page_icon="🤖", layout="centered")
# st.title("AI Doctor Chatbot 🤖")
# st.write("Hello, I am an AI Doctor. Let's proceed step by step to help you better!")

# if "step" not in st.session_state:
#     st.session_state.step = 1
#     st.session_state.disease = ""
#     st.session_state.severity = ""
#     st.session_state.medical_history = ""
#     st.session_state.follow_up = ""
#     st.session_state.response = ""

# # Step 1: Get the disease
# if st.session_state.step == 1:
#     st.subheader("Step 1: Tell me your primary disease.")
#     disease = st.text_input("Enter your disease:")
#     if st.button("Next"):
#         if disease:
#             st.session_state.disease = disease
#             st.session_state.step = 2
#         else:
#             st.warning("Please provide your disease.")

# # Step 2: Ask for severity
# elif st.session_state.step == 2:
#     st.subheader("Step 2: How severe is your condition?")
#     severity = st.selectbox(
#         "Select the severity level:",
#         ["Mild", "Moderate", "Severe"],
#         index=0,
#     )
#     if st.button("Next"):
#         st.session_state.severity = severity
#         st.session_state.step = 3

# # Step 3: Ask for medical history
# elif st.session_state.step == 3:
#     st.subheader("Step 3: Do you have any relevant medical history?")
#     medical_history = st.text_area("Enter your medical history:")
#     if st.button("Next"):
#         st.session_state.medical_history = medical_history
#         st.session_state.step = 4

# # Step 4: Follow-up questions (if any)
# elif st.session_state.step == 4:
#     st.subheader("Step 4: Additional questions")
#     follow_up = st.text_area("Provide additional details if necessary (e.g., symptoms):")
#     if st.button("Submit"):
#         st.session_state.follow_up = follow_up
#         st.session_state.step = 5

# # Step 5: Generate response
# elif st.session_state.step == 5:
#     st.subheader("Processing your details...")
#     response = getDoctorResponse(
#         st.session_state.disease,
#         st.session_state.severity,
#         st.session_state.medical_history,
#         st.session_state.follow_up,
#     )
#     st.session_state.response = response
#     st.session_state.step = 6

# # Step 6: Display the AI Doctor's guidance
# elif st.session_state.step == 6:
#     st.subheader("Here is your personalized advice:")
#     st.text_area("Doctor's Guidance", st.session_state.response, height=300)
#     if st.button("Restart"):
#         st.session_state.step = 1
#         st.session_state.disease = ""
#         st.session_state.severity = ""
#         st.session_state.medical_history = ""
#         st.session_state.follow_up = ""
#         st.session_state.response = ""



# import streamlit as st
# from langchain.prompts import PromptTemplate
# from langchain.llms import CTransformers

# # Function to get AI Doctor's response
# def getDoctorResponse(disease, severity, medical_history, follow_up):
#     llm = CTransformers(
#         model='models\llama-2-7b-chat.ggmlv3.q8_0.bin',
#         model_type='llama',
#         config={"max_new_tokens": 256, "temperature": 0.7},
#     )

#     template = """
#     You are an experienced doctor. Based on the following patient details:
#     - Disease: {disease}
#     - Severity: {severity}
#     - Medical History: {medical_history}
#     - Follow-up Details: {follow_up}

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

#     response = llm(
#         prompt.format(
#             disease=disease,
#             severity=severity,
#             medical_history=medical_history,
#             follow_up=follow_up,
#         )
#     )
#     return response.strip()

# # Initialize Streamlit session state
# if "conversation" not in st.session_state:
#     st.session_state.conversation = []
# if "memory" not in st.session_state:
#     st.session_state.memory = []
# if "stage" not in st.session_state:
#     st.session_state.stage = 0

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
#     </style>
#     """,
#     unsafe_allow_html=True,
# )

# st.title("AI Doctor Chatbot 🤖")

# # Add chat-like interaction
# chat_placeholder = st.container()
# user_input = st.text_input("Enter your response:", "")

# if st.session_state.stage == 0:
#     if user_input:
#         st.session_state.disease = user_input
#         st.session_state.conversation.append({"role": "user", "text": user_input})
#         st.session_state.conversation.append({"role": "bot", "text": "How severe is your condition? (Mild, Moderate, Severe)"})
#         st.session_state.stage = 1
#         user_input = ""

# elif st.session_state.stage == 1:
#     if user_input:
#         st.session_state.severity = user_input
#         st.session_state.conversation.append({"role": "user", "text": user_input})
#         st.session_state.conversation.append({"role": "bot", "text": "Do you have any relevant medical history?"})
#         st.session_state.stage = 2
#         user_input = ""

# elif st.session_state.stage == 2:
#     if user_input:
#         st.session_state.medical_history = user_input
#         st.session_state.conversation.append({"role": "user", "text": user_input})
#         st.session_state.conversation.append({"role": "bot", "text": "Any other symptoms or follow-up details?"})
#         st.session_state.stage = 3
#         user_input = ""

# elif st.session_state.stage == 3:
#     if user_input:
#         st.session_state.follow_up = user_input
#         st.session_state.conversation.append({"role": "user", "text": user_input})

#         # Generate response
#         response = getDoctorResponse(
#             st.session_state.disease,
#             st.session_state.severity,
#             st.session_state.medical_history,
#             st.session_state.follow_up,
#         )
#         st.session_state.conversation.append({"role": "bot", "text": response})

#         st.session_state.memory.append(
#             {
#                 "disease": st.session_state.disease,
#                 "severity": st.session_state.severity,
#                 "medical_history": st.session_state.medical_history,
#                 "follow_up": st.session_state.follow_up,
#                 "response": response,
#             }
#         )
#         st.session_state.stage = 4

# # Display the chat
# with chat_placeholder:
#     for message in st.session_state.conversation:
#         if message["role"] == "user":
#             st.markdown(f'<div class="chat-box user-text">You: {message["text"]}</div>', unsafe_allow_html=True)
#         else:
#             st.markdown(f'<div class="chat-box bot-text">Doctor: {message["text"]}</div>', unsafe_allow_html=True)

# # Restart or View Memory
# if st.session_state.stage == 4:
#     st.markdown("### What would you like to do next?")
#     col1, col2 = st.columns(2)
#     with col1:
#         if st.button("Start Over"):
#             st.session_state.stage = 0
#             st.session_state.conversation = []
#     with col2:
#         if st.button("View Past Cases"):
#             st.markdown("### Past Guidance and Medication")
#             for i, memory in enumerate(st.session_state.memory[-5:], start=1):
#                 st.markdown(
#                     f"**Case {i}:**\n\n"
#                     f"- **Disease**: {memory['disease']}\n"
#                     f"- **Severity**: {memory['severity']}\n"
#                     f"- **Medical History**: {memory['medical_history']}\n"
#                     f"- **Follow-up**: {memory['follow_up']}\n"
#                     f"- **Guidance**: {memory['response']}\n"
#                 )







# import streamlit as st
# from langchain.prompts import PromptTemplate
# from langchain.llms import CTransformers

# # Function to get AI Doctor's response
# def getDoctorResponse(disease, severity, medical_history, follow_up):
#     llm = CTransformers(
#         model='models\llama-2-7b-chat.ggmlv3.q8_0.bin',
#         model_type='llama',
#         config={"max_new_tokens": 256, "temperature": 0.7},
#     )

#     template = """
#     You are an experienced doctor. Based on the following patient details:
#     - Disease: {disease}
#     - Severity: {severity}
#     - Medical History: {medical_history}
#     - Follow-up Details: {follow_up}

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

#     response = llm(
#         prompt.format(
#             disease=disease,
#             severity=severity,
#             medical_history=medical_history,
#             follow_up=follow_up,
#         )
#     )
#     return response.strip()

# # Initialize Streamlit session state
# if "conversation" not in st.session_state:
#     st.session_state.conversation = [{"role": "bot", "text": "Hello, I am your AI Doctor. What problem or disease are you experiencing?"}]
# if "memory" not in st.session_state:
#     st.session_state.memory = []
# if "stage" not in st.session_state:
#     st.session_state.stage = 0
# if "user_input" not in st.session_state:
#     st.session_state.user_input = ""

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

#     # Generate response
#     response = getDoctorResponse(
#         st.session_state.disease,
#         st.session_state.severity,
#         st.session_state.medical_history,
#         st.session_state.follow_up,
#     )
#     st.session_state.conversation.append({"role": "bot", "text": response})

#     st.session_state.memory.append(
#         {
#             "disease": st.session_state.disease,
#             "severity": st.session_state.severity,
#             "medical_history": st.session_state.medical_history,
#             "follow_up": st.session_state.follow_up,
#             "response": response,
#         }
#     )
#     st.session_state.stage = 4

# # Display the chat
# with chat_placeholder:
#     for message in st.session_state.conversation:
#         if message["role"] == "user":
#             st.markdown(f'<div class="chat-box user-text">You: {message["text"]}</div>', unsafe_allow_html=True)
#         else:
#             st.markdown(f'<div class="chat-box bot-text">Doctor: {message["text"]}</div>', unsafe_allow_html=True)

# # Restart or View Memory
# if st.session_state.stage == 4:
#     st.markdown("### What would you like to do next?")
#     if st.button("Restart Chat"):
#         st.experimental_rerun()  # Refreshes the page





# import streamlit as st
# from langchain.prompts import PromptTemplate
# from langchain.llms import CTransformers

# # Function to get AI Doctor's response
# def getDoctorResponse(disease, severity, medical_history, follow_up):
#     llm = CTransformers(
#         model='models\llama-2-7b-chat.ggmlv3.q8_0.bin',
#         model_type='llama',
#         config={"max_new_tokens": 256, "temperature": 0.7},
#     )

#     template = """
#     You are an experienced doctor. Based on the following patient details:
#     - Disease: {disease}
#     - Severity: {severity}
#     - Medical History: {medical_history}
#     - Follow-up Details: {follow_up}

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

#     response = llm(
#         prompt.format(
#             disease=disease,
#             severity=severity,
#             medical_history=medical_history,
#             follow_up=follow_up,
#         )
#     )
#     return response.strip()

# # Initialize Streamlit session state
# if "conversation" not in st.session_state:
#     st.session_state.conversation = [{"role": "bot", "text": "Hello, I am your AI Doctor. What problem or disease are you experiencing?"}]
# if "history" not in st.session_state:
#     st.session_state.history = []
# if "stage" not in st.session_state:
#     st.session_state.stage = 0
# if "user_input" not in st.session_state:
#     st.session_state.user_input = ""

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

#     # Generate response
#     response = getDoctorResponse(
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
#     st.session_state.stage = 4

# # Display the chat
# with chat_placeholder:
#     for message in st.session_state.conversation:
#         if message["role"] == "user":
#             st.markdown(f'<div class="chat-box user-text">You: {message["text"]}</div>', unsafe_allow_html=True)
#         else:
#             st.markdown(f'<div class="chat-box bot-text">Doctor: {message["text"]}</div>', unsafe_allow_html=True)

# # Restart or View Memory
# if st.session_state.stage == 4:
#     st.markdown("### What would you like to do next?")
#     col1, col2 = st.columns(2)

#     with col1:
#         if st.button("Start New Chat"):
#             st.session_state.conversation = [{"role": "bot", "text": "Hello, I am your AI Doctor. What problem or disease are you experiencing?"}]
#             st.session_state.stage = 0
#             st.session_state.user_input = ""
#             st.experimental_rerun()  # Refresh the page

#     with col2:
#         if st.button("View Past History"):
#             st.write("### Past History")
#             for idx, memory in enumerate(st.session_state.history):
#                 st.markdown(f"**Case {idx + 1}:**")
#                 st.markdown(f"- **Disease:** {memory['disease']}")
#                 st.markdown(f"- **Severity:** {memory['severity']}")
#                 st.markdown(f"- **Medical History:** {memory['medical_history']}")
#                 st.markdown(f"- **Follow-Up Details:** {memory['follow_up']}")
#                 st.markdown(f"- **Response:** {memory['response']}")
#                 st.markdown("---")



# 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



# import streamlit as st
# import os
# from groq import Groq 
# import random
# from langchain.chains import ConversationChain
# from langchain.chains.conversation.memory import ConversationBufferMemory
# from langchain_groq import ChatGroq
# from langchain.prompts import PromptTemplate
# from dotenv import load_dotenv

# load_dotenv()

# groq_api_key = os.environ['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']




# import streamlit as st
# import os
# from dotenv import load_dotenv
# from langchain.prompts import PromptTemplate
# from langchain.llms import CTransformers
# from langchain.chains import ConversationChain
# from langchain.chains.conversation.memory import ConversationBufferMemory
# from langchain_groq import ChatGroq

# load_dotenv()

# # Set your Groq API Key here (directly or from .env file)
# groq_api_key = "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"

# # Define a function to reset the conversation and start a new one
# def refresh_app():
#     st.session_state.clear()
#     st.experimental_set_query_params()  # Triggering a page rerun

# # Initialize or reset the session state
# if 'conversation' not in st.session_state:
#     st.session_state['conversation'] = ConversationChain(
#         llm=ChatGroq(api_key=groq_api_key, model="gemma2-9b-it"),  # Using gemma2-9b-it model
#         memory=ConversationBufferMemory(),
#     )
#     st.session_state['history'] = []  # Store history of conversations
#     st.session_state['input_counter'] = 0  # Counter for unique keys

# # Define the logic for handling user input and getting responses
# def handle_input(user_input):
#     conversation = st.session_state['conversation']
#     response = conversation.predict(input=user_input)
#     st.session_state['history'].append(f"You: {user_input}\nBot: {response}")
#     return response

# # Layout of the page
# st.title("AI Doctor Chatbot 🤖")

# # Display current history of conversation
# if st.session_state['history']:
#     st.write("### Conversation History:")
#     for message in st.session_state['history']:
#         st.write(message)

# # Input box for user to provide symptoms/disease
# input_key = f"user_input_{st.session_state['input_counter']}"  # Create a unique key
# user_input = st.text_area("Describe your disease or symptoms:", key=input_key, height=100)

# if user_input:
#     response = handle_input(user_input)
#     st.write(f"AI Doctor: {response}")

#     # After each response, increment the input counter and clear the input field for next entry
#     st.session_state['input_counter'] += 1

#     # Button to restart the conversation
#     if st.button("Start New Chat"):
#         refresh_app()

#     # Button to view past conversation history
#     if st.button("View Past History"):
#         st.write("### Past Conversations")
#         for past_convo in st.session_state['history']:
#             st.write(past_convo)




















# import streamlit as st
# import os
# from dotenv import load_dotenv
# from langchain.prompts import PromptTemplate
# from langchain.chains import ConversationChain
# from langchain.chains.conversation.memory import ConversationBufferMemory
# from langchain_groq import ChatGroq

# load_dotenv()

# # Set your Groq API Key here (directly or from .env file)
# groq_api_key = "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"

# # Function to get AI Doctor's response based on the user's input
# def get_doctor_response(disease, severity, medical_history, follow_up):
#     llm = ChatGroq(api_key=groq_api_key, model="gemma2-9b-it")  # Groq model
#     template = """
#     You are an experienced doctor. Based on the following patient details:
#     - Disease: {disease}
#     - Severity: {severity}
#     - Medical History: {medical_history}
#     - Follow-up Details: {follow_up}

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

# # Define a function to reset the conversation and start a new one
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
#     st.session_state.stage = 4

# # Display the chat
# with chat_placeholder:
#     for message in st.session_state.conversation:
#         if message["role"] == "user":
#             st.markdown(f'<div class="chat-box user-text">You: {message["text"]}</div>', unsafe_allow_html=True)
#         else:
#             st.markdown(f'<div class="chat-box bot-text">Doctor: {message["text"]}</div>', unsafe_allow_html=True)

# # Restart or View Memory
# if st.session_state.stage == 4:
#     st.markdown("### What would you like to do next?")
#     col1, col2 = st.columns(2)

#     with col1:
#         if st.button("Start New Chat"):
#             st.session_state.conversation = [{"role": "bot", "text": "Hello, I am your AI Doctor. What problem or disease are you experiencing?"}]
#             st.session_state.stage = 0
#             st.session_state.user_input = ""
#             st.experimental_rerun()  # Refresh the page

#     with col2:
#         if st.button("View Past History"):
#             st.write("### Past History")
#             for idx, memory in enumerate(st.session_state.history):
#                 st.markdown(f"**Case {idx + 1}:**")
#                 st.markdown(f"- **Disease:** {memory['disease']}")
#                 st.markdown(f"- **Severity:** {memory['severity']}")
#                 st.markdown(f"- **Medical History:** {memory['medical_history']}")
#                 st.markdown(f"- **Follow-Up Details:** {memory['follow_up']}")
#                 st.markdown(f"- **Response:** {memory['response']}")
#                 st.markdown("---")









# import streamlit as st
# import os
# from dotenv import load_dotenv
# from langchain.prompts import PromptTemplate
# from langchain.chains import ConversationChain
# from langchain.chains.conversation.memory import ConversationBufferMemory
# from langchain_groq import ChatGroq

# load_dotenv()

# # Set your Groq API Key here (directly or from .env file)
# groq_api_key = "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"

# # Function to get AI Doctor's response based on the user's input
# def get_doctor_response(disease, severity, medical_history, follow_up):
#     llm = ChatGroq(api_key=groq_api_key, model="gemma2-9b-it")  # Groq model
#     template = """
#     You are an experienced doctor. Based on the following patient details:
#     - Disease: {disease}
#     - Severity: {severity}
#     - Medical History: {medical_history}
#     - Follow-up Details: {follow_up}

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

# # Define a function to reset the conversation and start a new one
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
#     st.session_state.stage = 4

# # Display the chat
# with chat_placeholder:
#     for message in st.session_state.conversation:
#         if message["role"] == "user":
#             st.markdown(f'<div class="chat-box user-text">You: {message["text"]}</div>', unsafe_allow_html=True)
#         else:
#             st.markdown(f'<div class="chat-box bot-text">Doctor: {message["text"]}</div>', unsafe_allow_html=True)

# # Restart or View Memory
# if st.session_state.stage == 4:
#     st.markdown("### What would you like to do next?")
#     col1, col2 = st.columns(2)

#     with col1:
#         if st.button("Start New Chat"):
#             # Reset session state
#             st.session_state.conversation = [{"role": "bot", "text": "Hello, I am your AI Doctor. What problem or disease are you experiencing?"}]
#             st.session_state.stage = 0
#             st.session_state.user_input = ""
            
#             # Reset history
#             st.session_state.history = []
            
#             # Trigger a page rerun after resetting state
#             st.experimental_rerun()

#     with col2:
#         if st.button("View Past History"):
#             st.write("### Past History")
#             for idx, memory in enumerate(st.session_state.history):
#                 st.markdown(f"**Case {idx + 1}:**")
#                 st.markdown(f"- **Disease:** {memory['disease']}")
#                 st.markdown(f"- **Severity:** {memory['severity']}")
#                 st.markdown(f"- **Medical History:** {memory['medical_history']}")
#                 st.markdown(f"- **Follow-Up Details:** {memory['follow_up']}")
#                 st.markdown(f"- **Response:** {memory['response']}")
#                 st.markdown("---")











# import streamlit as st
# import os
# from dotenv import load_dotenv
# from langchain.prompts import PromptTemplate
# from langchain.chains import ConversationChain
# from langchain.chains.conversation.memory import ConversationBufferMemory
# from langchain_groq import ChatGroq

# load_dotenv()

# # Set your Groq API Key here (directly or from .env file)
# groq_api_key = "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"

# # Function to get AI Doctor's response based on the user's input
# def get_doctor_response(disease, severity, medical_history, follow_up):
#     llm = ChatGroq(api_key=groq_api_key, model="gemma2-9b-it")  # Groq model
#     template = """
#     You are an experienced doctor. Based on the following patient details:
#     - Disease: {disease}
#     - Severity: {severity}
#     - Medical History: {medical_history}
#     - Follow-up Details: {follow_up}

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

# # Define a function to reset the conversation and start a new one
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
#     # Automatically continue to the next stage or restart the conversation
#     st.session_state.stage = 0  # or keep it here for another round of advice, based on requirements
#     st.session_state.user_input = ""

# # Display the chat
# with chat_placeholder:
#     for message in st.session_state.conversation:
#         if message["role"] == "user":
#             st.markdown(f'<div class="chat-box user-text">You: {message["text"]}</div>', unsafe_allow_html=True)
#         else:
#             st.markdown(f'<div class="chat-box bot-text">Doctor: {message["text"]}</div>', unsafe_allow_html=True)

# # View Past History
# st.markdown("### View Past History")
# if st.session_state.history:
#     for idx, memory in enumerate(st.session_state.history):
#         st.markdown(f"**Case {idx + 1}:**")
#         st.markdown(f"- **Disease:** {memory['disease']}")
#         st.markdown(f"- **Severity:** {memory['severity']}")
#         st.markdown(f"- **Medical History:** {memory['medical_history']}")
#         st.markdown(f"- **Follow-Up Details:** {memory['follow_up']}")
#         st.markdown(f"- **Response:** {memory['response']}")
#         st.markdown("---")






























































































# import streamlit as st
# import os
# from dotenv import load_dotenv
# from langchain.prompts import PromptTemplate
# from langchain.chains import ConversationChain
# from langchain.chains.conversation.memory import ConversationBufferMemory
# from langchain_groq import ChatGroq

# load_dotenv()

# # Set your Groq API Key here (directly or from .env file)
# groq_api_key = "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"

# # Function to get AI Doctor's response based on the user's input
# def get_doctor_response(disease, severity, medical_history, follow_up):
#     llm = ChatGroq(api_key=groq_api_key, model="gemma2-9b-it")  # Groq model
#     template = """
#     You are an experienced doctor. Based on the following patient details:
#     - Disease: {disease}
#     - Severity: {severity}
#     - Medical History: {medical_history}
#     - Follow-up Details: {follow_up}

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

# # Define a function to reset the conversation and start a new one
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
#     # Automatically continue to the next stage or restart the conversation
#     st.session_state.stage = 0  # or keep it here for another round of advice, based on requirements
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
#             st.markdown(f"- **Response:** {memory['response']}")
#             st.markdown("---")

















import streamlit as st
import os
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain_groq import ChatGroq

load_dotenv()

groq_api_key = "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"

def generate_question(stage, disease=None, severity=None, medical_history=None):
    llm = ChatGroq(api_key=groq_api_key, model="gemma2-9b-it")  # Groq model
    prompt = f"""
    You are an experienced general doctor AI assistant. Based on the patient's details so far:
    - Disease: {disease or "Not specified"}
    - Severity: {severity or "Not specified"}
    - Medical History: {medical_history or "Not specified"}

    Generate the next most relevant question to gather additional details about the patient's condition.
    Only ask one question.
    """
    return llm.predict(prompt).strip()

def get_doctor_response(disease, severity, medical_history, follow_up):
    llm = ChatGroq(api_key=groq_api_key, model="gemma2-9b-it")
    template = """
    You are an experienced general practitioner doctor. You are unable to suggest any advice other than general health problems. Based on the following patient details:
    - Disease: {disease}
    - Severity: {severity}
    - Medical History: {medical_history}
    - Follow-up Details: {follow_up}

    Only provide answers related to general health care, treatment, and advice. If the problem is not related to general health, inform the patient that you can only provide general health advice.

    Provide a concise output including:
    1. Medications
    2. Health tips
    3. Rest recommendations
    4. Dietary guidance
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
st.set_page_config(page_title="AI Doctor Chatbot", page_icon="🤖", layout="centered")
st.markdown("""
    <style>
    body {
        background-color: #f7f9fc;
        color: #333333;
        font-family: Arial, sans-serif;
    }
    .chat-box {
        background-color: #ffffff;
        border-radius: 8px;
        padding: 20px;
        margin-bottom: 16px;
        box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.1);
    }
    .user-text {
        text-align: left;
        font-weight: bold;
        color: #4CAF50;
    }
    .bot-text {
        text-align: left;
        color: #555555;
        margin-bottom: 10px;
    }
    .stTextInput {
        margin-top: 20px;
        padding: 10px;
        border: 1px solid #dddddd;
        border-radius: 8px;
    }
    .stButton > button {
        margin: 0 10px;
        padding: 8px 16px;
        font-size: 14px;
        border-radius: 6px;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("AI Doctor Chatbot 🤖")

# Initialize session states
if 'conversation' not in st.session_state:
    st.session_state['conversation'] = [{"role": "bot", "text": "Hello, I am your AI Doctor. What problem or disease are you experiencing?"}]
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
            st.markdown(f"- **Disease:** {memory['disease']}")
            st.markdown(f"- **Severity:** {memory['severity']}")
            st.markdown(f"- **Medical History:** {memory['medical_history']}")
            st.markdown(f"- **Follow-Up Details:** {memory['follow_up']}")
            st.markdown(f"- **Response:** {memory['response']}")
            st.markdown("---")
    else:
        st.write("No history available.")
