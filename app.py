from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Mon application securisee !"

if __name__ == '__main__':
    # On ajoute le commentaire d'arrêt tout au bout de la ligne 13
    app.run(host='0.0.0.0', port=5000)  # nosemgr
