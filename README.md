# Document Indexing and Retrieval with Qdrant and Vertex AI Gemini-pro

This application is designed to index documents and store their vector embeddings in Qdrant, facilitating efficient document retrieval. It utilizes Vertex AI's Gemini-pro 1.5 model for generating embeddings and performing Retrieval-Augmented Generation (RAG) consultations directly from the command line. This README will guide you through the main features and how to use the application.

## Features

1. **Document Indexing**: The application reads documents from a specified directory, generates vector embeddings using the Gemini-pro model, and stores these embeddings along with document metadata in Qdrant.
2. **Vector-Based Retrieval**: By embedding user queries, the application can search for and retrieve relevant documents from Qdrant based on the similarity of their vector embeddings.
3. **RAG Consultation**: The application leverages the power of Vertex AI Gemini-pro to generate answers to user queries by retrieving relevant documents and using them to provide contextually accurate responses.
4. **Command-Line Interface**: The application provides a simple CLI for indexing documents, asking questions, and managing collections.

## Usage

### Indexing Documents

To index documents from a folder, use the `index` command. This command reads all `.txt` files in the specified folder, generates vector embeddings for their content, and stores these embeddings in Qdrant.

```sh
python main.py index <folder_path> --collection <collection_name>
```

### Asking Questions

To ask a question and get a contextually accurate answer based on the indexed documents, use the `ask` command. This command embeds the question, retrieves relevant documents, and generates a response.

```sh
python main.py ask --question "Your question here"
```

### Managing Collections

To manage your document collections, use the `kickoff` command. This command can be used to perform initialization tasks or to reset the state of a collection.

```sh
python main.py kickoff <collection_name>
```
