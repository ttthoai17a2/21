import threading
import random

def calculate_sum(sub_list, result, index):
    """Hàm tính tổng các phần tử trong một danh sách con."""
    result[index] = sum(sub_list)
    print(f"Thread {index + 1}: Tổng = {result[index]}")

def main():
    # Nhập số phần tử và số luồng
    n = int(input("Nhập số phần tử: "))
    num_threads = int(input("Nhập vào số thread: "))

    # Tạo danh sách ngẫu nhiên với các giá trị từ 0 đến 10
    data = [random.randint(0, 10) for _ in range(n)]
    print(f"List: {data}")

    # Chia danh sách thành các phần
    chunk_size = n // num_threads
    chunks = [data[i * chunk_size:(i + 1) * chunk_size] for i in range(num_threads - 1)]
    chunks.append(data[(num_threads - 1) * chunk_size:])  # Phần còn lại

    # Lưu kết quả tổng của từng luồng
    result = [0] * num_threads
    threads = []

    # Tạo và khởi chạy các luồng
    for i in range(num_threads):
        thread = threading.Thread(target=calculate_sum, args=(chunks[i], result, i))
        threads.append(thread)
        thread.start()

    # Chờ tất cả các luồng hoàn thành
    for thread in threads:
        thread.join()

    # Tính tổng toàn bộ danh sách
    total_sum = sum(result)
    print(f"Tổng list = {total_sum}")

if __name__ == "__main__":
    main()