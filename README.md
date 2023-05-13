
This is a web application built using Streamlit that allows users to generate audio files from text inputs using different accents.

The application uses the gTTS library to generate audio files and the ACCENTS dictionary to select the accent of the generated audio file. The default accent is set to "US".

## Requirements
- Python 3.x
- Streamlit
- gTTS
- mpg123

## Usage
To run the application, simply navigate to the project directory and run the following command in the terminal:
```
streamlit run app.py
```

Once the application is running, the user can enter text into the input field and select an accent from the dropdown menu. When the "Generate a Voice" button is clicked, the application generates an audio file from the input text with the selected accent and plays the audio file.

## Files
- `app.py`: The main file containing the Streamlit application code.
- `audio_generated.mp3`: The generated audio file that is played by the application.

## Acknowledgements
The ACCENTS dictionary was sourced from the gTTS documentation. The mpg123 library is required to play the audio file on Linux machines.

## Limitations
- The gTTS library requires an internet connection to generate the audio file.
- The application only allows the selection of pre-defined accents and does not support custom accents.
