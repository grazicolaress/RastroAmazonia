from flask import Flask

app_grazi = Flask (__name__)

@app_grazi.route('/')
@app_grazi.route('/ola') 
def raiz():
    return 'Olá, turma!'

@app_grazi.route('/ola/<nome>')
def saudacoes (nome):       #função nova
    return f'Olá, {nome}!'

if __name__ == "__main__":  #verifica se o script está sendo executado diretamente    
    app_grazi.run(port=8880)
