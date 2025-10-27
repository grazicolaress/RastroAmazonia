from flask import Flask

app_grazi = Flask (__name__)

@app_grazi.route('/')
def raiz():
    return 'Olá, turma!'

app_grazi.run()
