from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')

@app.route('/esqueci-minha-senha')
def esquecisenha1():
    return render_template('esqueci-minha-senha.html')

@app.route('/esqueci-minha-senha2')
def esquecisenha2():
    return render_template('esqueci-minha-senha2.html')

@app.route('/galeria')
def galeria():
    return render_template('galeria.html')

if __name__ == '__main__':
    app.run(debug=True)     
    