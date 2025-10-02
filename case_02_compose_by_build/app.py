from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/echo", methods=["GET"])
def echo():
    message = request.args.get("msg", "Hello")
    return jsonify({"echo": message}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
