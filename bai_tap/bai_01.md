## Bài 1.2: Phân tích dự án rẽ nhánh do mâu thuẫn trong cộng đồng - Trường hợp MySQL và MariaDB
### 1. Bối cảnh và nguyên nhân mâu thuẫn

MySQL được phát triển từ năm 1995 bởi công ty MySQL AB và nhanh chóng trở thành một trong những hệ quản trị cơ sở dữ liệu mã nguồn mở phổ biến. Năm 2008, Sun Microsystems mua lại MySQL AB. Đến năm 2009, Oracle công bố kế hoạch mua lại Sun Microsystems, qua đó khiến tương lai của MySQL trở nên khó đoán.

Sự kiện này làm dấy lên lo ngại trong cộng đồng mã nguồn mở. Oracle vốn là công ty sở hữu hệ quản trị cơ sở dữ liệu thương mại Oracle Database, nên cộng đồng lo ngại rằng MySQL có thể bị thay đổi định hướng để phục vụ lợi ích thương mại của Oracle. Những lo ngại này đặc biệt liên quan đến khả năng phát triển phiên bản Community, mức độ mở của dự án và quyền tự chủ của cộng đồng phát triển.

### 2. Quá trình rẽ nhánh

Năm 2009, trong bối cảnh Oracle đang tiến hành thương vụ mua lại Sun Microsystems, Michael “Monty” Widenius - một trong những nhà sáng lập chính của MySQL - đã fork mã nguồn MySQL để xây dựng một dự án độc lập có tên MariaDB.

MariaDB ban đầu được định hướng trở thành một drop-in replacement cho MySQL, duy trì mức tương thích cao về cú pháp SQL, giao thức kết nối và nhiều thành phần của hệ thống. Điều này cho phép các ứng dụng đang sử dụng MySQL có thể chuyển sang MariaDB với tương đối ít thay đổi.

Sau khi tách khỏi MySQL, MariaDB tiếp tục phát triển theo hướng độc lập và bổ sung các tính năng riêng. Đây là điểm quan trọng của cơ chế fork: mã nguồn của dự án ban đầu có thể trở thành nền tảng cho một hướng phát triển mới khi cộng đồng hoặc các nhà phát triển chủ chốt không đồng thuận với định hướng của dự án gốc.

### 3. Tác động đến cộng đồng và công nghiệp

Fork MariaDB tạo ra những tác động đáng kể đối với hệ sinh thái cơ sở dữ liệu mã nguồn mở.

* **Sự chuyển dịch trong hệ sinh thái Linux:** Một số bản phân phối Linux lớn như Debian, Fedora, Red Hat Enterprise Linux và CentOS đã từng lựa chọn MariaDB thay cho MySQL làm hệ quản trị cơ sở dữ liệu mặc định.
* **Thúc đẩy đổi mới:** MariaDB phát triển các công nghệ riêng như Aria và MariaDB ColumnStore, đồng thời đưa ra những khác biệt về tính năng và hiệu năng so với MySQL.
* **Tạo áp lực cạnh tranh:** Sự tồn tại của MariaDB tạo thêm một lựa chọn mã nguồn mở cạnh tranh với MySQL, qua đó thúc đẩy sự phát triển của cả hai dự án.
* **Tăng quyền lựa chọn cho người dùng:** Người dùng không còn hoàn toàn phụ thuộc vào một hướng phát triển duy nhất mà có thể lựa chọn giữa các hệ quản trị có nguồn gốc từ cùng một nền tảng.

### 4. Bài học rút ra

Trường hợp MySQL và MariaDB cho thấy fork là một cơ chế quan trọng để giải quyết bất đồng và phân bổ lại quyền kiểm soát trong cộng đồng mã nguồn mở. Việc một công ty sở hữu thương hiệu và quyền phát triển dự án không đồng nghĩa với việc cộng đồng không còn khả năng tạo ra một hướng phát triển thay thế.

Khi các nhà phát triển không đồng thuận với định hướng của dự án gốc, họ có thể sử dụng mã nguồn hiện có để xây dựng một dự án độc lập. Tuy nhiên, fork cũng có thể dẫn đến sự phân mảnh về tính năng, khả năng tương thích và cộng đồng phát triển. Do đó, trường hợp MariaDB không chỉ cho thấy sức mạnh của mã nguồn mở mà còn cho thấy fork vừa là cơ chế giải quyết xung đột, vừa là động lực tạo ra cạnh tranh và đổi mới trong hệ sinh thái phần mềm.
