import uuid

import chromadb
import streamlit as st
from sentence_transformers import SentenceTransformer, util

@st.cache_resource
def load_model():
    return SentenceTransformer('all-MiniLM-L6-v2')

client = chromadb.Client()
collection = client.get_or_create_collection(name="knowledge_base")

def add_to_knowledge_base(chunks):
    
    model = load_model()

    embeddings = model.encode(chunks).tolist()

    ids = [str(uuid.uuid4()) for _ in chunks]

    collection.add(
        ids=ids,
        documents=chunks,
        embeddings=embeddings
    )

def search_knowledge_base(query):

    model = load_model()

    query_embedding = model.encode(query).tolist()

    search_results = collection.query(
        query_embeddings=[query_embedding],
        n_results=3
    )
    
    return search_results["documents"][0]