from agents.ingestion_agent import IngestionAgent
from agents.retrieval_agent import RetrievalAgent
from agents.llm_response_agent import LLMResponseAgent
from dotenv import load_dotenv
load_dotenv()


def main_pipeline(query, trace_id="rag-001"):
    # Agents
    ingest = IngestionAgent()
    retrieve = RetrievalAgent()
    llm = LLMResponseAgent()

    # Step 1: Ingestion
    msg1 = ingest.handle(trace_id)
    # Step 2: Indexing
    retrieve.handle(msg1)
    # Step 3: Retrieval
    msg2 = retrieve.retrieve(query, trace_id)
    # Step 4: LLM Answering
    result = llm.handle(msg2)
    return result
