from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o-mini")

prompts = [
    "Explain what an API is in simple terms.",
    "What is the difference between AI and machine learning?",
    "Explain how RAG works in a simple way."
]

for p in prompts:
    response = llm.invoke(p)
    print(response.content)