from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel

load_dotenv()
llm = HuggingFaceEndpoint(
    repo_id='mistralai/Mistral-7B-Instruct-v0.3',
    task='chat-completion',
    max_new_tokens=50
)
model = ChatHuggingFace(llm = llm)

prompt1 = PromptTemplate(
    template='Generate Short and Simple notes from this text \n {text}',
    input_variables=['text']
)

prompt2 = PromptTemplate(
    template='Generate 5 Simple Quiz ques from this text \n {text}',
    input_variables=['text']
)
prompt3 = PromptTemplate(
    template='Merge Provided notes and quiz into a single document \n notes -> {notes} quiz -> {quiz}',
    input_variables=['notes','quiz']
)
parser = StrOutputParser()

parallel_chain = RunnableParallel({     #-> this is the parallel
    'notes': prompt1 | model | parser,
    'quiz': prompt2 | model | parser,
})

merge_chain = prompt3 | model | parser      #this is the last chain

chain = parallel_chain | merge_chain         #this is actual merging of two chains

text = ''
result = chain.invoke({'text':text})

print(result)

chain.get_graph().print_ascii()