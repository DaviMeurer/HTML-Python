from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def RotaInicial():
    return "Hello World da API"

@app.route('/bemvindo')
def ExemploJSON():
    return jsonify(
        {
            "mensagem":"Eu sou um JSON"
        }
    )

if __name__ == "__main__":
    app.run(debug=True)