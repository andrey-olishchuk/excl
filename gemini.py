import google.generativeai as genai
from langchain_core.prompts import PromptTemplate


def embed_content(text):
    result = genai.embed_content(model="models/text-embedding-004", content=text)

    return result['embedding']

def prompt(text, documents):
    document = ""
    for d in documents:
        if document:
            document = document + " And less important source:" + d.payload["source"]
        else: 
            document = " The very first and most relevant source to search within is: " + d.payload["source"]

    llm_prompt = f'User input: {text}. Search exclusively in the following content with no exceptions and create an answer strictly extracted from the following texts: {document}. Answer: '

    model = genai.GenerativeModel(
        "gemini-1.5-pro", 
        system_instruction=[
            "You are a helpful cloud engineer and developer",
            "Your mission is to help to another engineers find answers, recepies and information about how to resolve their technical challenges.",
        ]
    )
    result = model.generate_content(llm_prompt)

    return result.text