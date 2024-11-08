from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

lista_produtos = [
        {"id": 1, "nome": "Cookie Recheado de Chocolate", "preco": 8, "quantidade": 15, "imagem": "cookies.jpg"},
        {"id": 2, "nome": "Pão de Mel", "preco": 8, "quantidade": 10, "imagem": "pao de mel.jfif"},
        {"id": 3, "nome": "Palha Italiana de Ninho", "preco": 7, "quantidade": 10, "imagem": "palha ninho.jpg"},
        {"id": 4, "nome": "Palha Italiana de Chocolate", "preco": 7, "quantidade": 10, "imagem": "palha brigadeiro.jpg"},
        {"id": 5, "nome": "Biscoitos Decorados", "preco": 6, "quantidade": 10, "imagem": "biscoitos.jpg"},
        {"id": 6, "nome": "Kit Biscoitos Recheados", "preco": 15, "quantidade": 10, "imagem": "kit biscoitos.jpg"},
    ]

@app.route('/')
def home():
    # Lista de produtos com nome, preço e quantidade
    
    return render_template('index.html', produtos=lista_produtos)

# Rota para exibir todos os produtos
@app.route('/produtos')
def produtos():
    return render_template('produtos.html', produtos=lista_produtos)

# Rota para simular a compra de um produto
@app.route('/comprar/<int:produto_id>')
def comprar(produto_id):
    produto = next((p for p in lista_produtos if p["id"] == produto_id), None)
    if produto:
        return render_template('comprar.html', produto=produto)
    return redirect(url_for('home'))

# Rota para o formulário de contato
@app.route('/contato', methods=['GET', 'POST'])
def contato():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        mensagem = request.form['mensagem']
        # Aqui você pode processar o envio, salvar em um banco de dados ou enviar um e-mail
        return redirect(url_for('home'))  # Simulando um envio com redirecionamento
    return render_template('contato.html')

# Rota para ver a história da loja
@app.route('/sobre')
def sobre():
    return render_template('sobre.html')

if __name__ == '_main_':
    app.run(debug=True)