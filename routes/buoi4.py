from flask import Blueprint, render_template, request

# Tạo Blueprint cho buổi 2
buoi4_bp = Blueprint("buoi4", __name__)


@buoi4_bp.route("/gioi-thieu")
@buoi4_bp.route("/buoi4", methods=["GET", "POST"])
def buoi4():
    # return render_template("buoi4.html")
    return "Xin chào mọi người"


@buoi4_bp.route("/user/<username>")
def user_profile(username):
    return f"Xin chào, {username}"


@buoi4_bp.route("/square/<x>")
def square(x):
    return f"{x}"


@buoi4_bp.route("/sum/<strs>")
def tong(strs):
    numbers = strs.split(",")
    total = sum(float(num) for num in numbers)
    return f"{total}"


@buoi4_bp.route("/tinh-toan")
def tinh_toan():
    a = request.args.get("a", type=float)
    b = request.args.get("b", type=float)
    op = request.args.get("op")

    # Kiểm tra nếu thiếu tham số
    if a is None or b is None or not op:
        return "Vui lòng nhập đầy đủ a, b và op", 400

    # Xử lý các phép tính
    if op == "add" or op == "+":
        ket_qua = a + b
    elif op == "sub" or op == "-":
        ket_qua = a - b
    elif op == "mul" or op == "*":
        ket_qua = a * b
    elif op == "div" or op == "/":
        if b == 0:
            return "Lỗi: Không thể chia cho 0", 400
        ket_qua = a / b
    else:
        return f"Phép toán '{op}' không hợp lệ", 400

    return f"Kết quả: {a} {op} {b} = {ket_qua}"


POSTS = [
    {
        "id": 1,
        "title": "Chào Flask",
        "author": "Thu Trang",
        "content": "Flask là một micro-framework...",
    },
]


def find_post(post_id):
    for post in POSTS:
        if post["id"] == post_id:
            return post
    return None


@buoi4_bp.route("/post/<int:post_id>")
def show_post(post_id):
    # GỌI HÀM Ở ĐÂY: Truyền post_id từ URL vào hàm find_post
    post = find_post(post_id)

    # Nếu không tìm thấy bài viết, trả về lỗi 404 (Not Found)
    if post is None:
        return "Không tìm thấy bài viết!", 404

    # Trả về giao diện HTML (hoặc trả về trực tiếp dict/string để test)
    return render_template("post_detail.html", post=post)
