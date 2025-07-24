from langchain_community.document_loaders import (
    PyPDFLoader,
    TextLoader,
    UnstructuredWordDocumentLoader,
    UnstructuredPowerPointLoader,
    CSVLoader
)
from core.mcp import MCPMessage
import os

class IngestionAgent:
    def __init__(self, folder="documents"):
        self.folder = folder

    def parse_documents(self):
        chunks = []
        for file in os.listdir(self.folder):
            path = os.path.join(self.folder, file)
            if file.endswith(".pdf"):
                chunks += PyPDFLoader(path).load()
            elif file.endswith(".txt") or file.endswith(".md"):
                chunks += TextLoader(path).load()
            elif file.endswith(".docx"):
                chunks += UnstructuredWordDocumentLoader(path).load()
            elif file.endswith(".pptx"):
                chunks += UnstructuredPowerPointLoader(path).load()
            elif file.endswith(".csv"):
                chunks += CSVLoader(path).load()
        return chunks

    def handle(self, trace_id):
        chunks = self.parse_documents()
        return MCPMessage(
            sender="IngestionAgent",
            receiver="RetrievalAgent",
            type_="DOC_PARSED",
            trace_id=trace_id,
            payload={"chunks": [chunk.page_content for chunk in chunks]}
        )
