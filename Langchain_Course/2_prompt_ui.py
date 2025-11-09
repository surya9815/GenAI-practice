from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import streamlit as st
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate


load_dotenv()
llm = HuggingFaceEndpoint(
    repo_id='TinyLlama/TinyLlama-1.1B-Chat-v1.0',
    task='conversational',
    max_new_tokens=150
)
model = ChatHuggingFace(llm=llm)

st.header('Research Tool')

#  ----- <Code for Static Prompt> -------

# user_input = st.text_input('Enter Your prompt')

# if st.button('Summarize'):
#     answer = model.invoke(user_input)
#     st.write(answer.content)

# ------<End Static>-------

# ------ Code For Dynamic Prompt
# st.selectbox --> gives dropdown
paper_input = st.selectbox("Select Research Paper Name", ["Select...", "Attention Is All You Need",
                                                          "BERT: Pre-training of Deep Bidirectional Transformers", 
                                                          "GPT-3: Language Models are Few-Shot Learners", 
                                                          "Diffusion Models Beat GANs on Image Synthesis"])
style_input = st.selectbox ("Select Explanation Style", ["Beginner-Friendly", "Technical", 
                                                         "Code-Oriented", "Mathematical"] )
length_input = st.selectbox ("Select Explanation Length", ["Short (1-2 paragraphs)", 
                                                           "Medium (3-5paragraphs)", 
                                                           "Long (detailed explanation) "])

# template
template = PromptTemplate(
    template="""
    Please summarize the research paper titled "{paper_input}" with the following specifications:
    Explanation Style: {style_input}
    Explanation Length: {length_input}
    1. Mathematical Details:
    - Include relevant mathematical equations if present in the paper.
    - Explain the mathematical concepts using simple, intuitive code snippets where applicable.
    2. Analogies:
    - Use relatable analogies to simplify complex ideas.
    If certain information is not available in the paper, respond with: "Insufficient information available" instead of guessing.
    Ensure the summary is clear, accurate, and aligned with the provided style and
    """,
    input_variables=['paper_input','style_input',"length_input"]
    
)

# # ---> Fill the Placehodlers
# prompt = template.invoke({
#     'paper_input':paper_input,
#     'style_input':style_input,
#     'length_input':length_input
# })

# if st.button('Summarize'):
#     answer = model.invoke(prompt)
#     st.write(answer.content)
    
# Using Chains
if st.button('Summarize'):
    chain = template | model
    # answer = model.invoke(prompt)
    answer = chain.invoke({
        'paper_input':paper_input,
        'style_input':style_input,
        'length_input':length_input
    })
    st.write(answer.content)