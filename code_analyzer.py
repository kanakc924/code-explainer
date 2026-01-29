import os
import time
import google.generativeai as genai
from typing import Optional
from dotenv import load_dotenv

load_dotenv()

class CodeAnalyzer:
    def __init__(self, api_key: Optional[str] = None):
        """
        Initialize the Gemini AI model.
        """
        self.api_key = api_key or os.getenv("GOOGLE_API_KEY")
        if not self.api_key:
            raise ValueError("Google API Key not found. Please set GOOGLE_API_KEY in .env file.")
        
        genai.configure(api_key=self.api_key)
        
        # Configuration for the model
        generation_config = {
            "temperature": 0.7,
            "top_p": 1,
            "top_k": 1,
            "max_output_tokens": 8192,
        }
        
        self.model = genai.GenerativeModel(
            model_name="gemini-3-pro-preview",
            generation_config=generation_config
        )

    def analyze_code(self, prompt: str) -> str:
        """
        Send the prompt to Gemini and return the response.
        """
        try:
            response = self.model.generate_content(prompt)
            if response.text:
                return response.text
            else:
                return "AI returned an empty response. Please try again."
        except Exception as e:
            return f"Error during analysis: {str(e)}"

    def analyze_with_retry(self, prompt: str, max_retries: int = 3) -> str:
        """
        Send prompt with a simple retry logic for rate limiting or transient errors.
        """
        for i in range(max_retries):
            try:
                return self.analyze_code(prompt)
            except Exception as e:
                if i == max_retries - 1:
                    return f"Failed after {max_retries} attempts: {str(e)}"
                time.sleep(2 ** i) # Exponential backoff
        return "Unknown error occurred during analysis."

    def check_api_status(self) -> bool:
        """
        Verify if the API key is valid and service is reachable.
        """
        try:
            # Simple probe
            self.model.generate_content("Ping")
            return True
        except Exception:
            return False
