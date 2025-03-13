from flask import Flask, url_for, render_template

#Inicialização
app = Flask(__name__)


#Rotas
@app.route("/")
def ola_mundo():
    titulo = "Gestão de Usuários"
    usuarios = [
        {"nome": "Guilherme", "membro_ativo": True},
        {"nome": "João", "membro_ativo": False},
        {"nome": "Maria", "membro_ativo": False},
    ]
    return render_template("index.html", titulo=titulo, usuarios=usuarios)

@app.route("/sobre")
def pagina_sobre():
    return """ 
        <b>Programador Python</b>: assista os vídeos no 
        <a href="https://youtube.com/@programadorpython">Canal no Youtube</a>
    """
#execução
app.run(debug=True)