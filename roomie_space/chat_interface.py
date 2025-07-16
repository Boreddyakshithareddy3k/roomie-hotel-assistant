import gradio as gr
import requests

def get_mistral_response(user_input):
    url = "http://localhost:11434/v1/chat/completions"
    
    payload = {
        "model": "mistral",
        "messages": [{"role": "user", "content": user_input}],
        "temperature": 0.7
    }

    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
        data = response.json()

        if "choices" in data and len(data["choices"]) > 0:
            return data["choices"][0]["message"]["content"]
        else:
            return "⚠️ Mistral model returned no response."
    except Exception as e:
        return f"⚠️ Error: {str(e)}"

with gr.Blocks() as interface:
    gr.Markdown("## 🏨 Roomie - Your Hotel Assistant (Mistral/Ollama)")
    user_input = gr.Textbox(label="Ask Roomie...")
    output_text = gr.Textbox(label="Roomie Says:")

    def respond(message):
        return get_mistral_response(message)

    user_input.submit(respond, inputs=user_input, outputs=output_text)

interface.launch(share=True)
