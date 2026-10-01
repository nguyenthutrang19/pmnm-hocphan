from flask import Blueprint, render_template, request

# Tạo Blueprint cho buổi 2
buoi3_bp = Blueprint("buoi3", __name__)


@buoi3_bp.route("/calc", methods=["GET", "POST"])
def home():
    result = None  # Mặc định chưa bấm nút thì kết quả là None
    a = ""
    b = ""

    if request.method == "POST":
        try:
            a = float(request.form.get("a", 0))
            b = float(request.form.get("b", 0))

            tong = a + b
            hieu = a - b
            tich = a * b

            if b == 0:
                thuong = "Không thể chia với số 0"
            else:
                thuong = a / b

            result = {"tong": tong, "hieu": hieu, "tich": tich, "thuong": thuong}
        except ValueError:
            result = "Lỗi: Vui lòng nhập số hợp lệ!"

    # return "Xin chao"
    return render_template("math.html", result=result, a=a, b=b)
