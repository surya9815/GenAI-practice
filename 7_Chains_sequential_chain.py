from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()
llm = HuggingFaceEndpoint(
    repo_id='mistralai/Mistral-7B-Instruct-v0.3',
    task='chat-completion',
    max_new_tokens=50
)
model = ChatHuggingFace(llm = llm)

prompt1 = PromptTemplate(
    template='Write something about {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='Write a summary about {text}',
    input_variables=['text']
)
parser = StrOutputParser()
chain = prompt1 | model | parser |prompt2 | model | parser

res = chain.invoke({'topic': 'india'})

print(res)

chain.get_graph().print_ascii()