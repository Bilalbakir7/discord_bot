import random

messages = ["merhaba!", "Bonjour!", "こんにちは!", "안녕하세요!", "你好!", "नमस्ते!", "Привет!", "مرحبًا"]

def handle_response(message) -> str:
    p_message = message.lower()
    if p_message == 'Hello':
        return 'Hello how are you?'

    if p_message == 'roll':
        return str(random.randint(1, 6))
    if p_message == 'hello':
        randomMessage = random.choice(messages)
        return randomMessage
    if p_message == 'how are you':
        return 'I am fine thank you!'