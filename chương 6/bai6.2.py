import threading
import urllib.request

def download_file(url, filename):
    """Hàm tải xuống tệp từ URL và lưu vào tệp local."""
    try:
        urllib.request.urlretrieve(url, filename)
        print(f"Đã tải xong: {filename}")
    except Exception as e:
        print(f"Lỗi khi tải {filename}: {e}")

def main():
    # Danh sách URL và tên tệp tương ứng
    files_to_download = [
        ("https://example.com/file1.zip", "file1.zip"),
        ("https://example.com/file2.zip", "file2.zip"),
        ("https://example.com/file3.zip", "file3.zip"),
    ]

    threads = []

    # Tạo và khởi chạy luồng cho từng tệp
    for url, filename in files_to_download:
        thread = threading.Thread(target=download_file, args=(url, filename))
        threads.append(thread)
        thread.start()

    # Chờ tất cả các luồng hoàn thành
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()