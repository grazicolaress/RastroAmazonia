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
                                        

#removido def dados_usuarios
#adicionado rota SEM parâmetros com defaults
@app_grazi.route('/usuario', defaults={"nome_usuario": "usuário", "nome_profissao": "Não informado", "nome_disciplina": "Não informada"})
@app_grazi.route('/usuario/<nome_usuario>;<nome_profissao>;<nome_disciplina>') 
def usuario(nome_usuario, nome_profissao, nome_disciplina):
    dados_usu = {"nome":nome_usuario, "profissão": nome_profissao, "disciplina": nome_disciplina}
    return render_template("t_usuario.html", nome=nome_usuario, dados=dados_usu)


@app_grazi.route('/usuario/<id>')       #rota de usuario com id para saudação personalizada
def saudacao(id):
    return render_template('t_homepage_nome.html', nome=id)

if __name__ == "__main__":  
    app_grazi.run(port=8880)
    

