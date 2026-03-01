from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv

load_dotenv()

# Create Hugging Face endpoint
llm = HuggingFaceEndpoint(
    repo_id="HuggingFaceH4/zephyr-7b-beta",  
    task="text-generation",
    max_new_tokens=300,
    temperature=0.7,
)

# Wrap as chat model
model = ChatHuggingFace(llm=llm)

chat_history = [
    SystemMessage(content="You are a helpful AI assistant")
]

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        break

    chat_history.append(HumanMessage(content=user_input))

    result = model.invoke(chat_history)

    chat_history.append(AIMessage(content=result.content))

    print("AI:", result.content)

print(chat_history)