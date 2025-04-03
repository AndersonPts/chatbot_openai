import logging
from app.openai_client import get_openai_client
from app.chat import start_chat

#logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

if __name__ == "__main__":
    client = get_openai_client()
    start_chat(client)
