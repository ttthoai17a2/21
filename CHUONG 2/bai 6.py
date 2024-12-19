import json

json_data = '''
{
    "name": "Nguyen Van A",
    "age": 30,
    "city": "Hanoi",
    "skills": ["Python", "Java", "C++"]
}
'''

python_data = json.loads(json_data)

print(python_data)
print(type(python_data))  