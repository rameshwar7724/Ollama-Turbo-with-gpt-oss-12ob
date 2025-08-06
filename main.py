import ollama
from ollama import Client

client = Client( 
                host = "https://ollama.com",
                headers = {
                    "Authorization": "24cbdcb5310048e695a459826d7449cc.yvuY6OFZrzRP9q_XZmtjFDGk"
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
    
    