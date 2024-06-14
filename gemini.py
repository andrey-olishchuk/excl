import google.generativeai as genai


def embed_content(text):
    result = genai.embed_content(model="models/text-embedding-004", content=text)

    return result['embedding']