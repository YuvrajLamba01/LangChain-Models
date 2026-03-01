from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

# Create endpoint
llm = HuggingFaceEndpoint(
    repo_id="HuggingFaceH4/zephyr-7b-beta",
    task="text-generation",
    max_new_tokens=200,
    temperature=1.0,
)

# Wrap into chat model
model = ChatHuggingFace(llm=llm)

# Generate text
result = model.invoke("Write a 5 line poem on cricket")

print(result.content)