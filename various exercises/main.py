

from flask import Flask
from flask import app

app = Flask(__name__)

@app.route('/', method= 'GET')
def response():
    return "<p>Home, sweet home.</p>"

# @app.route('/greet', method='GET')
# def response():
#     return "<h1>Hello, world!</h1>"

# @app.route('/greet <name>', method='GET')
# def response():
#     return "<h1>Hello, <name> </h1>"

# if __name__ == "__main__":
#     app.run(debug=True)