import os
from dotenv import load_dotenv

load_dotenv()

def get_openai_api_key() -> str:
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        raise ValueError('A chave da API não foi encontrada no arquivo .env')
    return api_key
