from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# http://localhost:8000/api/hello
@app.route('/') # EndPoint
def send_message():
    """Return a friendly HTTP greeting."""
    message = {'text': 'Hello World!'}
    return jsonify(message)

if __name__ == '__main__':
    app.run(debug=True, port=8000)
