# My LangChain Learning Journey 🤖

Hey there! This repository is a collection of scripts I wrote while learning how to use the **LangChain** framework. I built this to get hands-on experience connecting to different AI models, crafting dynamic prompts, building chat memory, and understanding how modern AI apps work behind the scenes.

## 🧠 What I Learned Building This

Through these scripts, I practically learned how to:

* **Connect to Different AI Brains:** I learned how to chat with commercial cloud models like OpenAI's GPT-4, open-source models via Hugging Face's API, and even run models completely locally on my own machine using Ollama.
* **Understand Vector Embeddings & Search:** I figured out how to convert regular text into mathematical numbers (vectors) and used `scikit-learn` to build a semantic search engine that compares "cosine similarity" to find meaning, not just exact keyword matches.
* **Master Prompt Engineering:** I learned how to dynamically structure the AI's instructions using `PromptTemplate` and `ChatPromptTemplate`, and how to save/load complex prompts as JSON files.
* **Give the AI a Memory:** I built a continuous chatbot that actually remembers the conversation by managing `SystemMessage`, `HumanMessage`, and `AIMessage` history.
* **Build a Real Web App:** I took my LangChain logic and turned it into an interactive "Research Paper Summarizer" web UI using **Streamlit**. 
* **Keep Secrets Safe:** I learned best practices for securing my API keys by using a `.env` file instead of writing them directly in the code.


