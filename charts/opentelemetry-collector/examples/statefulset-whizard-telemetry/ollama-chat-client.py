import requests
import openlit

openlit.init(otlp_endpoint="http://172.31.18.2:30318")

class OllamaChatClient:
    def __init__(self, api_url, api_key):
        self.api_url = api_url
        self.api_key = api_key
        self.headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.api_key}'
        }

    def send_message(self, message):
        payload = {
            'message': message
        }
        response = requests.post(self.api_url, headers=self.headers, json=payload)
        if response.status_code == 200:
            return response.json().get('response')
        else:
            response.raise_for_status()

if __name__ == "__main__":
    api_url = "http://host.docker.internal:11434/chat"  # Replace with your API URL
    api_key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6ImE2YTM1NmRhLTYwZWYtNDVlYS1iM2YwLTQ4YjgxOTg2Mzc4NyJ9.DwirBTQ7MjIKa_9mYcMswfvBh1WHknRI2cByHFRxYx0"  # Replace with your API key

    client = OllamaChatClient(api_url, api_key)

    print("Welcome to Ollama Chat! Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            break
        response = client.send_message(user_input)
        print(f"Ollama: {response}")