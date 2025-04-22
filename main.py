from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
import requests
import os

app = FastAPI()

BOT_TOKEN = os.getenv("BOT_TOKEN", "7706661575:AAEZtx8PPFZWAg5yXkCbwxV4t65FfjS0IS8")
CHAT_ID = os.getenv("CHAT_ID", "-1002329823291")
API_URL = f"https://api.telegram.org/bot{BOT_TOKEN}"

@app.get("/")
def root():
    return {"message": "CryptoBot Promoter API rodando na nuvem 🚀"}

@app.post("/webhook")
async def webhook(request: Request):
    payload = await request.json()
    print("Recebido do Telegram:", payload)

    # Responder automaticamente se for mensagem de texto
    if "message" in payload and "text" in payload["message"]:
        chat_id = payload["message"]["chat"]["id"]
        user_text = payload["message"]["text"]
        resposta = f"Você disse: {user_text} 🤖"

        requests.post(f"{API_URL}/sendMessage", json={
            "chat_id": chat_id,
            "text": resposta
        })

    return {"status": "ok"}

@app.post("/send_message")
async def send_message(request: Request):
    data = await request.json()
    message = data.get("message", "")

    requests.post(f"{API_URL}/sendMessage", json={
        "chat_id": CHAT_ID,
        "text": message
    })

    return {"status": "mensagem enviada", "message": message}

@app.get("/painel", response_class=HTMLResponse)
def painel():
    with open("painel.html", "r", encoding="utf-8") as f:
        return f.read()
