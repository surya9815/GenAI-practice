from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

load_dotenv()

embedding = OpenAIEmbeddings(model='text-embedding-3-large', dimensions=300)
documents = [
    "Virat Kohli is an Indian cricketer known for his aggressive batting and leadership.",
    "MS Dhoni is a former Indian captain famous for his calm demeanor and finishing skills.",
    "Sachin Tendulkar, also known as the 'God of Cricket', holds many batting records.",
    "Rohit Sharma is known for his elegant batting and record-breaking double centuries."
    "Jasprit Bumrah is an Indian Fast Bowler known for his aggressive bowling and yorker."
]

query = 'tell me about virat kohli'

document_embedding = embedding.embed_documents(documents)   #document embeddings
query_embedding = embedding.embed_query(query)      #query embedding

                    # | 2 D list
similarity_scores = cosine_similarity([query_embedding],document_embedding)     #--> used SKlearn to find the similarity between vectors

index, score = sorted(list(enumerate(similarity_scores)), key=lambda x:x[1])[-1]

print(documents[index]) #--> the most similar document

