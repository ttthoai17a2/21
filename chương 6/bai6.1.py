import threading

def print_thread_name():
    """Hàm in tên của luồng hiện tại."""
    print(f"Thread đang chạy: {threading.current_thread().name}")

def main():
    # Số lượng luồng muốn tạo
    num_threads = 5
    threads = []

    # Tạo và khởi chạy các luồng
    for i in range(num_threads):
        thread = threading.Thread(target=print_thread_name, name=f"Thread-{i+1}")
        threads.append(thread)
        thread.start()

    # Chờ tất cả các luồng hoàn thành
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()