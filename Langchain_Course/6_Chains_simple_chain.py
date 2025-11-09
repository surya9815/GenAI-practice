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

template = PromptTemplate(
    template='Write something about {topic}',
    input_variables=['topic']
)
parser= StrOutputParser()
chain = template | model | parser
result = chain.invoke({'topic':'Travel'})
print()
