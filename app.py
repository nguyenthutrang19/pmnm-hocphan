from flask import Flask, render_template

from routes.baitapchuong3 import baitapchuong3_bp
from routes.buoi3 import buoi3_bp
from routes.buoi4 import buoi4_bp

app = Flask(__name__)
app.json.ensure_ascii = False  # type: ignore


# Đăng ký blueprint vào ứng dụng
app.register_blueprint(buoi4_bp)
app.register_blueprint(buoi3_bp)
app.register_blueprint(baitapchuong3_bp)


@app.route("/")
def home():
    return ""


@app.errorhandler(404)
def page_not_found(e):
    # Lấy thông báo từ abort(404, description=...) nếu có
    error_msg = getattr(e, "description", None)
    return render_template("404.html", error_message=error_msg), 404


if __name__ == "__main__":
    app.run(debug=True)
