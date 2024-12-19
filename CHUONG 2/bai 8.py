import json

python_dict = {
    "name": "Nguyen Van A",
    "age": 30,
    "city": "Hanoi",
    "skills": ["Python", "Java", "C++"]
}

json_str = json.dumps(python_dict, sort_keys=True, indent=4)

print("Chuỗi JSON sắp xếp theo khóa và thụt lề 4:")
print(json_str)
