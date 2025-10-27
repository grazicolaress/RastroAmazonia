from flask import Flask, render_template #nova biblioteca

app_grazi = Flask (__name__, template_folder='t_templates')

@app_grazi.route('/') 
def homepage():
    return render_template ('homepage.html')

@app_grazi.route('/contato')
def contato():
    return render_template("contato.html")

if __name__ == "__main__":  
    app_grazi.run(port=8880)
