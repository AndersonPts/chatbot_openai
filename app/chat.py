import logging

def start_chat(client):
    print("ChatGPT - Terminal (digite 'sair' para encerrar)\n")
    messages = []

    while True:
        user_input = input("Você: ")
        if user_input.strip().lower() == "sair":
            print("Encerrando...")
            break

        messages.append({"role": "user", "content": user_input})

        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=messages,
                max_tokens=1000,
                temperature=0.7
            )
            reply = response.choices[0].message.content
            print(f"ChatGPT: {reply}\n")
            messages.append({"role": "assistant", "content": reply})
        except Exception as e:
            logging.error(f"Erro ao gerar resposta: {e}")
