| Name              | Version | License         |
|-------------------|---------|-----------------|
| Mako              | 1.4.1   | MIT             |
| MarkupSafe        | 3.0.3   | BSD-3-Clause    |
| SQLAlchemy        | 2.0.54  | MIT             |
| alembic           | 1.20.0  | MIT             |
| annotated-doc     | 0.0.5   | MIT             |
| annotated-types   | 0.8.0   | MIT             |
| anyio             | 4.15.1  | MIT             |
| app               | 0.1.0   | UNKNOWN         |
| backend           | 0.1.0   | UNKNOWN         |
| click             | 8.5.0   | BSD-3-Clause    |
| fastapi           | 0.141.1 | MIT             |
| greenlet          | 3.5.6   | MIT AND PSF-2.0 |
| h11               | 0.16.0  | MIT License     |
| idna              | 3.19    | BSD-3-Clause    |
| psycopg           | 3.3.5   | LGPL-3.0-only   |
| psycopg-binary    | 3.3.5   | LGPL-3.0-only   |
| pydantic          | 2.13.5  | MIT             |
| pydantic-settings | 2.15.0  | MIT             |
| pydantic_core     | 2.46.5  | MIT             |
| python-dotenv     | 1.2.3   | BSD-3-Clause    |
| starlette         | 1.6.0   | BSD-3-Clause    |
| typing-inspection | 0.4.4   | MIT             |
| typing_extensions | 4.16.0  | PSF-2.0         |
| tzdata            | 2026.4  | Apache-2.0      |
| uvicorn           | 0.53.0  | BSD-3-Clause    |


### 1. Phân loại và Xác định các nhóm Giấy phép

Dựa trên kết quả truy xuất từ công cụ `pip-licenses`, danh sách các thư viện trong môi trường ảo của dự án được phân loại theo từng nhóm giấy phép như sau:

* **Nhóm Permissive (Tự do / Phổ biến):** 
  * *Danh sách thư viện:* `Mako` (MIT), `MarkupSafe` (BSD-3-Clause), `SQLAlchemy` (MIT), `alembic` (MIT), `annotated-doc` (MIT), `annotated-types` (MIT), `anyio` (MIT), `click` (BSD-3-Clause), `fastapi` (MIT), `greenlet` (MIT/PSF-2.0), `h11` (MIT), `idna` (BSD-3-Clause), `pydantic` (MIT), `pydantic-settings` (MIT), `pydantic_core` (MIT), `python-dotenv` (BSD-3-Clause), `starlette` (BSD-3-Clause), `typing-inspection` (MIT), `typing_extensions` (PSF-2.0), `tzdata` (Apache-2.0), `uvicorn` (BSD-3-Clause).
  * *Đặc điểm:* Đây là các giấy phép cởi mở nhất, cho phép tự do sử dụng, sửa đổi và phân phối trong cả ứng dụng thương mại lẫn đóng nguồn.

* **Nhóm Weak Copyleft (Copyleft yếu):**
  * *Danh sách thư viện:* `psycopg` (LGPL-3.0-only), `psycopg-binary` (LGPL-3.0-only).
  * *Đặc điểm:* Ràng buộc tính chất Copyleft ở cấp độ thư viện độc lập, cho phép liên kết (linking/import) vào các ứng dụng đóng nguồn mà không lây lan nghĩa vụ mở mã nguồn sang toàn bộ dự án.

* **Nhóm Strong Copyleft (Copyleft mạnh - GPLv2, GPLv3, AGPLv3):**
  * **Không xuất hiện gói nào** thuộc nhóm này trong danh sách phân tích.

---

### 2. Phân tích Nghĩa vụ Pháp lý đối với Dự án Thương mại Đóng nguồn

Nếu dự án này được phát triển và thương mại hóa dưới dạng một **Phần mềm thương mại đóng nguồn (Proprietary Closed-Source Software)**, các nghĩa vụ pháp lý phát sinh được xác định như sau:

#### A. Đối với các thư viện nhóm Permissive (MIT, BSD, Apache, PSF)
* **Nghĩa vụ bắt buộc:** Dự án bắt buộc phải trích dẫn và lưu giữ các thông báo bản quyền gốc (**Copyright Notices**) cùng nội dung văn bản giấy phép đi kèm của tác giả các thư viện này trong tài liệu hoặc giao diện của sản phẩm (thường lưu ở file `LICENSES` hoặc mục *Legal/About*).
* **Quyền hạn mã nguồn:** Dự án **hoàn toàn có quyền giữ kín (đóng nguồn)** toàn bộ mã nguồn nghiệp vụ tự phát triển mà không gặp bất kỳ rào cản pháp lý nào.

#### B. Đối với hai thư viện nhóm Weak Copyleft (`psycopg`, `psycopg-binary` - LGPL-3.0)
* **Khả năng đóng nguồn dự án:** Do `psycopg` được tích hợp dưới dạng một thư viện phụ thuộc bên ngoài thông qua cơ chế `import` động của Python (Dynamic Linking), tính chất lây lan (viral effect) của LGPL **không áp dụng** lên mã nguồn chính của ứng dụng. Do đó, mã nguồn dự án thương mại vẫn được giữ kín.
* **Nghĩa vụ phát sinh cụ thể:**
  1. **Không can thiệp core library:** Dự án phải giữ nguyên bản và sử dụng `psycopg` như một module độc lập. Nếu nhóm phát triển thực hiện chỉnh sửa trực tiếp vào mã nguồn của bản thân gói `psycopg`, đoạn code sửa đổi đó bắt buộc phải được công khai dưới giấy phép LGPL-3.0.
  2. **Đảm bảo khả năng thay thế (Relinking):** Người dùng cuối phải có quyền tự do nâng cấp hoặc thay thế phiên bản `psycopg` trong môi trường chạy của ứng dụng mà không làm gián đoạn phần mềm. Cấu trúc môi trường ảo (`venv`) của Python mặc nhiên đáp ứng tốt điều kiện này.
  3. **Thông cáo bản quyền:** Cần ghi rõ việc dự án có sử dụng thư viện `psycopg` được phát hành theo giấy phép GNU Lesser General Public License v3.0.