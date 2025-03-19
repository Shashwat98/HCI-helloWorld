
import requests

# Set up the Hugging Face API endpoint and token
API_URL = "https://api-inference.huggingface.co/models/gpt2"
API_TOKEN = "####"   #Remove the API token after running it succesfully to prevent sharing it.

headers = {
    "Authorization": f"Bearer {API_TOKEN}"
}

# The input prompt for text generation
data = {
    "inputs": "Say Hello World in a creative way, just use a single sentence."
}

# Send the POST request to Hugging Face API
response = requests.post(API_URL, headers=headers, json=data)

# Check if the request was successful
if response.status_code == 200:
    result = response.json()
    generated_text = result[0]['generated_text']
    print(f"Generated Text: {generated_text}")
else:
    print(f"Error: {response.status_code}")
    print(response.text)
