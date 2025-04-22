from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
import httpx

app = FastAPI()

TELEGRAM_TOKEN = "7706661575:AAEZtx8PPFZWAg5yXkCbwxV4t65FfjS0IS8"
CHAT_ID = "-1002329823291"

@app.get("/")
def root():
    return {"message": "CryptoBot Promoter API rodando na nuvem 🚀"}

@app.post("/send_message")
async def send_message(request: Request):
    data = await request.json()
    message = data.get("message", "")

    async with httpx.AsyncClient() as client:
        await client.post(
            f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage",
            json={"chat_id": CHAT_ID, "text": message}
        )

    return {"status": "mensagem enviada", "message": message}

@app.get("/painel", response_class=HTMLResponse)
def painel():
    with open("painel.html", "r", encoding="utf-8") as f:
        return f.read()
