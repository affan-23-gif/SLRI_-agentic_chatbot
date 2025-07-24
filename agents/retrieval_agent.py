from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings  

from core.mcp import MCPMessage

class RetrievalAgent:
    def __init__(self):
        self.embeddings = OpenAIEmbeddings()
        self.vectordb = None

    def index_chunks(self, chunks):
        self.vectordb = FAISS.from_texts(chunks, embedding=self.embeddings)

    def retrieve(self, query, trace_id):
        docs = self.vectordb.similarity_search(query, k=5)
        return MCPMessage(
            sender="RetrievalAgent",
            receiver="LLMResponseAgent",
            type_="RETRIEVAL_RESULT",
            trace_id=trace_id,
            payload={
                "retrieved_context": [d.page_content for d in docs],
                "query": query
            }
        )

    def handle(self, mcp_message):
        if mcp_message.type == "DOC_PARSED":
            self.index_chunks(mcp_message.payload["chunks"])
