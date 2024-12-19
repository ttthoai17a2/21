import requests


api_url = "https://jsonplaceholder.typicode.com/posts"


response = requests.get(api_url)


if response.status_code == 200:
    
    posts = response.json()

    
    print(f"Tổng số bài post: {len(posts)}")

    
    print("Danh sách các bài post:")
    for post in posts:
        print(f"User ID: {post['userId']}")
        print(f"ID: {post['id']}")
        print(f"Title: {post['title']}")
        print(f"Body: {post['body']}")
        print("-" * 40)  
else:
    print("Có lỗi xảy ra khi lấy dữ liệu từ API.")
