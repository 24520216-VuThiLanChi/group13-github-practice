# group13-github-practice

# To Do List Application

Ứng dụng quản lý công việc đơn giản được viết bằng Python, hỗ trợ thêm, xóa, tìm kiếm và lưu danh sách công việc thông qua giao diện menu.
💻 Công nghệ sử dụng
Ngôn ngữ: Python 3.x

Lưu trữ: File Text/JSON (tùy theo file_handler.py bạn viết)

Quản lý mã nguồn: Git & GitHub (theo mô hình Git Flow/Branching)
# 📌 Chức năng chính
Thêm công việc mới

Hiển thị danh sách công việc

Đánh dấu hoàn thành công việc

Xóa công việc

Tìm kiếm công việc

Lưu và đọc dữ liệu từ file

Giao diện menu đơn giản trên terminal

# 📂 Cấu trúc project

to_do_list/

│

├── main.py

├── task_manager.py

├── file_handler.py

├── ui.py

└── README.md

# 📖 Mô tả các file
## main.py

-File chính để chạy chương trình.

-Khởi tạo ứng dụng

-Điều khiển luồng hoạt động chính

-Kết nối các module:
  
  +giao diện (ui.py)
  
  +quản lý công việc (task_manager.py)
  
  +lưu file (file_handler.py)
  
## task_manager.py

-Quản lý toàn bộ logic của danh sách công việc.

-Bao gồm các chức năng:

+Thêm task

+Xóa task

+Cập nhật trạng thái task

+Tìm kiếm task

+Hiển thị danh sách task

## file_handler.py

-Xử lý đọc và ghi dữ liệu.

-Chức năng:

-Lưu danh sách công việc vào file

-Đọc dữ liệu từ file khi khởi động chương trình

-Hỗ trợ lưu trữ dữ liệu lâu dài

## ui.py

-Xử lý giao diện người dùng trên terminal.

-Bao gồm:

-Hiển thị menu

-Nhận input từ người dùng

-Hiển thị thông báo và danh sách công việc

## 🌿 Các nhánh Git

-Branch	Chức năng

-feature-ui-readme: Phát triển giao diện người dùng và cập nhật README

-feature-search-save:	Thêm chức năng tìm kiếm và lưu file

-feature-task-manager:	Xây dựng module quản lý task

-feature-main-menu:	Thiết kế menu chính của chương trình

## ▶️ Cách chạy chương trình

## 📄 License

-Project được sử dụng cho mục đích học tập và thực hành Git/GitHub.
