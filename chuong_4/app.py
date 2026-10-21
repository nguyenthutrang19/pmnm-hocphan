from flask import Flask, jsonify, render_template

# Khai báo rõ thư mục chứa template là 'flask_template'
app = Flask(__name__, template_folder='flask_template')

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/hello")
def hello_api():
    return jsonify({"status": "success", "message": "Hello World"})

if __name__ == "__main__":
    app.run(debug=True, port=5000)