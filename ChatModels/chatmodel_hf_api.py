from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

#  Create endpoint
llm = HuggingFaceEndpoint(
    repo_id="HuggingFaceH4/zephyr-7b-beta",
    task="text-generation",
    max_new_tokens=150,
    temperature=0.7,
)

#  Wrap it into chat model
model = ChatHuggingFace(llm=llm)

#  Invoke
result = model.invoke("What is the capital of India?")
print(result.content)