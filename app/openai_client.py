from openai import OpenAI
from app.config import get_openai_api_key
import logging

def get_openai_client() -> OpenAI:
    try:
        api_key = get_openai_api_key()
        client = OpenAI(api_key=api_key)
        logging.info("API OpenAI conectada com sucesso")
        return client
    except Exception as e:
        logging.error(f"Erro ao conectar com OpenAI: {e}")
        raise
