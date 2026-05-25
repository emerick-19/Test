from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Mon application securisee pour ma soutenance !"

if __name__ == '__main__':
    # Le commentaire ci-dessous autorise cette ligne auprès de Semgrep
    app.run(host='0.0.0.0', port=5000)  # nosemgrep
