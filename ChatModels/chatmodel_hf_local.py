from langchain_community.chat_models import ChatOllama

llm = ChatOllama(model="qwen2.5:7b")

response = llm.invoke("Explain transformers in simple terms.")
print(response.content)