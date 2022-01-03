from flask import Flask, render_template

app = Flask(__name__)

#Flask é um framework de desenvolvimento de sites e Apis
# 01. pip install Flask
# 02. importar o flask
# 03. criar a primeira página do site.
# 03.01. route (caminho depois do domínio)
@app.route("/") # Isso é um decorator (uma linha de código que tem como objetivo atribuir uma nova funcionalidade pra função que vem logo abaixo dela)
# 03.02. função (o que você quer exibir naquela página)
# 03.03. template
def homepage():
    return render_template("homepage.html")

@app.route("/contatos")
def contatos():
    return render_template("contatos.html")

@app.route("/usuarios/<nome_usuario>")
def usuarios(nome_usuario):
    return render_template("usuarios.html", nome_usuario=nome_usuario)

# 04. colocar o site no ar.
if __name__ == "__main__":
    app.run(debug=True)
# 05. Colocar o site no servidor do Heroku
# 05.01. Criar uma conta no Heroku
# 05.02. Criar um app dentro da Heroku
# 05.03. Instalar Heroku CLI e instalar Git
# 05.04. Criar Procfile e inserir informações dentro dele
# 05.05. pip install gunicorn
# 05.06. Criar arquivo requirements.txt, pip freeze > requirements.txt
# 05.07. Seguir passo a passo do Heroku
# 05.07.01. Estar na pasta do projeto
# 05.07.02. Login heroku login
# 05.07.03. git init (se não estiver iniciado git config --global user.email "", git config --global user.name ""
# 05.07.04. heroku git:remote -a siteflaskyoutube
# 05.08. Deploy
# 05.08.01. git add .
# 05.08.02. git commit -am "make it better"
# 05.08.03. git push heroku master