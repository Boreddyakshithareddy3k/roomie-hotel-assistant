from langchain_community.chat_models import ChatOllama
from langchain.schema import HumanMessage

llm = ChatOllama(model="mistral")  # Ensure Ollama and Mistral are running

def get_roomie_response(user_input):
    message = HumanMessage(content=user_input)
    response = llm.invoke([message])
    return response.content
