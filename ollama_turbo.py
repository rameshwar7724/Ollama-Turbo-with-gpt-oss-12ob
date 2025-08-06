import ollama
from ollama import Client

client = Client( 
                host = "https://ollama.com",
                headers = {
                    "Authorization": "OLLAMA_API_KEY"
                }
)


messages = [
    {
        'role':'user',
        'content': 'What is todays date'
    }
]

for part in client.chat('gpt-oss:120b', messages = messages,stream=True):
    print(part['message']['content'],end='', flush=True)
    
    
