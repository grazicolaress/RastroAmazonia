from flask import Flask

app_grazi = Flask (__name__)

@app_grazi.route('/')
@app_grazi.route('/rota1') 
def rota1():
    return 'Olá, turma!'

@app_grazi.route('/rota2')
def rota2():
    resposta = "<h3> Essa é outra página da rota 2 <h3>"
    return resposta 

#@app_grazi.route('/ola/<nome>')
def saudacoes (nome):       #agora essa função não pertence a nenhuma rota
    return f'Olá, {nome}!'

if __name__ == "__main__":  
    app_grazi.run(port=8880)
