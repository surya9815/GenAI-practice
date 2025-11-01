# basic terminal Chatbot with Hugging Face
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id='mistralai/Mistral-7B-Instruct-v0.3',
    task='chat-completion',
    max_new_tokens=50
)
model = ChatHuggingFace(llm = llm)

chat_history = [
    SystemMessage(content='You are a GK teacher')
]     

while True:
    user_inp = input('You: ')
    chat_history.append(HumanMessage(content=user_inp))
    if user_inp == 'exit':
        break
    result = model.invoke(chat_history)
    chat_history.append(AIMessage(content=result.content))
    print('AI: ',result.content)
print('This is my Chat History: -> ',chat_history)
    

# result = model.invoke([HumanMessage(content="What is the capital of India?")])
# print(result.content)