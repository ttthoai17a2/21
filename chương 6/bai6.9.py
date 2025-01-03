import threading
import time

# Hàm thực hiện công việc của từng luồng
def access_website(website):
    print(f"Starting {website} at {time.strftime('%Y-%m-%d %H:%M:%S')}")
    time.sleep(2)  # Giả lập thời gian truy cập website
    print(f"Exiting {website} at {time.strftime('%Y-%m-%d %H:%M:%S')}")

# Danh sách các website cần truy cập
websites = ["Google", "Yahoo", "Facebook"]

# Tạo danh sách các luồng
threads = []

for website in websites:
    thread = threading.Thread(target=access_website, args=(website,))
    threads.append(thread)
    thread.start()

# Chờ tất cả các luồng hoàn thành
for thread in threads:
    thread.join()

print("All threads have finished.")