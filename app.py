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
    return render_template ('t_index.html', nome='Grazielle') 
                                        
@app_grazi.route('/usuario')
def dados_usuario():
    dados_usu = {"nome": "Grazielle", "profissão": "Estagiária", "disciplina": "Desenvolvimento Web III"}
    return render_template("t_usuario.html", dados=dados_usu)

@app_grazi.route('/usuario/<id>')       #nova rota para exibir saudacao personalizada
def saudacao(id):
    return render_template('t_homepage_nome.html', nome=id)

#acrescenta três parâmetros (nome_usuario, nome_profissao, nome_disciplina)
@app_grazi.route('/usuario/<nome_usuario>;<nome_profissao>;<nome_disciplina>') 
def usuario(nome_usuario, nome_profissao, nome_disciplina):
    dados_usu = {"profissão": nome_profissao, "disciplina": nome_disciplina}
    return render_template("t_usuario.html", nome=nome_usuario, dados = dados_usu)

if __name__ == "__main__":  
    app_grazi.run(port=8880)
    

