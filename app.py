from flask import Flask, render_template

app_grazi = Flask (__name__, template_folder='t_templates')

@app_grazi.route('/') 
def homepage():
    return render_template ('homepage.html')

@app_grazi.route('/contato')
def contato():
    return render_template('contato.html')

@app_grazi.route('/index')
def indice():
    return render_template ('t_index.html', nome='Grazielle') #passa a variável nome para aparecer na tela

@app_grazi.route('/usuario') #nova rota para perfil de usuario
def dados_usuario():
    dados_usu = {"nome":"Grazielle", "profissão":"Estagiária", "disciplina":"Desenvolvimento Web III"}
    return render_template("t_usuario.html", dados = dados_usu)

if __name__ == "__main__":  
    app_grazi.run(port=8880)
