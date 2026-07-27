from google import genai
from dotenv import load_dotenv
from pathlib import Path
import os

# Load the .env file from the backend folder
env_path = Path(__file__).resolve().parents[2] / ".env"
load_dotenv(dotenv_path=env_path)

# Read the API key
API_KEY = os.getenv("GEMINI_API_KEY")

# Check if the key was loaded
if not API_KEY:
    raise ValueError(
        "GEMINI_API_KEY not found. Make sure your .env file is in the backend folder."
    )

# Create Gemini client
client = genai.Client(api_key=API_KEY)


def ask_gemini(prompt):
    """
    Sends a prompt to Gemini and returns the generated response.
    """

    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=prompt
    )

    return response.text


# Test the connection
if __name__ == "__main__":
    reply = ask_gemini("Say hello in one sentence.")
    print(reply)