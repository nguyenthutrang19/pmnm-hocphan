from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func, String  #[cite: 4, 5]
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column  #[cite: 5]

# Định nghĩa header trả về dạng văn bản thuần để hiển thị đẹp trên trình duyệt
TEXT = {"Content-Type": "text/plain; charset=utf-8"}  #

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)

app = Flask(__name__)
app.config["SECRET_KEY"] = "dev-chi-dung-khi-phat-trien"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///qlsv.db"
db.init_app(app)

# Model Student[cite: 5]
class Student(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)  #[cite: 5]
    mssv: Mapped[str] = mapped_column(String(10), unique=True)  #[cite: 5]
    name: Mapped[str] = mapped_column(String(100))  #[cite: 5]
    gpa: Mapped[float] = mapped_column(default=0.0)  #[cite: 5]

    def __repr__(self):  #[cite: 5]
        return f"<Student {self.mssv} {self.name}>"  #[cite: 5]

with app.app_context():
    db.create_all()

# ROUTE BƯỚC 5: THÊM DỮ LIỆU MẪU 
@app.get("/them-mau")  #[cite: 4]
def add_sample():
    total = db.session.scalar(db.select(func.count(Student.id)))  #[cite: 4]
    if total > 0:
        return f"Đã có {total} sinh viên, không thêm nữa."  #[cite: 4]

    an = Student(mssv="23T1020001", name="Nguyễn Văn An", gpa=8.5)  #[cite: 4]
    db.session.add(an)  #[cite: 4]
    db.session.add_all([
        Student(mssv="23T1020002", name="Trần Thị Bình", gpa=6.8),  #[cite: 4]
        Student(mssv="23T1020003", name="Lê Hoàng Cường", gpa=9.1),  #[cite: 4]
        Student(mssv="23T1020004", name="Phạm Minh Dũng", gpa=4.5),  #[cite: 4]
        Student(mssv="23T1020005", name="Hoàng Thu Hà", gpa=7.4),  #[cite: 4]
    ])  #[cite: 4]
    db.session.commit()  #[cite: 4]
    return "Đã thêm 5 sinh viên mẫu thành công!"

# ROUTE HIỂN THỊ DANH SÁCH SINH VIÊN (HTML TEMPLATE)
@app.get("/")
@app.get("/students")
def list_students():
    students = db.session.scalars(db.select(Student)).all()
    return render_template("students.html", students=students)

# ROUTE BƯỚC 6: ĐỌC DỮ LIỆU BẰNG VIEW FUNCTION
@app.get("/thu-truy-van")  #
def try_queries():
    if db.session.scalar(db.select(func.count(Student.id))) == 0:  #
        return "Chưa có dữ liệu, hãy mở /them-mau trước.", TEXT  #

    lines = []  #
    
    # 1. get(3)
    lines.append(f"1. get(3): {db.session.get(Student, 3)}")  #
    
    # 2. get(99)
    lines.append(f"2. get(99): {db.session.get(Student, 99)}")  #
    
    # 3. Tất cả sinh viên
    everyone = db.session.execute(db.select(Student)).scalars().all()  #
    lines.append(f"3. Tất cả: {len(everyone)} sinh viên")  #
    
    # 4. Lọc GPA >= 8 và sắp xếp giảm dần
    stmt = (
        db.select(Student)
        .where(Student.gpa >= 8)
        .order_by(Student.gpa.desc())
    )  #
    good = db.session.execute(stmt).scalars().all()  #
    lines.append(f"4. Điểm >= 8: {good}")  #
    
    # 5. Lọc theo MSSV
    binh = db.session.scalar(
        db.select(Student).filter_by(mssv="23T1020002")
    )  #
    lines.append(f"5. MSSV 23T1020002: {binh}")  #
    
    # 6. Thống kê số lượng và điểm trung bình
    count = db.session.scalar(db.select(func.count(Student.id)))  #
    avg = db.session.scalar(db.select(func.avg(Student.gpa)))  #
    lines.append(f"6. Số SV: {count}, điểm TB: {avg:.2f}")  #

    return "\n".join(lines), TEXT  #

if __name__ == "__main__":
    app.run(debug=True)

# ROUTE MỚI: Trang thống kê sinh viên sử dụng render_template
# ROUTE THỐNG KÊ
@app.get("/thong-ke")
def statistics():
    total = db.session.scalar(db.select(func.count(Student.id))) or 0
    avg = db.session.scalar(db.select(func.avg(Student.gpa))) or 0.0

    # Lấy danh sách theo từng loại
    ds_gioi = db.session.scalars(db.select(Student).where(Student.gpa >= 8.0)).all()
    ds_kha = db.session.scalars(db.select(Student).where(Student.gpa >= 6.5, Student.gpa < 8.0)).all()
    ds_tb = db.session.scalars(db.select(Student).where(Student.gpa >= 5.0, Student.gpa < 6.5)).all()
    ds_yeu = db.session.scalars(db.select(Student).where(Student.gpa < 5.0)).all()

    return render_template(
        "thong_ke.html",
        total=total,
        avg=round(avg, 2),
        ds_gioi=ds_gioi,
        ds_kha=ds_kha,
        ds_tb=ds_tb,
        ds_yeu=ds_yeu
    )