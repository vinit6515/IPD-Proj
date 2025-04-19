import streamlit as st

# Page config
st.set_page_config(page_title="Virtual Doctor Portal", layout="centered")

# Custom CSS for modern UI
st.markdown("""
    <style>
        /* Import a clean Google font */
        @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600&display=swap');

        html, body, [class*="css"] {
            font-family: 'Montserrat', sans-serif;
            background: linear-gradient(135deg, #e0f7ff, #f5f7fa, #e0f7ff);
            background-size: 400% 400%;
            animation: gradientBG 20s ease infinite;
        }

        @keyframes gradientBG {
            0% {background-position: 0% 50%;}
            50% {background-position: 100% 50%;}
            100% {background-position: 0% 50%;}
        }

        h1 {
            color: #004080;
            text-align: center;
            font-size: 3rem;
            margin-bottom: 0.2em;
        }

        p {
            text-align: center;
            font-size: 1.2em;
            color: #444;
            margin-top: 0;
            margin-bottom: 2em;
        }

        .doctor-button {
            background: linear-gradient(135deg, #0074D9, #005fa3);
            color: white;
            border: none;
            padding: 1rem 2rem;
            font-size: 1.1em;
            border-radius: 14px;
            cursor: pointer;
            transition: all 0.3s ease-in-out;
            margin: 1rem auto;
            display: block;
            width: 60%;
            font-weight: 600;
            box-shadow: 0 6px 15px rgba(0,0,0,0.1);
        }

        .doctor-button:hover {
            transform: translateY(-3px) scale(1.02);
            box-shadow: 0 8px 20px rgba(0,0,0,0.15);
        }

        footer {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown("<h1>🩺 Virtual Doctor Portal</h1>", unsafe_allow_html=True)
st.markdown("<p>Choose your preferred specialist to begin the consultation.</p>", unsafe_allow_html=True)

# Doctor links
doctor_links = {    
    "General Physician 👨‍⚕️": "https://ai-doctor-general-viraj27.streamlit.app/",
    "Dentist 🦷": "https://ai-chatbot-dentist-viraj27.streamlit.app/",
    "Gynaecologist 👩‍⚕️": "https://ai-doctor-gyno-viraj27.streamlit.app/",
    "Orthopedic 🦴": "https://ai-doctor-orthopedic-viraj27.streamlit.app/"
}

# Buttons
for doctor, link in doctor_links.items():
    button_html = f"""
        <form action="{link}" target="_blank">
            <button class="doctor-button">{doctor}</button>
        </form>
    """
    st.markdown(button_html, unsafe_allow_html=True)


