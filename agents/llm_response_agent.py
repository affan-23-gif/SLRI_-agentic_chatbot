from core.mcp import MCPMessage
from langchain.chat_models import ChatOpenAI
from langchain.chains.question_answering import load_qa_chain
from langchain.prompts import PromptTemplate
from langchain.docstore.document import Document

class LLMResponseAgent:
    def __init__(self):
        self.llm = ChatOpenAI(temperature=0)
        self.chain = load_qa_chain(self.llm, chain_type="stuff")

    def handle(self, mcp_message):
        docs = [Document(page_content=chunk) for chunk in mcp_message.payload["retrieved_context"]]
        query = mcp_message.payload["query"]
        answer = self.chain.run(input_documents=docs, question=query)

        return {
            "answer": answer,
            "sources": docs
        }
