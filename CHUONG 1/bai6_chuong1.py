class Stack:
    def __init__(self, size):
       
        self.size = size
        self.stack = []  
        self.top = -1   

    
    def push(self, value):
        if self.isFull():
            print("Ngăn xếp đã đầy!")
        else:
            self.stack.append(float(value))  
            self.top += 1
            print(f"Đã thêm {value} vào ngăn xếp.")

    
    def pop(self):
        if self.isEmpty():
            print("Ngăn xếp rỗng, không thể pop!")
            return None
        else:
            popped_value = self.stack.pop()  
            self.top -= 1
            print(f"Đã lấy {popped_value} ra khỏi ngăn xếp.")
            return popped_value

    
    def isEmpty(self):
        return self.top == -1

    
    def isFull(self):
        return self.top == self.size - 1

    
    def count(self):
        return self.top + 1

    
    def print(self):
        if self.isEmpty():
            print("Ngăn xếp rỗng.")
        else:
            print("Nội dung ngăn xếp (từ đỉnh đến đáy):")
            for i in range(self.top, -1, -1):  
                print(self.stack[i])

    
    def __del__(self):
        del self.stack
        print("Ngăn xếp đã bị hủy.")


stack = Stack(5)  
stack.push(1.2)   
stack.push(3.4)  
stack.push(5.6)   

stack.print()     

stack.pop()       
stack.print()     
