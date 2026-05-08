from task_manager import TaskManager
from file_handler import FileHandler
from ui import UI

def main():
    manager = TaskManager()
    # Tải dữ liệu cũ nếu có
    manager.tasks = FileHandler.load_tasks()
    
    while True:
        UI.display_menu()
        choice = UI.get_input("Chọn chức năng (1-5): ")

        if choice == '1':
            UI.show_tasks(manager.tasks)
        
        elif choice == '2':
            title = UI.get_input("Nhập công việc mới: ")
            if title:
                manager.add_task(title)
                FileHandler.save_tasks(manager.tasks)
        
        elif choice == '3':
            UI.show_tasks(manager.tasks)
            try:
                idx = int(UI.get_input("Nhập số thứ tự để thay đổi trạng thái: ")) - 1
                manager.toggle_task(idx)
                FileHandler.save_tasks(manager.tasks)
            except ValueError:
                print("Lỗi: Vui lòng nhập số.")
        
        elif choice == '4':
            UI.show_tasks(manager.tasks)
            try:
                idx = int(UI.get_input("Nhập số thứ tự muốn xóa: ")) - 1
                manager.remove_task(idx)
                FileHandler.save_tasks(manager.tasks)
            except ValueError:
                print("Lỗi: Vui lòng nhập số.")
            
        elif choice == '5':
            print("Đã lưu dữ liệu. Tạm biệt!")
            break
        else:
            print("Lựa chọn không hợp lệ.")

if __name__ == "__main__":
    main()