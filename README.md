 Layer       | Tools/Tech                                   |
|-------------|-----------------------------------------------|
|  LLM       | `Mistral` (via `Ollama`)                      |
|  LangChain | (optional) for advanced prompt orchestration |
|  UI        | `Gradio` for user chat interface              |
| Voice     | `pyttsx3`, `speech_recognition` (STT, TTS)    |
| Admin     | `Streamlit` Dashboard for monitoring          |
| Backend   | Python, REST API (Ollama local endpoint)      |

⚙️ Setup Instructions

 1. Install and Run Ollama + Mistral

➡Install Ollama:
[https://ollama.com/download](https://ollama.com/download)

bash-
ollama pull mistral
ollama serve


2. Launch the Chatbot
bash-
cd backend
pip install -r requirements.txt
python chat_interface.py
 This launches the Gradio interface at:
🔗 http://localhost:7860
