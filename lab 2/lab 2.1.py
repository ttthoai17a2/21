import numpy as np

np.random.seed(42)  
nhiet_do = np.random.uniform(18, 35, 30)

nhiet_do = np.round(nhiet_do, 2)

print(nhiet_do)
nhiet_do_trung_binh = np.mean(nhiet_do)
print("Nhiệt độ trung bình trong tháng:", nhiet_do_trung_binh, "độ C")





