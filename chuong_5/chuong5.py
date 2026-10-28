from flask import Flask, render_template, request

app = Flask(__name__)

# --- ROUTE TRANG CHỦ ---
@app.route('/')
def index():
    return render_template('index.html')


# --- BÀI 1: MÁY TÍNH CƠ BẢN ---
def parse_b1(val_str):
    if not val_str or not val_str.strip():
        return None, "Vui lòng nhập một số."
    try:
        return float(val_str.strip().replace(',', '.')), None
    except ValueError:
        return None, "Vui lòng nhập một số."

def format_b1(val):
    return str(int(val)) if val == int(val) else str(val)

@app.route('/bai1', methods=['GET', 'POST'])
def bai1():
    a, b, op = "", "", "+"
    error_a = error_b = error_op = result = None

    if request.method == 'POST':
        a = request.form.get('a', '')
        b = request.form.get('b', '')
        op = request.form.get('op', '+')

        num_a, error_a = parse_b1(a)
        num_b, error_b = parse_b1(b)

        if op not in ['+', '-', '*', '/']:
            error_op = "Phép toán không hợp lệ."

        if not error_b and op == '/' and num_b == 0:
            error_b = "Không thể chia cho 0."

        if not error_a and not error_b and not error_op:
            ops = {'+': num_a + num_b, '-': num_a - num_b, '*': num_a * num_b, '/': num_a / num_b}
            res = ops[op]
            result = f"{format_b1(num_a)} {op} {format_b1(num_b)} = {format_b1(res)}"

    return render_template('bai1.html', a=a, b=b, op=op, error_a=error_a, error_b=error_b, error_op=error_op, result=result)


# --- BÀI 2: TÍNH ĐIỂM HỌC PHẦN ---
def validate_score(val_str):
    if not val_str or not val_str.strip():
        return None, "Vui lòng nhập một số."
    try:
        score = float(val_str.strip().replace(',', '.'))
        if score < 0 or score > 10:
            return None, "Điểm phải từ 0 đến 10."
        return score, None
    except ValueError:
        return None, "Vui lòng nhập một số."

@app.route('/bai2', methods=['GET', 'POST'])
def bai2():
    cc, gk, ck = "", "", ""
    err_cc = err_gk = err_ck = result = None

    if request.method == 'POST':
        cc = request.form.get('cc', '')
        gk = request.form.get('gk', '')
        ck = request.form.get('ck', '')

        num_cc, err_cc = validate_score(cc)
        num_gk, err_gk = validate_score(gk)
        num_ck, err_ck = validate_score(ck)

        if err_cc is None and err_gk is None and err_ck is None:
            total = num_cc * 0.1 + num_gk * 0.3 + num_ck * 0.6
            total_round = round(total, 1)

            if num_ck < 1.0:
                grade, note = "F", " (điểm thi dưới 1)"
            else:
                note = ""
                if total_round >= 8.5: grade = "A"
                elif total_round >= 7.0: grade = "B"
                elif total_round >= 5.5: grade = "C"
                elif total_round >= 4.0: grade = "D"
                else: grade = "F"

            result = f"{total_round} · {grade}{note}"

    return render_template('bai2.html', cc=cc, gk=gk, ck=ck, err_cc=err_cc, err_gk=err_gk, err_ck=err_ck, result=result)


# --- BÀI 3: TÍNH CHỈ SỐ BMI ---
def validate_height(val_str):
    if not val_str or not val_str.strip():
        return None, "Vui lòng nhập một số."
    try:
        val = float(val_str.strip().replace(',', '.'))
        if 0 < val < 10:
            return None, "Giá trị phải từ 50 đến 250. (nhập mét thay vì cm)"
        elif val < 50 or val > 250:
            return None, "Giá trị phải từ 50 đến 250."
        return val, None
    except ValueError:
        return None, "Vui lòng nhập một số."

def validate_weight(val_str):
    if not val_str or not val_str.strip():
        return None, "Vui lòng nhập một số."
    try:
        val = float(val_str.strip().replace(',', '.'))
        if val < 10 or val > 300:
            return None, "Lỗi ở cân nặng: Giá trị phải từ 10 đến 300."
        return val, None
    except ValueError:
        return None, "Vui lòng nhập một số."

@app.route('/bai3', methods=['GET', 'POST'])
def bai3():
    height_str = ""
    weight_str = ""
    err_height = None
    err_weight = None
    
    bmi_val = None
    classification = None
    ideal_text = ""

    if request.method == 'POST':
        height_str = request.form.get('height', '')
        weight_str = request.form.get('weight', '')

        h_num, err_height = validate_height(height_str)
        w_num, err_weight = validate_weight(weight_str)

        if err_height is None and err_weight is None:
            # Đổi cm sang m
            h_m = h_num / 100.0
            bmi = w_num / (h_m * h_m)
            bmi_val = round(bmi, 1)

            # Phân loại theo chuẩn Châu Á
            if bmi_val < 18.5:
                classification = "Thiếu cân"
            elif bmi_val < 23.0:
                classification = "Bình thường"
                # Cân nặng nên có tương ứng BMI 18.5 - 22.9
                w_min = round(18.5 * (h_m ** 2), 1)
                w_max = round(22.9 * (h_m ** 2), 1)
                ideal_text = f", nên có {w_min}–{w_max} kg"
            elif bmi_val < 25.0:
                classification = "Thừa cân"
            else:
                classification = "Béo phì"

    return render_template(
        'bai3.html',
        height=height_str,
        weight=weight_str,
        err_height=err_height,
        err_weight=err_weight,
        bmi_val=bmi_val,
        classification=classification,
        ideal_text=ideal_text
    )


if __name__ == '__main__':
    
    app.run(debug=True)
    # --- ROUTE LIÊN HỆ ---
@app.route('/contact')
def contact():
    return render_template('contact.html')