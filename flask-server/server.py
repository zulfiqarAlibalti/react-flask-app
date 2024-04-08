from flask import Flask, jsonify

app = Flask(__name__)

# members API routes
@app.route('/members')
def members():
    return {"members": ["member1", "member2", "member3"]}

if __name__ == '__main__':
    app.run(debug=True)
