import threading

def print_even_numbers(limit, sync_event_odd, sync_event_even):
    """Luồng in các số chẵn theo thứ tự tăng dần."""
    for num in range(0, limit + 1, 2):
        sync_event_even.wait()  # Chờ tín hiệu từ luồng lẻ
        print(f"Số chẵn: {num}")
        sync_event_even.clear()  # Xóa tín hiệu hiện tại
        sync_event_odd.set()  # Báo hiệu luồng lẻ tiếp tục

def print_odd_numbers(limit, sync_event_odd, sync_event_even):
    """Luồng in các số lẻ theo thứ tự tăng dần."""
    for num in range(1, limit + 1, 2):
        sync_event_odd.wait()  # Chờ tín hiệu từ luồng chẵn
        print(f"Số lẻ: {num}")
        sync_event_odd.clear()  # Xóa tín hiệu hiện tại
        sync_event_even.set()  # Báo hiệu luồng chẵn tiếp tục

def main():
    limit = 10  # Ngưỡng tối đa
    sync_event_odd = threading.Event()
    sync_event_even = threading.Event()

    # Bắt đầu với luồng chẵn
    sync_event_even.set()

    even_thread = threading.Thread(target=print_even_numbers, args=(limit, sync_event_odd, sync_event_even))
    odd_thread = threading.Thread(target=print_odd_numbers, args=(limit, sync_event_odd, sync_event_even))

    even_thread.start()
    odd_thread.start()

    even_thread.join()
    odd_thread.join()

if __name__ == "__main__":
    main()