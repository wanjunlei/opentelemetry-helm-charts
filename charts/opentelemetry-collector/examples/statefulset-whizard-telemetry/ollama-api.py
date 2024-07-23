import openlit
import asyncio
import ollama
from ollama import Client
from ollama import AsyncClient

openlit.init(otlp_endpoint="http://172.31.18.2:30318")

# Refer to ollama-python for more info: https://github.com/ollama/ollama-python
# Calling ollama API with a custom client

def chat_with_custom_client():
  client = Client(host='http://localhost:11434')
  response = client.chat(model='llama3', messages=[
    {
      'role': 'user',
      'content': 'Why is the sky blue?',
    },
  ])
  print(f"Ollama: {response}")

def chat_in_stream():
  stream = ollama.chat(
      model='llama3',
      messages=[{'role': 'user', 'content': 'Why is the sky blue?'}],
      stream=True,
  )
  for chunk in stream:
    print(chunk['message']['content'], end='', flush=True)

# async client with non-stream response
async def chat_async():
  message = {'role': 'user', 'content': 'Why is the sky blue?'}
  response = await AsyncClient().chat(model='llama3', messages=[message])
  print(f"Ollama: {response}")

# async client with stream response
async def chat_async_in_stream():
  message = {'role': 'user', 'content': 'Why is the sky blue?'}
  async for part in await AsyncClient().chat(model='llama3', messages=[message], stream=True):
    print(part['message']['content'], end='', flush=True)

#asyncio.run(chat_async())
#asyncio.run(chat_async_in_stream())
chat_in_stream()
