import json

python_obj = {
    "name": "Nguyen Van A",
    "age": 30,
    "city": "Hanoi",
    "skills": ["Python", "Java", "C++"]
}


json_str = json.dumps(python_obj)


print("Chuỗi JSON:", json_str)

json_data = json.loads(json_str)

for key, value in json_data.items():
    print(f"{key}: {value}")
