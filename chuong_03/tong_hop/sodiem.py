from _markupbase import escape

from flask import Flask, abort, jsonify, make_response, redirect, request, url_for

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False

STUDENTS = {
    "23T1020001": {
        "name": "Nguyễn Văn An",
        "lop": "K47A",
        "scores": {"PMMNM": 8.5, "CSDL": 7.0, "MMT": 9.0},
    },
    "23T1020002": {
        "name": "Trần Thị Bình",
        "lop": "K47A",
        "scores": {"PMMNM": 6.0, "CSDL": 5.5, "MMT": 9.0},
    },
    "23T1020003": {
        "name": "Lê Hoàng Cường",
        "lop": "K47B",
        "scores": {"PMMNM": 9.5, "CSDL": 9.0},
    },
    "23T1020004": {
        "name": "Phạm Minh Dũng",
        "lop": "K47B",
        "scores": {"PMMNM": 4.0, "CSDL": 3.5, "MMT": 5.0},
    },
    "23T1020005": {"name": "Hoàng Thu Hà", "lop": "K47A", "scores": {}},
    "23T1020006": {
        "name": "Võ Quốc Khánh",
        "lop": "K47C",
        "scores": {"PMMNM": 7.5, "MMT": 8.0},
    },
}


# Các hàm phụ
def average(scores):
    if not scores:
        return None
    return round(sum(scores.values()) / len(scores), 2)


def rank(avg):
    if avg is None:
        return "Chưa có điểm"
    if avg >= 8.5:
        return "Giỏi"
    if avg >= 7.0:
        return "Khá"
    if avg >= 5.0:
        return "Trung bình"
    return "Yếu"


def student_summary(mssv):
    student = STUDENTS.get(mssv)
    if not student:
        return None
    avg = average(student["scores"])
    return {
        "mssv": mssv,
        "name": student["name"],
        "lop": student["lop"],
        "scores": student["scores"],
        "average": avg,
        "rank": rank(avg),
    }


def layout(title, body):
    safe_title = escape(title)
    nav_home = url_for("home")
    nav_students = url_for("student_list")
    nav_search = url_for("search_student")

    return f"""<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <title>{safe_title} - Sổ điểm</title>
</head>
<body>
    <nav>
        <a href="{nav_home}">Trang chủ</a> | 
        <a href="{nav_students}">Sinh viên</a> | 
        <a href="{nav_search}">Tìm kiếm</a>
    </nav>
    <hr>
    <h1>{safe_title}</h1>
    <div>{body}</div>
</body>
</html>"""


# ---------- PHẦN 1: GIAO DIỆN WEB ----------


# Câu 1: Trang chủ
@app.route("/")
def home():
    total_students = len(STUDENTS)
    classes = set(s["lop"] for s in STUDENTS.values())
    total_classes = len(classes)

    link_web = url_for("student_list")
    link_api = url_for("api_get_students")

    body = f"""
    <p>Tổng số sinh viên: <strong>{total_students}</strong></p>
    <p>Số lớp: <strong>{total_classes}</strong></p>
    <ul>
        <li><a href="{link_web}">Xem danh sách sinh viên (Giao diện Web)</a></li>
        <li><a href="{link_api}">Xem danh sách sinh viên (API JSON)</a></li>
    </ul>
    """
    return layout("Trang chủ", body)


# -------- Câu 2: Danh sách sinh viên (Có lọc theo lớp)
@app.route("/students")
def student_list():
    lop_filter = request.args.get("lop", "").strip()
    all_classes = sorted(list(set(s["lop"] for s in STUDENTS.values())))

    nav_links = [f'<a href="{url_for("student_list")}">Tất cả</a>']
    for c in all_classes:
        nav_links.append(f'<a href="{url_for("student_list", lop=c)}">{escape(c)}</a>')
    filter_bar = " | ".join(nav_links)

    filtered_students = []
    for mssv in STUDENTS:
        summary = student_summary(mssv)
        if summary is not None:
            if lop_filter:
                if summary["lop"].lower() == lop_filter.lower():
                    filtered_students.append(summary)
            else:
                filtered_students.append(summary)

    if not filtered_students:
        table_content = "<p>Không có sinh viên phù hợp.</p>"
    else:
        rows = []
        for s in filtered_students:
            detail_url = url_for("student_detail", mssv=s["mssv"])
            avg_str = f"{s['average']:.2f}" if s["average"] is not None else "-"
            rows.append(f"""
            <tr>
                <td><a href="{detail_url}">{escape(s["mssv"])}</a></td>
                <td>{escape(s["name"])}</td>
                <td>{escape(s["lop"])}</td>
                <td>{avg_str}</td>
                <td>{escape(s["rank"])}</td>
            </tr>
            """)

        table_content = f"""
        <table border="1" cellpadding="5" cellspacing="0">
            <thead>
                <tr>
                    <th>MSSV</th>
                    <th>Họ tên</th>
                    <th>Lớp</th>
                    <th>Điểm TB</th>
                    <th>Xếp loại</th>
                </tr>
            </thead>
            <tbody>
                {"".join(rows)}
            </tbody>
        </table>
        """

    body = f"""
    <div>Lọc theo lớp: {filter_bar}</div>
    <br>
    {table_content}
    """
    return layout("Danh sách sinh viên", body)


# --------Câu 3: Chi tiết sinh viên
@app.route("/students/<mssv>")
def student_detail(mssv):
    summary = student_summary(mssv)
    if summary is None:
        abort(404, description=f"Không có sinh viên với MSSV = {mssv}.")

    class_url = url_for("student_list", lop=summary["lop"])

    if summary["scores"]:
        score_rows = "".join(
            [
                f"<tr><td>{escape(course)}</td><td>{score}</td></tr>"
                for course, score in summary["scores"].items()
            ]
        )
        scores_table = f"""
        <table border="1" cellpadding="5" cellspacing="0">
            <tr><th>Học phần</th><th>Điểm</th></tr>
            {score_rows}
        </table>
        """
    else:
        scores_table = "<p>Chưa có điểm học phần nào.</p>"

    avg_str = f"{summary['average']:.2f}" if summary["average"] is not None else "-"
    export_url = url_for("export_csv", mssv=mssv)
    short_url = url_for("short_student_detail", mssv=mssv)

    body = f"""
    <p><strong>MSSV:</strong> {escape(summary['mssv'])}</p>
    <p><strong>Họ tên:</strong> {escape(summary['name'])}</p>
    <p><strong>Lớp:</strong> <a href="{class_url}">{escape(summary['lop'])}</a></p>
    <p><strong>Điểm trung bình:</strong> {avg_str}</p>
    <p><strong>Xếp loại:</strong> {escape(summary['rank'])}</p>
    <p><strong>Link rút gọn:</strong> <a href="{short_url}">{short_url}</a></p>
    <p><a href="{export_url}">Tải bảng điểm (CSV)</a></p>
    <h3>Bảng điểm từng học phần</h3>
    {scores_table}
    """
    return layout(f"Chi tiết: {summary['name']}", body)


# --------Câu 4: Link rút gọn 301
@app.route("/sv/<mssv>")
def short_student_detail(mssv):
    return redirect(url_for("student_detail", mssv=mssv), code=301)


# --------Câu 5: Xuất CSV
@app.route("/students/<mssv>/export")
def export_csv(mssv):
    summary = student_summary(mssv)
    if summary is None:
        abort(404, description=f"Không có sinh viên với MSSV = {mssv}.")

    csv_lines = ["hoc_phan,diem"]
    for course, score in summary["scores"].items():
        csv_lines.append(f"{course},{score}")
    csv_content = "\n".join(csv_lines)

    response = make_response(csv_content)
    response.headers["Content-Type"] = "text/csv; charset=utf-8"
    response.headers["Content-Disposition"] = f"attachment; filename=diem_{mssv}.csv"
    return response


# --------Câu 6: Tìm kiếm an toàn (chống XSS)
@app.route("/search")
def search_student():
    query = request.args.get("q", "").strip()
    results = []

    if query:
        q_lower = query.lower()
        for mssv, data in STUDENTS.items():
            if q_lower in mssv.lower() or q_lower in data["name"].lower():
                s = student_summary(mssv)
                if s is not None:
                    results.append(s)

    if not query:
        search_result_html = ""
    elif not results:
        search_result_html = f'<p>Tìm thấy 0 kết quả cho "{escape(query)}".</p>'
    else:
        items = []
        for s in results:
            detail_url = url_for("student_detail", mssv=s["mssv"])
            items.append(
                f'<li><a href="{detail_url}">{escape(s["name"])} ({escape(s["mssv"])})</a> - Lớp: {escape(s["lop"])}</li>'
            )
        search_result_html = f"""
        <p>Tìm thấy {len(results)} kết quả cho "{escape(query)}":</p>
        <ul>
            {"".join(items)}
        </ul>
        """

    body = f"""
    <form action="{url_for('search_student')}" method="get">
        <input type="text" name="q" value="{escape(query)}" placeholder="Nhập tên hoặc MSSV...">
        <button type="submit">Tìm kiếm</button>
    </form>
    <br>
    {search_result_html}
    """
    return layout("Tìm kiếm sinh viên", body)


#------ PHẦN 2: API JSON------


#---------Câu 7.1. Lấy danh sách sinh viên có tham số
@app.route("/api/students", methods=["GET"])
def api_get_students():
    lop_param = request.args.get("lop", "").strip()
    min_avg_raw = request.args.get("min_avg")

    min_avg = None
    if min_avg_raw is not None:
        try:
            min_avg = float(min_avg_raw)
        except ValueError:
            abort(400, description="Tham số min_avg phải là một số hợp lệ.")

    results = []
    for mssv in STUDENTS:
        summary = student_summary(mssv)
        if summary is None:
            continue

        # Lọc theo lớp (không phân biệt hoa thường)
        if lop_param and summary["lop"].lower() != lop_param.lower():
            continue

        # Lọc theo điểm trung bình (bỏ qua sinh viên chưa có điểm)
        if (
            summary is not None
            and (not lop_param or summary["lop"].lower() == lop_param.lower())
            and (
                min_avg is None
                or (summary["average"] is not None and summary["average"] >= min_avg)
            )
        ):
            results.append(summary)

    return jsonify(results)


#---------Câu 7.2: Lấy chi tiết thông tin một sinh viên theo MSSV
@app.route("/api/students/<mssv>", methods=["GET"])
def api_get_student_detail(mssv):
    summary = student_summary(mssv)
    if summary is None:
        abort(404, description=f"Không tìm thấy sinh viên có MSSV = {mssv}.")

    return jsonify(summary)


#---------Câu 8: Quản lý điểm một học phần
@app.route("/api/students/<mssv>/scores/<course>", methods=["GET", "PUT", "DELETE"])
def api_manage_score(mssv: str, course: str):
    student = STUDENTS.get(mssv)
    if not student:
        abort(404, description=f"Không tìm thấy sinh viên có MSSV = {mssv}.")

    # Tên học phần luôn chuyển thành chữ hoa
    course_upper = course.upper()

    # Xem điểm
    if request.method == "GET":
        if course_upper not in student["scores"]:
            abort(404, description=f"Sinh viên chưa có điểm học phần {course_upper}.")
        return jsonify(
            {
                "mssv": mssv,
                "course": course_upper,
                "score": student["scores"][course_upper],
            }
        )

    # Thêm hoặc Sửa điểm
    elif request.method == "PUT":
        score_raw = request.args.get("score")

        # Lỗi 400 nếu thiếu tham số score
        if score_raw is None:
            abort(400, description="Thiếu tham số 'score'.")

        # Lỗi 400 nếu score sai kiểu
        try:
            score_val = float(score_raw)
        except ValueError:
            abort(400, description="Tham số 'score' phải là một số.")

        # Lỗi 400 nếu score ngoài [0, 10]
        if not (0 <= score_val <= 10):
            abort(400, description="Điểm phải nằm trong khoảng từ 0 đến 10.")

        # Kiểm tra xem đây là thao tác THÊM MỚI (201) hay CẬP NHẬT (200)
        is_new = course_upper not in student["scores"]
        student["scores"][course_upper] = score_val
        avg = average(student["scores"])

        res_data = {
            "mssv": mssv,
            "course": course_upper,
            "score": score_val,
            "average": avg,
        }

        if is_new:
            # Thêm mới: trả 201 + header Location
            response = jsonify(res_data)
            response.status_code = 201
            response.headers["Location"] = url_for(
                "api_manage_score", mssv=mssv, course=course_upper
            )
            return response
        else:
            # Sửa điểm: trả 200
            return jsonify(res_data), 200

    # Xóa điểm
    elif request.method == "DELETE":
        if course_upper not in student["scores"]:
            abort(404, description=f"Sinh viên chưa có điểm học phần {course_upper}.")

        del student["scores"][course_upper]
        return make_response("", 204)

    # Branch phòng ngừa lỗi Pylance và xử lý các method khác
    else:
        abort(405, description="Phương thức không được hỗ trợ.")


# ----------Câu 9: Trang lỗi thống nhất cho 400, 404, 405
ERR_TITLES = {
    400: "Dữ liệu không hợp lệ",
    404: "Không tìm thấy",
    405: "Phương thức không được hỗ trợ",
}


@app.errorhandler(400)
@app.errorhandler(404)
@app.errorhandler(405)
def handle_error(error):
    # Lấy mã HTTP status code (mặc định 500 nếu không xác định)
    code = getattr(error, "code", 500)

    # Lấy tiêu đề lỗi tương ứng từ bảng ERR_TITLES
    title = ERR_TITLES.get(code, "Lỗi ứng dụng")

    # Lấy mô tả chi tiết từ error.description
    description = getattr(error, "description", "Đã xảy ra lỗi.")

    # Phản hồi định dạng JSON cho các route API bắt đầu bằng /api/
    if request.path.startswith("/api/"):
        return jsonify({"error": title, "detail": description}), code

    # Phản hồi giao diện HTML cho các trang Web còn lại
    body = f"<h2>{code} - {escape(title)}</h2><p>{escape(description)}</p>"
    return layout(f"Lỗi {code}", body), code


if __name__ == "__main__":
    app.run(debug=True, port=8000)