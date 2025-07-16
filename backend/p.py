# ✅ p.py (or langchain_agent.py test file)

import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# ✅ This is the correct model for text chat
model = genai.GenerativeModel(model_name="gemini-1.5-pro")

response = model.generate_content("Hello! What can you do?")
print(response.text)
