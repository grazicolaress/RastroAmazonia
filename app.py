from flask import Flask, render_template, request, redirect, url_for, session, jsonify #algumas libs importantes
import json
import os

app = Flask(__name__, template_folder='t_templates')


#dados simulados dos animais
animais = [
    {
        'id': 1,
        'nome': 'Boto Cor-de-Rosa',
        'especie': 'Inia geoffrensis',
        'foto': 'boto.jpg',
        'historia': 'Boto monitorado na região do Rio Amazonas...',
        'localizacao': '-3.1190, -60.0217'
    },
    {
        'id': 2,
        'nome': 'Onça-pintada',
        'especie': 'Panthera onca',
        'foto': 'onca.jpg',
        'historia': 'Onça monitorada na Reserva Extrativista...',
        'localizacao': '-4.4419, -61.4474'
    }
]


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST']) #é para aceitar os dois metodos
def login():
    if request.method == 'POST':  #se for envio de form
        email = request.form['email']
        senha = request.form['senha']
        #validação simples
        return redirect(url_for('galeria')) 
    return render_template('t_login.html') #se for acessar normal




if __name__ == '__main__':
    app.run(debug=True, port=8880)