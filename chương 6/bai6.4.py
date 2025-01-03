import threading

# Biến toàn cục để lưu kết quả giai thừa
factorial_result = 1
lock = threading.Lock()

def calculate_partial_factorial(start, end):
    """Hàm tính tích các số trong khoảng [start, end]."""
    global factorial_result
    partial_result = 1
    for num in range(start, end + 1):
        partial_result *= num

    # Sử dụng khóa để tránh xung đột khi cập nhật kết quả toàn cục
    with lock:
        factorial_result *= partial_result

def main():
    number = 10  # Số cần tính giai thừa
    num_threads = 4  # Số luồng muốn sử dụng
    threads = []
    step = number // num_threads

    # Chia dãy số thành các phần cho mỗi luồng
    for i in range(num_threads):
        start = i * step + 1
        end = (i + 1) * step if i < num_threads - 1 else number
        thread = threading.Thread(target=calculate_partial_factorial, args=(start, end))
        threads.append(thread)
        thread.start()

    # Chờ tất cả các luồng hoàn thành
    for thread in threads:
        thread.join()

    print(f"Giai thừa của {number} là: {factorial_result}")

if __name__ == "__main__":
    main()