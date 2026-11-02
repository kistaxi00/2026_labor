from flask import Flask, jsonify

app = Flask(__name__)
@app.route('/ap1/uzenet')
def uzenet():
    return jsonify({'Uzenet': 'ok'})

app.run(port=5000)