from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # Lista de produtos com nome, preço e quantidade
    produtos = [
        {"nome": "Cookie Recheado de Chocolate", "preco": 8, "quantidade": 15, "imagem": "doces.jpg"},
        {"nome": "Pão de Mel", "preco": 8, "quantidade": 10, "imagem": "doces.jpg"},
        {"nome": "Palha Italiana de Ninho", "preco": 7, "quantidade": 10, "imagem": "doces.jpg"},
        {"nome": "Palha Italiana de Chocolate", "preco": 7, "quantidade": 10, "imagem": "doces.jpg"},
    ]
    return render_template('index.html', produtos=produtos)

if __name__ == '__main__':
    app.run(debug=True)
