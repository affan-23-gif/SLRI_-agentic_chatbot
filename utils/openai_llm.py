import os
from typing import Any
from openai import OpenAI # pip install openai

class OpenAILLM:
    """
    Integrates with the OpenAI API to generate responses.
    The API key is loaded from an environment variable for security.
    """
    def __init__(self):
        # Load OpenAI API key from environment variable
        self.api_key = os.getenv("OPENAI_API_KEY")
        if not self.api_key:
            raise ValueError("OPENAI_API_KEY environment variable not set. Please set it to your OpenAI API key.")
        
        # Initialize the OpenAI client
        self.client = OpenAI(api_key=self.api_key)
        print("OpenAILLM: Initialized with OpenAI client.")

    def generate_response(self, prompt: str) -> str:
        """
        Sends a prompt to the OpenAI API and returns the generated response.
        Uses the 'gpt-3.5-turbo' model by default.
        """
        try:
            chat_completion = self.client.chat.completions.create(
                model="gpt-3.5-turbo", # You can change this to "gpt-4" or other models
                messages=[
                    {"role": "system", "content": "You are a helpful assistant that provides answers based on provided context."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7, # Controls randomness: lower for more deterministic, higher for more creative
                max_tokens=500, # Maximum number of tokens in the response
            )
            # Extract the content from the first choice's message
            response_content = chat_completion.choices[0].message.content
            return response_content
        except Exception as e:
            print(f"Error calling OpenAI API: {e}")
            return f"An error occurred while generating response from OpenAI: {e}"

