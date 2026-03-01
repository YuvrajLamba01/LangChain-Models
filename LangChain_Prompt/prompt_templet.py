from langchain_core.prompts import PromptTemplate
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

# Create HF endpoint 
llm = HuggingFaceEndpoint(
    repo_id="HuggingFaceH4/zephyr-7b-beta",
    task="text-generation",
    max_new_tokens=200,
    temperature=0.7,
)

# Wrap as chat model
model = ChatHuggingFace(llm=llm)

# Prompt template
template2 = PromptTemplate(
    template="Greet this person in 5 languages. The name of the person is {name}",
    input_variables=["name"]
)

# Fill values
prompt = template2.invoke({"name": "user"})

result = model.invoke(prompt)

print(result.content)