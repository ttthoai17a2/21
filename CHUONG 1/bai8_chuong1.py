class Employee:
    def __init__(self, name, birth_date, hire_date):
        self.name = name                    
        self.birth_date = birth_date        
        self.hire_date = hire_date          

    
    def display(self):
        print(f"Họ và tên: {self.name}")
        print("Ngày sinh: ", end="")
        self.birth_date.display()
        print("Ngày vào công ty: ", end="")
        self.hire_date.display()


class Date:
    def __init__(self, day=1, month=1, year=2000):
        self.day = day
        self.month = month
        self.year = year

    def is_leap_year(self):
        if (self.year % 4 == 0 and self.year % 100 != 0) or (self.year % 400 == 0):
            return True
        return False

    def days_in_month(self):
        if self.month in [1, 3, 5, 7, 8, 10, 12]:
            return 31
        elif self.month in [4, 6, 9, 11]:
            return 30
        elif self.month == 2:
            return 29 if self.is_leap_year() else 28
        return 0

    def display(self):
        print(f"{self.day}/{self.month}/{self.year}")

    def next(self):
        if self.day < self.days_in_month():
            self.day += 1
        else:
            self.day = 1
            if self.month < 12:
                self.month += 1
            else:
                self.month = 1
                self.year += 1


birth_date = Date(15, 6, 1990)  
hire_date = Date(1, 9, 2015)    
employee = Employee("Nguyễn Văn A", birth_date, hire_date)

employee.display()
