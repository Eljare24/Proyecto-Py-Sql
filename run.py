from flask import Flask

app = Flask(__name__)
@app.route('/')
def inicio():
    return ('Hola esta es la página de inicio')
if __name__ == '__main__':
    app.run(debug=True)