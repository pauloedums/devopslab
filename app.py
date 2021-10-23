from flask import Flask

app = Flask(__name__)

@app.route("/")
def pagina_inicial():
    return "Hello World"

@app.route("/soma")
def soma_valores():
    x=10+10
    return "Sua soma de 10+10="+str(x)

if __name__ == '__main__':
    app.run()
