from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def inicio():
    return "API de suma activa. Usa /sumar?a=5&b=7"

@app.route('/sumar', methods=['GET'])
def sumar():
    try:
        a = float(request.args.get('a'))
        b = float(request.args.get('b'))
        resultado = a + b
        return jsonify({"resultado": resultado})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
