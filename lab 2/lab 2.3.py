import pandas as pd
import numpy as np

# 1. Đọc dữ liệu từ file CSV
file_path = '21_Hoai_17A2\lab 2\diem_hoc_phan.csv'
data = pd.read_csv(file_path)

# Chuyển đổi dữ liệu sang mảng NumPy
data_np = data.to_numpy()

# 2. Quy đổi từ thang điểm 10 sang điểm tín chỉ
def convert_to_credit_grade(score):
    if 8.5 <= score <= 10:
        return 'A'
    elif 8.0 <= score < 8.5:
        return 'B+'
    elif 7.0 <= score < 8.0:
        return 'B'
    elif 6.5 <= score < 7.0:
        return 'C+'
    elif 5.5 <= score < 6.5:
        return 'C'
    elif 5.0 <= score < 5.5:
        return 'D+'
    elif 4.0 <= score < 5.0:
        return 'D'
    else:
        return 'F'

# Áp dụng quy đổi cho từng cột học phần
grade_columns = ['HP 1', 'HP 2', 'HP 3']
for col in grade_columns:
    data[f'{col} Grade'] = data[col].apply(convert_to_credit_grade)

# 3. Chia tách dữ liệu theo học phần
data_hp1 = data[['id', 'Tên sinh viên', 'HP 1', 'HP 1 Grade']]
data_hp2 = data[['id', 'Tên sinh viên', 'HP 2', 'HP 2 Grade']]
data_hp3 = data[['id', 'Tên sinh viên', 'HP 3', 'HP 3 Grade']]

# 4. Phân tích dữ liệu theo từng học phần
def analyze_scores(data, column_name):
    scores = data[column_name]
    total = scores.sum()
    mean = scores.mean()
    std_dev = scores.std()
    return total, mean, std_dev

results = {}
for col in grade_columns:
    total, mean, std_dev = analyze_scores(data, col)
    results[col] = {
        'Total': total,
        'Mean': mean,
        'Standard Deviation': std_dev
    }

# 5. Phân tích điểm tổng hợp
# Tính số lượng sinh viên đạt từng loại điểm chữ trên tổng số học phần
grade_summary = {}
for grade in ['A', 'B+', 'B', 'C+', 'C', 'D+', 'D', 'F']:
    grade_count = (data[[f'{col} Grade' for col in grade_columns]] == grade).sum().sum()
    grade_summary[grade] = grade_count

# Hiển thị kết quả
print("=== Phân tích theo học phần ===")
for col, stats in results.items():
    print(f"Học phần: {col}")
    print(f"  Tổng điểm: {stats['Total']}")
    print(f"  Điểm trung bình: {stats['Mean']:.2f}")
    print(f"  Độ lệch chuẩn: {stats['Standard Deviation']:.2f}")

print("\n=== Phân tích điểm tổng hợp ===")
for grade, count in grade_summary.items():
    print(f"Điểm {grade}: {count}")