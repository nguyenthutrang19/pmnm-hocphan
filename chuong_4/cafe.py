from datetime import datetime
from flask import Flask, render_template, request, abort
import math

app = Flask(__name__)

SHOP = {
    "name": "cà phê Sông Hương",
    "address": "12 Lê Lợi, Huế",
    "open": 7,
    "close": 22,
}

PROMOTIONS = [
    "Giảm 10% cho sinh viên",
    "Mua 2 tặng 1 vào thứ Hai",
]

MENU = [
    {"id": 1, "name": "cà phê đen", "price": 20000, "available": True, "image": "ca-phe-den.jpg"},
    {"id": 2, "name": "bạc xỉu", "price": 30000, "available": True, "image": "bac-xiu.jpg"},
    {"id": 3, "name": "cà phê sữa", "price": 25000, "available": True, "image": "ca-phe-sua.jpg"},
    {"id": 4, "name": "trà đào", "price": 35000, "available": True, "image": "tra-dao.jpg"},
    {"id": 5, "name": "trà vải", "price": 35000, "available": True, "image": "tra-vai.jpg"},
    {"id": 6, "name": "bánh mì", "price": 15000, "available": False, "image": "banh-mi.jpg"},
    {"id": 7, "name": "bánh ngọt", "price": 20000, "available": True, "image": "banh-ngot.jpg"}
]

@app.get("/")
def index():
    hour = request.args.get("gio", type=int)
    if hour is None:
        hour = datetime.now().hour

    is_open = SHOP["open"] <= hour < SHOP["close"]

    return render_template(
        "index.html",
        shop=SHOP,
        hour=hour,
        is_open=is_open,
        promotions=PROMOTIONS,
    )

@app.template_filter('vnd')
def format_vnd(value):
    return f"{value:,.0f}".replace(",", ".") + " đ"

@app.route('/menu')
def menu():
    page_param = request.args.get('page', 1)
    
    # 1. Ép kiểu tham số page, nếu gửi 'abc' thì mặc định về 1
    try:
        page = int(page_param)
    except (ValueError, TypeError):
        page = 1

    per_page = 3  
    total_items = len(MENU)
    pages = math.ceil(total_items / per_page)

    if page < 1 or (pages > 0 and page > pages):
        abort(404)

    start = (page - 1) * per_page
    end = start + per_page
    items = MENU[start:end]

    # TRUYỀN ĐỦ CÁC BIẾN items, page, pages SANG TEMPLATE
    return render_template('menu.html', items=items, page=page, pages=pages)

@app.route('/contact')
def contact():
    return render_template('contact.html', shop=SHOP)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == "__main__":
    app.run(debug=True)