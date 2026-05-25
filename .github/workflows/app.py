from flask import Flask
app = Flask(__name__)

# ❌ La clé secrète qui va faire rater le test Gitleaks
AWS_SECRET_KEY = "AKIAIMXFFAFAKEKEY12345" 

@app.route('/')
def hello():
    return "Mon app de soutenance !"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
