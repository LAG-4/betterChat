import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
if not os.getenv("GOOGLE_API_KEY"):
    raise ValueError("GOOGLE_API_KEY environment variable is not set.")
os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")

client = genai.Client()
search_tool= types.Tool(
    google_search=types.GoogleSearch()
)
config= types.GenerateContentConfig(
    tools=[search_tool],

)


response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Latest news about microsoft",
    config=config,
)

print(response.text)