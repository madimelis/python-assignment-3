import os
import csv 
import json

#Practice 4
#D1
folder = r"C:\Users\Админ\OneDrive\Рабочий стол\python-assignment-3"
foldername = "output"
"""print("Checkintg file...")
if not os.path.exists(os.path.join(folder, "students.csv")):   
    print("Error: file students.csv not found. Please download the file from LMS")
    exit() 
print("File found: students.csv")

print(" ")
print("Checking output folder...")
if not os.path.exists(os.path.join(folder, foldername)):
    os.makedirs(os.path.join(folder, foldername))  
    print("Output folder created: output/")
else:    print("Output folder already exists: output/")

print(" ")

#D2

students = []
with open(os.path.join(folder, "students.csv"), encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append(row)
print(f"Total students: {len(students)}")
print(" ")
print("First 5 rows:")
print("-" * 30)
for student in students[:5]:
    print(f"{student['student_id']} | {student['age']} | {student['gender']} | {student['country']} | GPA: {student['GPA']}")
print("-" * 30)
print(" ")
print(" ")

#D3

sorted_students = sorted(students, key=lambda x: float(x['final_exam_score']), reverse = True)
top10 = sorted_students[:10]
print("-" * 30)
print("Top 10 Students by Exam Score")
print("-" * 30)
for i in range(len(top10)):
    student = top10[i]
    print(f"{i+1}. {student['student_id']} | {student['country']} | {student['major']} | Score: {student['final_exam_score']} | GPA: {student['GPA']}")
print(" ")
print(" ")

#D4

result = {
    "analysis": "Top 10 Students by Exam Score",
    "total_students": len(students),
    "top_10": []
}
for i in range(len(top10)):
    student = top10[i]
    result["top_10"].append({
        "rank": i + 1,
        "student_id": student["student_id"],
        "country": student["country"],
        "major": student["major"],
        "final_exam_score": float(student["final_exam_score"]),
        "GPA": float(student["GPA"])
    })

with open(os.path.join(folder, foldername, "result.json"), "w", encoding="utf-8") as f:
    json.dump(result, f, indent=4)

print("=" * 30)
print("ANALYSIS RESULT")
print("=" * 30)
print(f"Analysis : {result['analysis']}")
print(f"Total students : {result['total_students']}")
print("Top 10 saved to output/result.json")
print("=" * 30)
print("Result saved to output/result.json")
"""

# Practice 5
#D1
def check_files():
    print("Checking file...")
    file_path = os.path.join(folder, "students.csv")
    if not os.path.exists(file_path):
        print("Error: students.csv not found. Please download the file from LMS.")
        return False
    print("File found: students.csv")
    print(" ")
    print("Checking output folder...")
    output_path = os.path.join(folder, foldername)
    if not os.path.exists(output_path):
        os.makedirs(output_path)
        print("Output folder created: output/")
    else:
        print("Output folder already exists: output/")
    return True


def load_data(filename):    #D4
    print("Loading data...")
    
    try:
        students = []
        with open(filename, encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                students.append(row)
        
        print(f"Data loaded successfully: {len(students)} students")
        return students

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found. Please check the filename.")
        return []

    except Exception as e:
        print(f"Error: {e}")
        return []
    

def preview_data(students, n = 5):
    print(f"First {n} rows:")
    print("-" * 30)
    for student in students[:n]:
        print(f"{student['student_id']} | {student['age']} | {student['gender']} | {student['country']} | GPA: {student['GPA']}")
    print("-" * 30)

#D2

def get_top_students(students, n = 10):
    sorted_students = sorted(students, key=lambda x: float(x['final_exam_score']), reverse=True)
    return sorted_students[:n]

def print_top_students(top_students, title):
    print("-" * 30)
    print(title)
    print("-" * 30)
    
    for i in range(len(top_students)):
        s = top_students[i]
        print(f"{i+1}. {s['student_id']} | {s['country']} | {s['major']} | Score: {s['final_exam_score']} | GPA: {s['GPA']}")
    print("-" * 30)

#D3
def lambda_operations(students):
    print("-" * 30)
    print("Lambda / Map / Filter")
    print("-" * 30)
    print(" ")

    top_scorers = list(filter(lambda s: float(s['final_exam_score']) > 95, students))
    print(f"Students with score > 95 : {len(top_scorers)}")
    gpa_values = list(map(lambda s: float(s['GPA']),students))
    print(f"GPA values (first 5) : {gpa_values[:5]}")
    print(" ")
    good_assignments = list(filter(lambda s: float(s['assignment_score']) > 90, students))
    print(f"Students assignment > 90 : {len(good_assignments)}")
    print("-" * 30)


# Main execution
def main():
    if not check_files():
        return
    
    file_path = os.path.join(folder, "students.csv")
    print(" ")
    students = load_data(file_path)
    print(" ")
    preview_data(students) 
    print(" ")

    top10 = get_top_students(students)
    print_top_students(top10, "Top 10 Students by Exam Score")
    print(" ")
    top5 = get_top_students(students, 5)
    print_top_students(top5, "Top 5 Students by Exam Score")

    lambda_operations(students)

    load_data("wrong_file.csv") 

if __name__ == "__main__":    main()

#Practice 6
#D1


    
    

