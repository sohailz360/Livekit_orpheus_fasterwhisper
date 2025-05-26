#  Voice Assistant with Orpheus TTS/Faster Whisper and LiveKit



## 🔊 Overview

It is a fully openai api based,  voice assistant that combines the power of Orpheus TTS, LiveKit, and local LLMs to create incredibly natural and expressive speech. This project eliminates the need for cloud-based API services by integrating:




- **Orpheus TTS** for human-like speech with natural intonation and emotion
- **LiveKit** for real-time voice communication
- ** Whisper** for accurate speech-to-text conversion
- **Gemini** for running local large language models

The result is a voice assistant with remarkably natural speech capabilities, including emotional expressions like laughs, sighs, and gasps - all running completely on your local machine.

## ✨ Features


- 🗣️ **Expressive Speech** - Natural intonation, rhythm, and emotional expressions
- 🎭 **Emotion Tags** - Simple text-based tags to control emotion and expression
- 🎙️ **Real-time Conversation** - Fluid interaction through LiveKit
- 🧠 **Local LLM Integration** - Uses Ollama to run powerful models locally
- 👂 **Advanced Speech Recognition** - Fast local transcription with Whisper




## 💬 Usage

1. Make sure the Orpheus TTS server is running (default: http://localhost:5005)
2. Make sure Ollama is running with the llama3.2 model loaded
3. Make sure to reaplce the default openai tts.py with the tts.py from this repo 
4. Run the voice assistant:
   ```bash
   python tara.py
   ```

5. Connect to the LiveKit room and start interacting with Tara

## 🔧 How It Works

The system consists of several integrated components:

1. **Speech-to-Text (STT)**: Uses Faster Whisper for local transcription
2. **Language Model**: Connects to a local Ollama instance running LLama3.2
3. **Text-to-Speech (TTS)**: Modified OpenAI TTS module that connects to Orpheus TTS
4. **Voice Pipeline**: Handles the flow between components via LiveKit

Tara uses special text tags to express emotions in speech:
- `<giggle>`, `<laugh>`, `<chuckle>` for humor
- `<sigh>`, `<groan>` for showing disappointment or frustration
- `<gasp>`, `<cough>`, `<sniffle>`, `<yawn>` for other human-like expressions

## 🔄 Customization

You can modify the `tara.py` file to:
- Change the voice by editing the `voice` parameter in the TTS setup
- Modify the personality by editing the system prompt
- Adjust the LLM model by changing the Ollama model name
- Configure different endpoints for any of the services
