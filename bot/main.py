import os
import openai
from dotenv import load_dotenv

# Завантаження ключа з .env
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

SYSTEM_PROMPT_FILE = "system_prompt.txt"
LOG_FILE = "output.txt"

# Завантаження системної інструкції
with open(SYSTEM_PROMPT_FILE, "r", encoding="utf-8") as f:
    system_prompt = f.read()

def log_message(role, content):
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"{role.upper()}: {content}\n")

messages = [{"role": "system", "content": system_prompt}]

print("CoffeeGo Bot запущено! Введіть свій запит або /exit для виходу.")

while True:
    user_input = input("Ви: ")
    if user_input.strip().lower() == "/exit":
        print("До зустрічі!")
        break
    elif user_input.strip().lower() == "/reset":
        messages = [{"role": "system", "content": system_prompt}]
        print("Контекст очищено!")
        continue

    messages.append({"role": "user", "content": user_input})
    log_message("user", user_input)

    response = openai.ChatCompletion.create(
        model="gpt-5-mini",
        messages=messages
    )

    reply = response.choices[0].message["content"]
    print("Бот:", reply)

    messages.append({"role": "assistant", "content": reply})
    log_message("assistant", reply)
