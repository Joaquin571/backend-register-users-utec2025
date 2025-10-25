import os
import requests

NOTIFY_BASE = os.getenv("NOTIFY_BASE", "http://127.0.0.1:8081")
NOTIFY_TOKEN = os.getenv("NOTIFY_TOKEN", "dev-secret")
NOTIFY_TIMEOUT = float(os.getenv("NOTIFY_TIMEOUT", "3"))

def send_welcome_email(to_email: str, name: str, phone: str):
    """
    Llama al Notification Service para enviar el email de bienvenida.
    Levanta excepción si el servicio responde != 2xx.
    """
    url = f"{NOTIFY_BASE}/notify/email/welcome"
    payload = {"to": to_email, "name": name, "phone": phone}
    headers = {
        "Authorization": f"Bearer {NOTIFY_TOKEN}",
        "Content-Type": "application/json",
    }

    resp = requests.post(url, json=payload, headers=headers, timeout=NOTIFY_TIMEOUT)
    resp.raise_for_status() 
    return resp.json() if resp.content else {}
