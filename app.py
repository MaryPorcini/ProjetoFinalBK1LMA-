from flask import Flask, render_template, request, redirect, url_for
import json
import os

app = Flask(__name__)
app.secret_key = 'supersecretkey'

CONTATOS_FILE = "contatos.json"
PRODUTOS_FILE = "produtos.json"

def save_contato_to_file(data):
    if os.path.exists(CONTATOS_FILE):
        with open(CONTATOS_FILE, "r") as file:
            contatos = json.load(file)
    else:
        contatos = []

    contatos.append(data)

    with open(CONTATOS_FILE, "w") as file:
        json.dump(contatos, file, indent=4)

def save_compra_to_file(data):
    if os.path.exists(PRODUTOS_FILE):
        with open(PRODUTOS_FILE, "r") as file:
            compras = json.load(file)
    else:
        compras = []

    compras.append(data)

    with open(PRODUTOS_FILE, "w") as file:
        json.dump(compras, file, indent=4)

lista_produtos = [
    {"id": 1, "nome": "Cookie Recheado de Chocolate", "preco": 10, "imagem": "cookies.jpg"},
    {"id": 2, "nome": "Pão de Mel", "preco": 8, "imagem": "pao de mel.jfif"},
    {"id": 3, "nome": "Palha Italiana de Ninho", "preco": 15, "imagem": "palha ninho.jpg"},
    {"id": 4, "nome": "Palha Italiana de Brigadeiro", "preco": 15, "imagem": "palha brigadeiro.jpg"},
    {"id": 5, "nome": "Biscoitos Decorados (4 unidades)", "preco": 20, "imagem": "biscoitos.jpg"},
    {"id": 6, "nome": "Kit Confeiteiro (4 unidades)", "preco": 50, "imagem": "kit biscoitos.jpg"},
    {"id": 7, "nome": "Brownie com Nozes", "preco": 10, "imagem": "brownies com nozes.jpg"},
    {"id": 8, "nome": "Caixa de Alfajor (6 unidades)", "preco": 40, "imagem": "Alfajor.jpg"},
    {"id": 9, "nome": "Pote de Casadinhos de Doce de Leite (12 unidades)", "preco": 50, "imagem": "12 casadinhos.jpg"},
    {"id": 10, "nome": "Kit Casinha", "preco": 90, "imagem": "kit casinha.jpg"},
]

@app.route('/')
def home():
    return render_template('index.html', produtos=lista_produtos)

@app.route('/produtos')
def produtos():
    return render_template('produtos.html', produtos=lista_produtos)

@app.route('/comprar/<int:produto_id>', methods=['GET', 'POST'])
def comprar(produto_id):
    produto = next((p for p in lista_produtos if p["id"] == produto_id), None)
    if produto:
        if request.method == 'POST':
            quantidade = int(request.form['quantidade'])
            nome = request.form['nome']
            localizacao = request.form['localizacao']
            entrega = request.form['entrega']
            valor_total = produto["preco"] * quantidade
            
            # Criando o dicionário com os dados da compra, incluindo nome e localização
            compra_data = {
                'produto_id': produto['id'],
                'nome_produto': produto['nome'],
                'quantidade': quantidade,
                'valor_total': valor_total,
                'nome_comprador': nome,
                'localizacao_comprador': localizacao,
                'data_entrega' : entrega,
            }

            # Salvando a compra no arquivo JSON
            save_compra_to_file(compra_data)
            
            # Passando os dados para o template para exibir ao usuário
            return render_template('comprar.html', 
                                   produto=produto, 
                                   compra_concluida=True, 
                                   valor_total=valor_total, 
                                   quantidade=quantidade, 
                                   nome=nome, 
                                   localizacao=localizacao,
                                   entrega=entrega)
        
        return render_template('comprar.html', produto=produto)
    return redirect(url_for('home'))

# Rota para o formulário de contato
@app.route('/contato', methods=['GET', 'POST'])
def contato():
    feedback = None
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        mensagem = request.form['mensagem']

        # Criando o dicionário com os dados do contato
        contato_data = {
            'nome': nome,
            'email': email,
            'mensagem': mensagem
        }

        # Salvando os dados no arquivo JSON
        save_contato_to_file(contato_data)

        feedback = "Agradecemos por seu feedback. Fique de olho em seu email que logo entraremos em contato!"
    
    return render_template('contato.html', feedback=feedback)

@app.route('/sobre')
def sobre():
    return render_template('sobre.html')

if __name__ == '__main__':
    app.run(debug=True)
