# Phân tích vụ tranh chấp pháp lý: Oracle v. Google (Bản quyền & Giấy phép Java)

## 1. Các bên liên quan
- **Nguyên đơn:** Oracle Corporation (Chủ sở hữu quyền tác giả ngôn ngữ và nền tảng Java sau khi mua lại Sun Microsystems).
- **Bị đơn:** Google LLC (Công ty phát triển hệ điều hành Android).

## 2. Giấy phép liên quan
- **GPLv2 (GNU General Public License, version 2)** kèm theo ngoại lệ **Classpath Exception** đối với mã nguồn Java OpenJDK.
- Quyền sở hữu trí tuệ đối với các **Giao diện lập trình ứng dụng (API)**.

## 3. Lập luận của mỗi bên
- **Lập luận của Oracle:** Google đã sao chép trái phép khoảng 11.500 dòng code khai báo API (Header code) cùng cấu trúc, trình tự và tổ chức (SSO) của 37 gói Java API trong hệ điều hành Android mà không mua giấy phép thương mại từ Sun/Oracle, vi phạm bản quyền phần mềm nghiêm trọng.
- **Lập luận của Google:** Khai báo API chỉ là giao diện tương tác (tương tự như bàn phím hay ổ cắm điện) nhằm mục đích tương thích sinh thái, không phải là đoạn code thực thi nghiệp vụ (implementation). Việc tái sử dụng API này thuộc phạm vi **Sử dụng hợp lý (Fair Use)** trong luật bản quyền Hoa Kỳ, giúp lập trình viên Java dễ dàng chuyển sang lập trình ứng dụng Android.

## 4. Kết quả và Ý nghĩa pháp lý
- **Kết quả:** Tháng 4 năm 2021, Tòa án Tối cao Hoa Kỳ đã tuyên bố **Google thắng kiện**. Tòa phán quyết rằng việc Google tái sử dụng cấu trúc các gói Java API nằm trong phạm vi **Fair Use** về mặt pháp lý.
- **Ý nghĩa pháp lý:** 
  - Tạo tiền lệ pháp lý bảo vệ ngành công nghiệp phần mềm: Việc tái triển khai API để đạt được tính tương thích (Interoperability) giữa các hệ thống không bị coi là vi phạm bản quyền.
  - Khẳng định ranh giới giữa việc "sao chép ý tưởng/giao diện" và "sao chép mã thực thi", ngăn chặn rủi ro thâu tóm/độc quyền nền tảng phát triển của các tập đoàn công nghệ lớn đối với cộng đồng mã nguồn mở.