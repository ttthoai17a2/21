import threading
import random

def find_max(sub_list):
    """Hàm tìm giá trị lớn nhất của một sub-list"""
    return max(sub_list)

def main():
    # Tạo một list với n phần tử có giá trị ngẫu nhiên từ 0-100
    n = 100
    list_data = [random.randint(0, 100) for _ in range(n)]

    # Chia list thành 4 sub-list
    sub_list_size = n // 4
    sub_lists = [list_data[i:i+sub_list_size] for i in range(0, n, sub_list_size)]

    # Tạo 4 Thread để tìm giá trị lớn nhất của mỗi sub-list
    threads = []
    max_values = []
    for sub_list in sub_lists:
        t = threading.Thread(target=lambda: max_values.append(find_max(sub_list)))
        t.start()
        threads.append(t)

    # Chờ các Thread hoàn thành
    for t in threads:
        t.join()

    # Tìm giá trị lớn nhất của toàn bộ list
    overall_max = max(max_values)
    print(f"Giá trị lớn nhất trong list: {overall_max}")

if __name__ == "__main__":
    main()