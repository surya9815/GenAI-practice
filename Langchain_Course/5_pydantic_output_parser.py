from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser  #-> imp one for this demo
from pydantic import BaseModel, Field

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id='mistralai/Mistral-7B-Instruct-v0.3',
    task='chat-completion',
    max_new_tokens=50
)
model = ChatHuggingFace(llm = llm)

class Person(BaseModel):
    name: str = Field(description='Name of Person')
    age: int = Field(gt=18, description='Age of Person')
    city: str = Field(description='Name of city Person belongs to')
    
parser = PydanticOutputParser(pydantic_object=Person)

template = PromptTemplate(
    template='Generate the name and age of a fictional {place} person \n {format_instruction}',
    input_variables=['place'],
    partial_variables={'format_instruction':parser.get_format_instructions()}
)

# prompt = template.invoke({'place':'India'})
# result = model.invoke(prompt)
# fin_result = parser.parse(result.content)

chain = template | model  | parser
fin_result = chain.invoke({'place':'India'})

print(fin_result)