from decimal import Decimal, InvalidOperation
from math import isfinite
import os
from typing import TypedDict

from flask import Blueprint, Flask, flash, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func, String, ForeignKey
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)
book_management_bp = Blueprint("book_management", __name__, template_folder="templates")

class BookFormValues(TypedDict):
    title: str
    author: str
    price: Decimal
    category_id: str

class Category(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    description: Mapped[str] = mapped_column(String(255), default="", nullable=False)

    books: Mapped[list["Book"]] = relationship(
        back_populates="category", cascade="all, delete-orphan"
    )

class Book(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(150), nullable=False)
    author: Mapped[str] = mapped_column(String(100), nullable=False)
    price: Mapped[float] = mapped_column(default=0.0, nullable=False)
    category_id: Mapped[int] = mapped_column(ForeignKey("category.id"), nullable=False)

    category: Mapped["Category"] = relationship(back_populates="books")

def init_book_management(app: Flask, url_prefix: str = "/quan-ly-sach") -> None:
    app.config.setdefault("SECRET_KEY", os.environ.get("SECRET_KEY", "dev-quan-ly-sach"))
    app.config.setdefault("SQLALCHEMY_DATABASE_URI", "sqlite:///sach.db")
    db.init_app(app)
    app.register_blueprint(book_management_bp, url_prefix=url_prefix)
    with app.app_context(): db.create_all()

@book_management_bp.post("/seed")
def seed_data():
    if db.session.scalar(db.select(func.count(Category.id))):
        flash("Cơ sở dữ liệu đã có danh mục, không thêm dữ liệu mẫu.", "info")
        return redirect(url_for(".dashboard"))

    categories = [
        Category(name="Công nghệ thông tin", description="Sách lập trình, hệ thống, dữ liệu"),
        Category(name="Kinh tế", description="Sách quản trị, tài chính, khởi nghiệp"),
        Category(name="Văn học", description="Tiểu thuyết, truyện ngắn trong và ngoài nước"),
    ]
    db.session.add_all(categories)
    db.session.flush()
    db.session.add_all([
        Book(title="Lập trình Python cơ bản", author="Nguyễn Văn A", price=120000, category=categories[0]),
        Book(title="Cơ sở dữ liệu SQLite", author="Trần Thị B", price=95000, category=categories[0]),
        Book(title="Tư duy kinh tế học", author="Lê Hoàng C", price=150000, category=categories[1]),
        Book(title="Nhà giả kim", author="Paulo Coelho", price=79000, category=categories[2]),
    ])
    db.session.commit()
    flash("Đã thêm dữ liệu mẫu thành công.", "success")
    return redirect(url_for(".dashboard"))

@book_management_bp.get("/")
def dashboard():
    total_categories = db.session.scalar(db.select(func.count(Category.id))) or 0
    total_books = db.session.scalar(db.select(func.count(Book.id))) or 0
    total_value = db.session.scalar(db.select(func.sum(Book.price))) or 0.0

    categories = db.session.scalars(db.select(Category).order_by(Category.name)).all()
    recent_books = db.session.scalars(
        db.select(Book).order_by(Book.id.desc()).limit(5)
    ).all()

    return render_template("dashboard.html", total_categories=total_categories,
                           total_books=total_books, total_value=total_value,
                           categories=categories, recent_books=recent_books)


@book_management_bp.get("/categories")
def list_categories():
    categories = db.session.scalars(db.select(Category).order_by(Category.name)).all()
    return render_template("categories.html", categories=categories)


@book_management_bp.route("/categories/create", methods=["GET", "POST"])
def create_category():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        description = request.form.get("description", "").strip()
        error = _validate_category(name, description)
        if error:
            flash(error, "danger")
        else:
            db.session.add(Category(name=name, description=description))
            if _commit_or_duplicate("Tên danh mục đã tồn tại."):
                flash("Đã thêm danh mục thành công.", "success")
                return redirect(url_for(".list_categories"))
    return render_template("category_form.html", action="Thêm", category=None)

@book_management_bp.route("/categories/edit/<int:id>", methods=["GET", "POST"])
def edit_category(id: int):
    category = db.get_or_404(Category, id)
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        description = request.form.get("description", "").strip()
        error = _validate_category(name, description, category.id)
        if error:
            flash(error, "danger")
        else:
            category.name = name
            category.description = description
            if _commit_or_duplicate("Tên danh mục đã tồn tại."):
                flash("Đã cập nhật danh mục thành công.", "success")
                return redirect(url_for(".list_categories"))
    return render_template("category_form.html", action="Sửa", category=category)

@book_management_bp.post("/categories/delete/<int:id>")
def delete_category(id: int):
    category = db.get_or_404(Category, id)
    db.session.delete(category)
    db.session.commit()
    flash("Đã xóa danh mục và các sách thuộc danh mục.", "success")
    return redirect(url_for(".list_categories"))

@book_management_bp.get("/books")
def list_books():
    category_id = request.args.get("category_id", type=int)
    categories = db.session.scalars(db.select(Category).order_by(Category.name)).all()
    stmt = db.select(Book).order_by(Book.title)
    selected_category = None
    if category_id is not None:
        selected_category = db.get_or_404(Category, category_id)
        stmt = stmt.where(Book.category_id == category_id)

    books = db.session.scalars(stmt).all()
    return render_template("books.html", books=books, categories=categories,
                           selected_category=selected_category)

@book_management_bp.route("/books/create", methods=["GET", "POST"])
def create_book():
    categories = db.session.scalars(db.select(Category).order_by(Category.name)).all()
    default_cat_id = request.args.get("category_id", type=int)

    if request.method == "POST":
        values = _book_form_values()
        error = _validate_book(values, categories)
        if error:
            flash(error, "danger")
        else:
            db.session.add(Book(title=values["title"], author=values["author"],
                                price=float(values["price"]),
                                category_id=int(values["category_id"])))
            if _commit_or_duplicate("Không thể lưu sách."):
                flash("Đã thêm sách thành công.", "success")
                return redirect(url_for(".list_books", category_id=values["category_id"]))

    return render_template("book_form.html", action="Thêm", book=None,
                           categories=categories, default_cat_id=default_cat_id)

@book_management_bp.route("/books/edit/<int:id>", methods=["GET", "POST"])
def edit_book(id: int):
    book = db.get_or_404(Book, id)
    categories = db.session.scalars(db.select(Category).order_by(Category.name)).all()

    if request.method == "POST":
        values = _book_form_values()
        error = _validate_book(values, categories)
        if error:
            flash(error, "danger")
        else:
            book.title = values["title"]
            book.author = values["author"]
            book.price = float(values["price"])
            book.category_id = int(values["category_id"])
            if _commit_or_duplicate("Không thể cập nhật sách."):
                flash("Đã cập nhật sách thành công.", "success")
                return redirect(url_for(".list_books", category_id=book.category_id))

    return render_template("book_form.html", action="Sửa", book=book,
                           categories=categories, default_cat_id=book.category_id)

@book_management_bp.post("/books/delete/<int:id>")
def delete_book(id: int):
    book = db.get_or_404(Book, id)
    category_id = book.category_id
    db.session.delete(book)
    db.session.commit()
    flash("Đã xóa sách thành công.", "success")
    return redirect(url_for(".list_books", category_id=category_id))

def _validate_category(name: str, description: str, category_id: int | None = None) -> str | None:
    if not name:
        return "Vui lòng nhập tên danh mục."
    if len(name) > 100:
        return "Tên danh mục không được vượt quá 100 ký tự."
    if len(description) > 255:
        return "Mô tả không được vượt quá 255 ký tự."
    duplicate = db.session.scalar(db.select(Category.id).where(
        func.lower(Category.name) == name.lower(), Category.id != (category_id or 0)))
    if duplicate:
        return "Tên danh mục đã tồn tại."
    return None

def _book_form_values() -> BookFormValues:
    try:
        price = Decimal(request.form.get("price", "").strip() or "0")
    except InvalidOperation:
        price = Decimal("-1")
    return {"title": request.form.get("title", "").strip(),
            "author": request.form.get("author", "").strip(), "price": price,
            "category_id": request.form.get("category_id", "").strip()}

def _validate_book(values: BookFormValues, categories: list[Category]) -> str | None:
    title = values["title"]
    author = values["author"]
    price = values["price"]
    category_id = values["category_id"]
    if not title or not author:
        return "Vui lòng nhập tên sách và tên tác giả."
    if len(title) > 150 or len(author) > 100:
        return "Tên sách tối đa 150 ký tự, tên tác giả tối đa 100 ký tự."
    if not price.is_finite() or price < 0 or not isfinite(float(price)):
        return "Giá sách phải là số hợp lệ và không âm."
    if not category_id.isdigit() or int(category_id) not in {c.id for c in categories}:
        return "Vui lòng chọn một danh mục hợp lệ."
    return None

def _commit_or_duplicate(message: str) -> bool:
    try:
        db.session.commit()
        return True
    except IntegrityError:
        db.session.rollback()
        flash(message, "danger")
        return False


if __name__ == "__main__":
    app = Flask(__name__)
    init_book_management(app, url_prefix="")
    app.run(debug=True)