from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

lista_produtos = [
        {"id": 1, "nome": "Cookie Recheado de Chocolate", "preco": 10, "quantidade": 15, "imagem": "cookies.jpg"},
        {"id": 2, "nome": "Pão de Mel", "preco": 8, "quantidade": 10, "imagem": "pao de mel.jfif"},
        {"id": 3, "nome": "Palha Italiana de Ninho", "preco": 15, "quantidade": 10, "imagem": "palha ninho.jpg"},
        {"id": 4, "nome": "Palha Italiana de Chocolate", "preco": 15, "quantidade": 10, "imagem": "palha brigadeiro.jpg"},
        {"id": 5, "nome": "Biscoitos Decorados (4 unidades)", "preco": 20, "quantidade": 10, "imagem": "biscoitos.jpg"},
        {"id": 6, "nome": "Kit Confeiteiro (4 unidades)", "preco": 50, "quantidade": 10, "imagem": "kit biscoitos.jpg"},
        {"id": 7, "nome": "Brownie com Nozes", "preco": 10, "quantidade": 10, "imagem": "brownies com nozes.jpg"},
        {"id": 8, "nome": "Caixa de Alfajor (6 unidades)", "preco": 40, "quantidade": 11, "imagem": "Alfajor.jpg"},
        {"id": 9, "nome": "Pote de Casadinhos de Doce de Leite (12 unidades)", "preco": 50, "quantidade": 8, "imagem": "12 casadinhos.jpg"},
        {"id": 10, "nome": "Kit Casinha", "preco": 90, "quantidade": 10, "imagem": "kit casinha.jpg"},
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
    feedback= None
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        mensagem = request.form['mensagem']
        # Aqui você pode processar o envio, salvar em um banco de dados ou enviar um e-mail
        feedback = "Agradecemos por seu feedback. Fique de olho em seu email que logo entraremos em contato!"
    return render_template('contato.html', feedback = feedback)

# Rota para ver a história da loja
@app.route('/sobre')
def sobre():
    return render_template('sobre.html')

if __name__ == '_main_':
    app.run(debug=True)