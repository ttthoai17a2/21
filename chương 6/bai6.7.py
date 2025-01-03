import threading
import time

def task(name):
    """Hàm thực hiện nhiệm vụ mô phỏng."""
    print(f"Starting {name}")
    for i in range(5):
        print(f"{name}: {time.ctime()}")
        time.sleep(1)  # Tạm dừng 1 giây để mô phỏng công việc
    print(f"Exiting {name}")

def main():
    # Danh sách tên các luồng
    thread_names = ["Google", "Yahoo", "Facebook"]

    threads = []

    # Tạo và khởi động các luồng
    for name in thread_names:
        thread = threading.Thread(target=task, args=(name,))
        threads.append(thread)
        thread.start()

    # Chờ tất cả các luồng hoàn thành
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()