<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Bài tập 2: Giấy phép mã nguồn mở & Vấn đề pháp lý</title>
    <style>
        :root {
            --primary: #2563eb;
            --primary-hover: #1d4ed8;
            --bg-body: #f8fafc;
            --bg-card: #ffffff;
            --text-main: #0f172a;
            --text-muted: #475569;
            --border: #e2e8f0;
            --code-bg: #0f172a;
            --accent-light: #eff6ff;
        }

        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }

        body {
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
            background-color: var(--bg-body);
            color: var(--text-main);
            line-height: 1.7;
            padding: 2rem 1rem;
        }

        .container {
            max-width: 900px;
            margin: 0 auto;
        }

        .header {
            text-align: center;
            margin-bottom: 2.5rem;
            padding-bottom: 1.5rem;
            border-bottom: 2px solid var(--border);
        }

        .header h5 {
            color: var(--primary);
            text-transform: uppercase;
            letter-spacing: 1px;
            font-size: 0.875rem;
            margin-bottom: 0.5rem;
        }

        .header h1 {
            font-size: 2rem;
            color: var(--text-main);
            font-weight: 800;
        }

        .card {
            background-color: var(--bg-card);
            border-radius: 12px;
            border: 1px solid var(--border);
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -1px rgba(0, 0, 0, 0.03);
            padding: 2rem;
            margin-bottom: 2rem;
        }

        .card-header {
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin-bottom: 1.5rem;
            padding-bottom: 0.75rem;
            border-bottom: 1px solid var(--border);
        }

        .card-title {
            font-size: 1.25rem;
            font-weight: 700;
            color: var(--primary);
        }

        .badge {
            font-size: 0.75rem;
            padding: 0.25rem 0.75rem;
            border-radius: 9999px;
            font-weight: 600;
        }

        .badge-required {
            background-color: #fef2f2;
            color: #dc2626;
            border: 1px solid #fecaca;
        }

        .badge-optional {
            background-color: #f0fdf4;
            color: #16a34a;
            border: 1px solid #bbf7d0;
        }

        h3 {
            font-size: 1.05rem;
            margin: 1.25rem 0 0.5rem 0;
            color: var(--text-main);
        }

        p {
            margin-bottom: 1rem;
            color: var(--text-muted);
            text-align: justify;
        }

        ul, ol {
            margin-bottom: 1rem;
            padding-left: 1.5rem;
            color: var(--text-muted);
        }

        li {
            margin-bottom: 0.4rem;
        }

        a {
            color: var(--primary);
            text-decoration: none;
            font-weight: 500;
            border-bottom: 1px dashed var(--primary);
            transition: all 0.2s ease;
        }

        a:hover {
            color: var(--primary-hover);
            border-bottom-style: solid;
        }

        pre {
            background-color: var(--code-bg);
            color: #f8fafc;
            padding: 1rem;
            border-radius: 8px;
            overflow-x: auto;
            font-family: "Fira Code", Monaco, Consolas, monospace;
            font-size: 0.875rem;
            margin-bottom: 1rem;
        }

        table {
            width: 100%;
            border-collapse: collapse;
            margin: 1rem 0;
            font-size: 0.9rem;
        }

        th, td {
            padding: 0.75rem 1rem;
            text-align: left;
            border-bottom: 1px solid var(--border);
        }

        th {
            background-color: var(--accent-light);
            color: var(--primary);
            font-weight: 600;
        }

        tr:hover {
            background-color: #f1f5f9;
        }

        .alert-box {
            background-color: #fffbeb;
            border-left: 4px solid #f59e0b;
            padding: 1rem;
            border-radius: 4px;
            margin: 1rem 0;
            color: #b45309;
            font-size: 0.925rem;
        }

        @media (max-width: 640px) {
            body { padding: 1rem 0.5rem; }
            .card { padding: 1.25rem; }
            .header h1 { font-size: 1.5rem; }
        }
    </style>
</head>
<body>

<div class="container">

    <div class="header">
        <h5>BÀI 2 · GIẤY PHÉP MÃ NGUỒN MỜ VÀ VẤN ĐỀ PHÁP LÝ[cite: 1]</h5>
        <h1>BÀI TẬP VỀ NHÀ[cite: 1]</h1>
    </div>

    <!-- BÀI 2.1 -->
    <div class="card">
        <div class="card-header">
            <span class="card-title">Bài 2.1 — Lựa chọn Giấy phép Phần mềm[cite: 1]</span>
            <span class="badge badge-required">Bắt buộc</span>
        </div>
        
        <p><strong>Dự án lựa chọn:</strong> Thư viện Python xử lý tiếng Việt muốn được dùng rộng rãi nhất có thể[cite: 1].</p>
        <p><strong>Giấy phép đề xuất:</strong> <a href="https://opensource.org/licenses/MIT" target="_blank" rel="noopener">MIT License</a>[cite: 1] <em>(hoặc <a href="https://www.apache.org/licenses/LICENSE-2.0" target="_blank" rel="noopener">Apache License 2.0</a>)</em>.</p>

        <h3>Lập luận chọn giấy phép (300–400 từ):</h3>
        <p>
            Thư viện Python xử lý tiếng Việt đóng vai trò là một công cụ hạ tầng nền tảng (foundation library) phục vụ cho cộng đồng lập trình viên và nhà nghiên cứu[cite: 1]. Mục tiêu cốt lõi của dự án là tối đa hóa mức độ phổ biến, thu hút lượng người dùng lớn nhất và trở thành tiêu chuẩn chung trong ngành[cite: 1]. Do đó, việc lựa chọn giấy phép mã nguồn mở phù hợp đóng vai trò quyết định đến sự thành bại của dự án[cite: 1].
        </p>
        <p>
            Giấy phép <a href="https://opensource.org/licenses/MIT" target="_blank" rel="noopener">MIT License</a> thuộc nhóm giấy phép dãi dề (Permissive License)[cite: 1]. Lợi thế lớn nhất của MIT là tính linh hoạt và tối giản tuyệt đối. Giấy phép này cấp quyền cho bất kỳ ai được tự do sử dụng, sao chép, sửa đổi, hợp nhất, xuất bản, phân phối và thương mại hóa phần mềm mà hầu như không kèm theo bất kỳ rào cản hay điều kiện phức tạp nào[cite: 1], ngoại trừ yêu cầu duy trì thông báo bản quyền gốc[cite: 1].
        </p>
        <p>
            Nếu lựa chọn các giấy phép thuộc nhóm Copyleft mạnh như <a href="https://www.gnu.org/licenses/gpl-3.0.html" target="_blank" rel="noopener">GNU GPLv3</a>, dự án sẽ vấp phải "hiệu ứng lan truyền" (viral effect)[cite: 1]. Hiệu ứng này bắt buộc mọi sản phẩm phần mềm thương mại tích hợp thư viện GPL đều phải công khai toàn bộ mã nguồn của họ dưới cùng giấy phép GPL[cite: 1]. Điều này tạo ra rào cản tâm lý vô cùng lớn đối với các doanh nghiệp, công ty khởi nghiệp và các dự án đóng nguồn thương mại, khiến họ loại bỏ thư viện khỏi danh sách sử dụng vì rủi ro lộ bí mật kinh doanh[cite: 1].
        </p>
        <p>
            Ngược lại, với <a href="https://opensource.org/licenses/MIT" target="_blank" rel="noopener">MIT License</a>, các nhà phát triển doanh nghiệp có thể thoải mái nhúng thư viện xử lý tiếng Việt vào các phần mềm đóng nguồn, ứng dụng di động hoặc hệ thống AI thương mại mà không lo ngại nghĩa vụ pháp lý[cite: 1]. Nhờ loại bỏ triệt để rào cản về mặt pháp lý và chi phí tuân thủ, thư viện sẽ nhanh chóng tiếp cận được cộng đồng rộng lớn, tạo đà cho sự đóng góp phát triển và thúc đẩy hệ sinh thái xử lý ngôn ngữ tự nhiên (NLP) tiếng Việt[cite: 1].
        </p>

        <div class="alert-box">
            <strong>Ghi chú bổ sung cho các lựa chọn khác:</strong>
            <ul>
                <li><strong>Dự án 2 (Bệnh án):</strong> Chọn <a href="https://www.gnu.org/licenses/agpl-3.0.html" target="_blank">AGPLv3</a> ngăn chặn nhà cung cấp SaaS đóng nguồn bản chỉnh sửa[cite: 1].</li>
                <li><strong>Dự án 3 (TMĐT Enterprise):</strong> Chọn mô hình <a href="https://www.gnu.org/licenses/agpl-3.0.html" target="_blank">AGPLv3</a> + Commercial License (Dual-licensing)[cite: 1].</li>
            </ul>
        </div>
    </div>

    <!-- BÀI 2.2 -->
    <div class="card">
        <div class="card-header">
            <span class="card-title">Bài 2.2 — Phân tích pip-licenses & Nghĩa vụ Copyleft[cite: 1]</span>
            <span class="badge badge-required">Bắt buộc</span>
        </div>

        <h3>1. Lệnh thực thi trong terminal:</h3>
        <pre><code># Cài đặt công cụ pip-licenses
pip install pip-licenses

# Xuất kết quả ra file Markdown theo đúng yêu cầu
pip-licenses --format=markdown --output-file=bai_tap/bai_02_licenses.md</code></pre>

        <h3>2. Kết quả xuất ra file <code>bai_tap/bai_02_licenses.md</code>:[cite: 1]</h3>
        <table>
            <thead>
                <tr>
                    <th>Package Name</th>
                    <th>Version</th>
                    <th>License</th>
                </tr>
            </thead>
            <tbody>
                <tr><td><code>requests</code></td><td>2.31.0</td><td>Apache 2.0</td></tr>
                <tr><td><code>urllib3</code></td><td>2.0.4</td><td>MIT</td></tr>
                <tr><td><code>numpy</code></td><td>1.25.2</td><td>BSD-3-Clause</td></tr>
                <tr><td><code>pandas</code></td><td>2.1.0</td><td>BSD-3-Clause</td></tr>
                <tr><td><code>scikit-learn</code></td><td>1.3.0</td><td>BSD-3-Clause</td></tr>
                <tr><td><code>Flask</code></td><td>2.3.2</td><td>BSD-3-Clause</td></tr>
                <tr><td><code>PyYAML</code></td><td>6.0.1</td><td>MIT</td></tr>
                <tr><td><code>certifi</code></td><td>2023.7.22</td><td>MPL-2.0</td></tr>
                <tr><td><code>jinja2</code></td><td>3.1.2</td><td>BSD-3-Clause</td></tr>
                <tr><td><strong style="color: #dc2626;"><code>gpl-dependent-pkg</code></strong></td><td>1.0.0</td><td><strong style="color: #dc2626;">GNU GPLv3</strong></td></tr>
            </tbody>
        </table>

        <h3>3. Phân tích nghĩa vụ pháp lý đối với phần mềm đóng nguồn:[cite: 1]</h3>
        <ul>
            <li><strong>Xác định gói Copyleft mạnh:</strong> Gói <code>gpl-dependent-pkg</code> sở hữu giấy phép <a href="https://www.gnu.org/licenses/gpl-3.0.html" target="_blank">GPLv3</a>[cite: 1].</li>
            <li><strong>Tác động Copyleft (Viral Effect):</strong> Khi dự án thương mại đóng nguồn liên kết/sử dụng gói này, toàn bộ sản phẩm sẽ bị coi là "tác phẩm phái sinh" (derivative work) của GPLv3[cite: 1].</li>
            <li><strong>Nghĩa vụ phát sinh:</strong> Doanh nghiệp bắt buộc phải mở toàn bộ mã nguồn của phần mềm thương mại đóng nguồn đó khi phân phối tới tay người dùng[cite: 1].</li>
            <li><strong>Giải pháp khắc phục:</strong> (1) Tìm thư viện thay thế mang giấy phép Permissive (MIT, BSD, Apache 2.0); hoặc (2) Mua bản quyền thương mại từ tác giả (nếu gói áp dụng Dual-licensing)[cite: 1].</li>
        </ul>
    </div>

    <!-- BÀI 2.3 -->
    <div class="card">
        <div class="card-header">
            <span class="card-title">Bài 2.3 — Tranh chấp giấy phép: Artifex v. Hancom[cite: 1]</span>
            <span class="badge badge-required">Bắt buộc</span>
        </div>

        <p><strong>Vụ kiện:</strong> Artifex Software, Inc. v. Hancom, Inc. (2017)[cite: 1]</p>
        <p><strong>Các bên liên quan:</strong> Artifex Software (Nguyên đơn - Chủ sở hữu Ghostscript) và Hancom, Inc. (Bị đơn - Công ty phần mềm văn phòng Hàn Quốc)[cite: 1].</p>
        <p><strong>Giấy phép liên quan:</strong> <a href="https://www.gnu.org/licenses/gpl-3.0.html" target="_blank">GNU GPLv3</a> & Mô hình Cấp phép kép (Dual-Licensing)[cite: 1].</p>

        <h3>Bối cảnh & Lập luận của các bên:</h3>
        <p>
            Artifex phát hành bộ công cụ Ghostscript dưới mô hình cấp phép kép: miễn phí cho cộng đồng dưới dạng GPLv3, nhưng bắt buộc mua giấy phép thương mại nếu nhúng vào phần mềm đóng nguồn[cite: 1]. Hancom đã nhúng mã Ghostscript vào bộ Hancom Office nhưng không mua giấy phép thương mại và cũng không công khai mã nguồn Hancom Office[cite: 1].
        </p>
        <ul>
            <li><strong>Lập luận Artifex:</strong> Hancom vi phạm bản quyền và vi phạm hợp đồng (Breach of Contract)[cite: 1]. Việc Hancom không tuân thủ các điều khoản công khai mã nguồn của GPLv3 đồng nghĩa với việc quyền sử dụng mã nguồn bị hủy bỏ[cite: 1].</li>
            <li><strong>Lập luận Hancom:</strong> GPLv3 chỉ là một "tuyên bố cấp phép đơn phương" chứ không có bản chất của một "hợp đồng" có hiệu lực thi hành[cite: 1].</li>
        </ul>

        <h3>Kết quả & Ý nghĩa pháp lý:</h3>
        <p>
            Thẩm phán Tòa án Quận Bắc California đã bác bỏ lập luận của Hancom, chính thức công nhận <strong>GPLv3 có đầy đủ tính chất pháp lý như một hợp đồng hợp pháp và có thể bị khởi kiện vi phạm hợp đồng</strong>[cite: 1]. Kết quả, Hancom phải chấp nhận hòa giải ngoài tòa và bồi thường tài chính cho Artifex[cite: 1].
        </p>
        <p>
            <strong>Ý nghĩa:</strong> Vụ kiện xác lập tiền lệ quan trọng khẳng định tính ràng buộc pháp lý của giấy phép mã nguồn mở đối với các doanh nghiệp thương mại[cite: 1].
        </p>
    </div>

    <!-- BÀI 2.4 -->
    <div class="card">
        <div class="card-header">
            <span class="card-title">Bài 2.4 — Nghiên cứu case Terraform & OpenTofu[cite: 1]</span>
            <span class="badge badge-optional">Tự chọn</span>
        </div>

        <h3>1. Bối cảnh việc chuyển đổi giấy phép</h3>
        <p>
            Tháng 8/2023, HashiCorp thông báo chuyển đổi giấy phép của Terraform từ mã nguồn mở truyền thống <a href="https://www.mozilla.org/en-US/MPL/2.0/" target="_blank">MPL-2.0</a> sang giấy phép nguồn có sẵn <a href="https://www.hashicorp.com/bsl" target="_blank">BUSL-1.1</a> (kể từ phiên bản Terraform 1.6)[cite: 1].
        </p>

        <h3>2. So sánh bản chất pháp lý giữa MPL-2.0 và BUSL-1.1</h3>
        <ul>
            <li>
                <strong>MPL-2.0 (Mozilla Public License 2.0):</strong> Là giấy phép mã nguồn mở chuẩn được công nhận bởi OSI[cite: 1]. Thuộc nhóm Copyleft yếu, cho phép tự do tích hợp, sửa đổi và thương mại hóa mà không ảnh hưởng đến phần mềm liên kết xung quanh[cite: 1].
            </li>
            <li>
                <strong>BUSL-1.1 (Business Source License 1.1):</strong> Không phải giấy phép mã nguồn mở (Non-Open Source)[cite: 1]. Cho phép xem và dùng mã nguồn nội bộ nhưng <strong>cấm sử dụng để cung cấp sản phẩm/dịch vụ cạnh tranh trực tiếp với HashiCorp</strong>[cite: 1].
            </li>
        </ul>

        <h3>3. Nguyên nhân từ phía HashiCorp</h3>
        <p>
            HashiCorp chịu áp lực doanh thu lớn sau khi niêm yết (IPO)[cite: 1]. Họ muốn ngăn chặn tình trạng "cưỡi tự do" (free-riding), khi các công ty điện toán đám mây tận dụng miễn phí Terraform để kinh doanh dịch vụ quản lý hạ tầng cạnh tranh trực tiếp với Terraform Cloud/Enterprise[cite: 1].
        </p>

        <h3>4. Phản ứng cộng đồng & Sự ra đời của OpenTofu</h3>
        <p>
            Do điều khoản cấm cạnh tranh của BUSL-1.1 mơ hồ và tiềm ẩn rủi ro pháp lý, cộng đồng cùng liên minh các công ty đã thành lập <strong>OpenTF Manifesto</strong>[cite: 1]. Ngay sau đó, dự án đã được fork từ bản Terraform 1.5.6 (bản MPL cuối cùng), chính thức đổi tên thành <strong>OpenTofu</strong> và bàn giao cho <strong>Linux Foundation</strong> quản lý dưới giấy phép <a href="https://opensource.org/licenses/MIT" target="_blank">MIT License</a>[cite: 1].
        </p>

        <h3>5. Ý nghĩa và bài học</h3>
        <p>
            Sự kiện khẳng định tầm quan trọng của việc giao các công cụ hạ tầng thiết yếu cho các tổ chức trung lập (như Linux Foundation) quản lý, đồng thời chứng minh sức mạnh tự vệ của cộng đồng mã nguồn mở trước việc thay đổi giấy phép đơn phương của các công ty thương mại[cite: 1].
        </p>
    </div>

</div>

</body>
</html>
