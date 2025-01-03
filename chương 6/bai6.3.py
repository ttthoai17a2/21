import threading

def print_even_numbers(start, end):
    """Hàm in các số chẵn trong khoảng [start, end]."""
    print("Số chẵn:")
    for num in range(start, end + 1):
        if num % 2 == 0:
            print(num, end=" ")
    print()

def print_odd_numbers(start, end):
    """Hàm in các số lẻ trong khoảng [start, end]."""
    print("Số lẻ:")
    for num in range(start, end + 1):
        if num % 2 != 0:
            print(num, end=" ")
    print()

def main():
    start = 30
    end = 50

    # Tạo luồng cho số chẵn và số lẻ
    even_thread = threading.Thread(target=print_even_numbers, args=(start, end))
    odd_thread = threading.Thread(target=print_odd_numbers, args=(start, end))

    # Khởi chạy các luồng
    even_thread.start()
    odd_thread.start()

    # Chờ các luồng hoàn thành
    even_thread.join()
    odd_thread.join()

if __name__ == "__main__":
    main()