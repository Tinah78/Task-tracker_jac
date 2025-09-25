from dotenv import load_dotenv
import os
from task import Task

# Load .env file
load_dotenv()

# Import Gemini client
from google import genai

def get_gemini_client():
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("GEMINI_API_KEY not found. Please set it in your .env file.")
    
    # Initialize Gemini client
    client = genai.Client(api_key=api_key)
    return client

def suggest_task(task_list):
    incomplete_tasks = [t for t in task_list if not t.completed]
    if not incomplete_tasks:
        print("All tasks are complete!")
        return

    client = get_gemini_client()

    # Create a prompt for Gemini
    prompt = f"I have these tasks: {[t.title for t in incomplete_tasks]}. Which one should I do next and why?"

    # Generate AI suggestion
    response = client.models.generate_content(
        model="gemini-2.5-flash",  # Or any Gemini model you have access to
        contents=prompt
    )

    suggestion = response.text.strip()
    print(f"Gemini AI suggests you complete: '{suggestion}'")