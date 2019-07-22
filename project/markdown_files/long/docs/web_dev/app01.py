from flask import Flask


app = Flask(__name__)

@app.route('/<name>')
def index(name):
    return '<h1>hello, world : {}</h1>'.format(name)

if __name__ == '__main__':
    app.run(debug=True)
