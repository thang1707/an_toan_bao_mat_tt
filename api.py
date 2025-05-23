import elgamal
from flask import Flask, request,  jsonify
app = Flask(__name__)
@app.route("/encrypted", methods=["POST"])
def encryted():
    data = request.get_json()
    message = data.get("message")
    encryted = elgamal.ma_hoa()