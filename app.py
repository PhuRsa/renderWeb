from flask import Flask, request

app = Flask(__name__)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    char_value = request.args.get('char', default='', type=str)
    return char_value if char_value else '', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
