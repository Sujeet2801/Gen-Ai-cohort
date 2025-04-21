import os
import genai

# Set your API key directly in the script
os.environ['GOOGLE_API_KEY'] = 'your_api_key_here'

# Initialize the client
client = genai.Client()

# Generate content
response = client.models.generate_content(
    model='gemini-2.0-flash',  # Use the appropriate model name
    contents='Why is the sky blue?'
)

print(response.text)
