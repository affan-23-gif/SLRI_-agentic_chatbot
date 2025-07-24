from typing import Any

class MockLLM:
    """
    A simple mock Large Language Model for demonstration and testing purposes.
    It provides predefined responses based on keywords in the prompt.
    In a real application, this would be replaced by an actual LLM integration
    (e.g., OpenAI, Google Gemini, HuggingFace Inference API).
    """
    def generate_response(self, prompt: str) -> str:
        """
        Simulates an LLM generating a response based on the input prompt.
        """
        prompt_lower = prompt.lower()

        if "what kpis were tracked" in prompt_lower:
            return "Based on the provided context, the KPIs tracked in Q1 included revenue, customer acquisition cost, and conversion rate. [cite: file: sales_review.md] [cite: file: metrics.pdf]"
        elif "revenue" in prompt_lower and "q1" in prompt_lower:
            return "According to the sales review, Q1 revenue was $1.2M. The metrics report also indicates revenue of $1.5 Million. [cite: file: sales_review.md] [cite: file: metrics.pdf]"
        elif "customer acquisition cost" in prompt_lower or "cac" in prompt_lower:
            return "The Customer Acquisition Cost (CAC) for Q1 was $50. [cite: file: sales_review.md]"
        elif "net promoter score" in prompt_lower or "nps" in prompt_lower:
            return "The Net Promoter Score (NPS) for Q1 was 45. [cite: file: metrics.pdf]"
        elif "test document" in prompt_lower:
            return "The test document mentions that revenue was up by 10% in Q1. [cite: file: example.txt]"
        elif "not enough information" in prompt_lower or "don't have enough information" in prompt_lower:
            return "I don't have enough information in the provided context to answer that question."
        else:
            # Default response if no specific keyword is matched
            return "I am a mock LLM. My response is based on the provided context. If you asked a specific question about KPIs, revenue, or customer acquisition, I might have a more detailed answer. Otherwise, I acknowledge your input."

