from flask import Flask, request,  jsonify
from flask_cors import CORS
import sys
import random
app = Flask(__name__)
CORS(app)


p = 127 # p tự chọn và p phải là một số nguyên tố lớn
g = 7 # g là phần tử sinh của trường Z*p  (tự chọn)
x = 3 # x là khóa riêng (tự chọn), đây là khóa bí mật
y = pow(g, x, p) # khóa công khai (p,g,y)



def xu_ly_chuoi(m):
    return [ord(ch) for ch in m]


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
#mã hóa 1 kí tự khi đã chuyển từ chữ sang số
def ma_hoa(p,g,y,m):
    while True:
        k = random.randint(2, p - 2)
        if gcd(k, p - 1) == 1:
            break
    c1 = pow(g, k, p)
    c2 = (m * pow(y, k, p)) % p
    return c1, c2

def giai_ma(c1, c2, p, x):
    s = pow(c1,x,p)
    s_inv = pow(s,-1,p) # pow(m,-1,mod)
    m = (c2*s_inv)%p
    return m


# ---- API mã hóa ----
@app.route("/encrypted", methods=["POST"])
def encrypt():
    data = request.get_json()
    message = data.get("message")
    if not message:
        return jsonify({"error": "khong co thong diep"}), 400
    list_char = xu_ly_chuoi(message)
    res = []
    for m in list_char:
        c1, c2 = ma_hoa(p,g,y,m)
        res.append({'c1': c1, 'c2': c2})

    return jsonify({
        'original': message,
        'encrypted': res
    })


# ---- API giải mã ----
@app.route("/decrypted", methods=["POST"])
def decrypt():
    data = request.get_json()
    encrypted_data = data.get("encrypted")
    if not encrypted_data or not isinstance(encrypted_data, list):
        return jsonify({"error": "Du lieu ma hoa khong hop le"}), 400
    decrypted_chars = []
    for item in encrypted_data:
        c1 = item.get('c1')
        c2 = item.get('c2')
        if c1 is None or c2 is None:
            return jsonify({'error': 'thieu c1 hoac c2 trong du lieu'}), 400
        m = giai_ma(c1,c2,p,x)
        decrypted_chars.append(chr(m))
    original_message = ''.join(decrypted_chars)
    return jsonify({
        "decrypted": original_message
    })
    


if __name__ == "__main__":
    app.run(debug=True)
