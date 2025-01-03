import threading
from urllib.request import urlopen

def fetch_url(url):
    """Hàm gửi yêu cầu HTTP và in kết quả."""
    try:
        with urlopen(url) as response:
            print(f"URL: {url} - Status: {response.status}")
    except Exception as e:
        print(f"Lỗi khi truy cập {url}: {e}")

def main():
    # Danh sách các URL cần gửi yêu cầu
    urls = [
        "https://www.google.com",
        "https://www.python.org",
        "https://www.github.com",
        "https://www.example.com",
    ]

    threads = []

    # Tạo và khởi chạy các luồng để gửi yêu cầu
    for url in urls:
        thread = threading.Thread(target=fetch_url, args=(url,))
        threads.append(thread)
        thread.start()

    # Chờ tất cả các luồng hoàn thành
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()