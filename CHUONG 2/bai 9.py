import json

with open("company_data.json", "r", encoding="utf-8") as file:
    data = json.load(file)


company_name = data["company"]["name"]
company_address = data["company"]["address"]
departments = data["company"]["departments"]


total_employees = sum(len(dept["employees"]) for dept in departments)


print(f"Tên công ty: {company_name}")
print(f"Địa chỉ: {company_address}")
print("-----Thống kê nhân viên theo đơn vị------")


for idx, dept in enumerate(departments, start=1):
    department_name = dept["name"]
    employee_count = len(dept["employees"])
    percentage = (employee_count / total_employees) * 100

    
    print(f"{idx}./Tên đơn vị: {department_name}.")
    print(f"- Số nhân viên: {employee_count}")
    print(f"- Tỷ lệ: {percentage:.2f}%")
