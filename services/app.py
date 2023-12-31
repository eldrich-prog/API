from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# http://localhost:5000/api/message
@app.route('/api/message') # EndPoint
def send_message():
    """Return a friendly HTTP greeting."""
    message = {'text': 'connected.'}
    return jsonify(message)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
