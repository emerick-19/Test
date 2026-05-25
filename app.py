from flask import Flask

app = Flask(__name__)

# ❌ FAILLE DE SÉCURITÉ : Une clé secrète ne doit JAMAIS être écrite en dur dans le code
AWS_SECRET_KEY = "AKIAIMXFFAFAKEKEY12345" 

@app.route('/')
def hello():
    return "Mon application pour ma soutenance !"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
