# Lập luận lựa chọn Giấy phép Mã nguồn mở cho Nền tảng Thương mại Điện tử (Dual-Licensing Core)

## 1. Giấy phép đề xuất
Đối với dự án nền tảng thương mại điện tử hướng tới mô hình kinh doanh bán bản doanh nghiệp (Enterprise Edition), giấy phép phù hợp nhất cho phiên bản nguồn mở là **GNU Affero General Public License v3.0 (AGPL-3.0)** kết hợp với mô hình **Cấp phép kép (Dual-licensing / Open-core)**.

## 2. Lý do chọn giấy phép AGPL-3.0
AGPL-3.0 là một giấy phép Copyleft mạnh (Strong Copyleft) được thiết kế riêng cho các phần mềm chạy trên môi trường máy chủ và dịch vụ đám mây (SaaS).

- **Khắc phục lỗ hổng SaaS (SaaS Loophole):** Khác với GPLv3 chỉ yêu cầu phân phối mã nguồn khi phần mềm được "phân phối" (distributed) dưới dạng file thực thi (.exe, .apk), AGPL-3.0 quy định rằng nếu phần mềm chạy trên máy chủ và người dùng tương tác qua mạng (như web/API thương mại điện tử), bên sử dụng vẫn **bắt buộc phải công khai toàn bộ mã nguồn chỉnh sửa** cho cộng đồng.
- **Tạo động lực mua bản Enterprise:** Các doanh nghiệp lớn muốn tích hợp nền tảng này vào hệ thống nội bộ, chỉnh sửa mã nguồn độc quyền, hoặc làm dịch vụ SaaS thương mại mà không muốn tiết lộ bí mật kinh doanh/mã nguồn sẽ **không thể sử dụng bản AGPL-3.0**. Điều này buộc họ phải trả phí để mua **Giấy phép Thương mại (Commercial License)** từ công ty phát triển.

## 3. Lập luận kinh tế và kỹ thuật
Mô hình này đã được chứng minh thành công qua các dự án thương mại mã nguồn mở hàng đầu như **WooCommerce (GPL/AGPL)**, **Magento (Open Software License)**, hay **MongoDB/Elasticsearch** (trước đây). 

- **Cộng đồng phát triển (Community Edition):** Giúp dự án lan tỏa nhanh, nhận được sự đóng góp sửa lỗi, plugin và giao diện từ cộng đồng lập trình viên dưới bản AGPL-3.0.
- **Tối ưu doanh thu (Enterprise Edition):** Tạo dòng tiền bền vững từ bản trả phí thương mại (cung cấp các tính năng nâng cao như High Availability, Advanced Analytics, Dedicated Support, và quyền đóng nguồn code tùy biến).