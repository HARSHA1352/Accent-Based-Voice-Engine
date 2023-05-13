from gtts import gTTS
import os
import streamlit as st

# Define available accents
ACCENTS = {
    "Arabic": "ar",
    "Australian": "en-au",
    "Brazilian Portuguese": "pt-br",
    "British": "en-gb",
    "Canadian English": "en-ca",
    "Canadian French": "fr-ca",
    "Chinese": "zh",
    "Danish": "da",
    "Dutch": "nl",
    "Finnish": "fi",
    "Filipino": "fil",
    "French": "fr",
    "German": "de",
    "Hebrew": "he",
    "Hong Kong English": "en-hk",
    "Indian": "en-in",
    "Indonesian": "id",
    "Irish": "en-ie",
    "Italian": "it",
    "Japanese": "ja",
    "Korean": "ko",
    "Malaysian English": "en-my",
    "Mexican Spanish": "es-mx",
    "New Zealand": "en-nz",
    "Norwegian": "no",
    "Portuguese": "pt",
    "Russian": "ru",
    "Scottish": "en-scotland",
    "Singaporean English": "en-sg",
    "South African": "en-za",
    "Spanish": "es",
    "Swedish": "sv",
    "Thai": "th",
    "Turkish": "tr",
    "US": "en-us",
    "Vietnamese": "vi",
    "Welsh": "en-wls"
}


# Set default accent to US
default_accent = "US"

# Set page title
st.set_page_config(page_title="Accent Based Voice Assistant")

# Create the web interface
st.title("Accent Based Voice Assistant")

# Get input text from user
text = st.text_input("Enter the text:")

# Select the accent
accent = st.selectbox("Select the accent:", list(ACCENTS.keys()), index=list(ACCENTS.keys()).index(default_accent))

# Create button to generate the voice
if st.button("Generate a Voice"):
    # Generate voice
    tts = gTTS(text=text, lang=ACCENTS[accent])
    tts.save("audio_generated.mp3")
    os.system("mpg123 audio_generated.mp3")
    st.audio("audio_generated.mp3", format="audio/mp3")

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
