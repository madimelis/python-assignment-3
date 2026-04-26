import os
import csv 
import json

#task 1
class FileManager:
    def __init__(self, folder, filename):
        self.folder = folder
        self.filename = filename

    def check_file(self):
        print("Checking file...")
        file_path = os.path.join(self.folder, self.filename)
        if not os.path.exists(file_path):
            print(f"Error: {self.filename} not found")
            return False
        print(f"File found: {self.filename}")
        print(" ")
        return True
    
    def check_output_folder(self, folder = "output"):
        print("Checking output folder...")
        output_path = os.path.join(self.folder, folder)
        if not os.path.exists(output_path):
            os.makedirs(output_path)
            print(f"Output folder created: {folder}/")
        else:
            print(f"Output folder already exists: {folder}/")
        print(" ")
        return True

#task 2

class DataLoader:
    def __init__(self, folder, filename):
        self.folder = folder
        self.filename = filename
        self.students = []

    def load(self):
        print("Loading data...")
        
        try:
            with open(os.path.join(self.folder, self.filename), encoding="utf-8") as file:
                reader = csv.DictReader(file)
                self.students = [row for row in reader]
            
            print(f"Data loaded successfully: {len(self.students)} students")
            print(" ")
            return self.students

        except FileNotFoundError:
            print(f"Error: File '{self.filename}' not found. Please check the filename.")
            return self.students

        except Exception as e:
            print(f"Error: {e}")
            return []
    

    def preview_data(self, n = 5):
        print(f"First {n} rows:")
        print("-" * 30)
        for student in self.students[:n]:
            print(f"{student['student_id']} | {student['age']} | {student['gender']} | {student['country']} | GPA: {student['GPA']}")
        print("-" * 30)

#task 3

class DataAnalyzer:
    def __init__(self, students):
        self.students = students

    def analyze(self):
        valid_students = []
        for s in self.students:
            try:
                s['final_exam_score'] = float(s['final_exam_score'])
                s['GPA'] = float(s['GPA'])
                valid_students.append(s)
            except ValueError:
                print(f"Warning: could not convert value for student {s.get('student_id')} — skipping row.")
                continue
        sorted_students = sorted(valid_students, key=lambda x: x['final_exam_score'], reverse=True)
        self.result = {"top10": sorted_students[:10],}
        return self.result
    
    def print_results(self):
        print("-" * 30)
        print("Top 10 Students by Exam Score")
        print("-" * 30)

        for i in range(len(self.result.get("top10", []))):
            s = self.result.get("top10", [])[i]
            print(f"{i+1}. {s['student_id']} | {s['country']} | {s['major']} | Score: {s['final_exam_score']} | GPA: {s['GPA']}")

#task 4

class ResultSaver:
    def __init__(self, result, folder, output_path):
        self.result = result
        self.folder = folder
        self.output_path = output_path

    def save_json(self):
        try:
            with open(os.path.join(self.folder, self.output_path), 'w', encoding='utf-8') as f:
                json.dump(self.result, f, indent=4)

            print(f"Result saved to {self.output_path}")

        except Exception as e:
            print(f"Error saving file: {e}")
    
#task 5

def main():
    folder = r"C:\Users\Админ\OneDrive\Рабочий стол\python-assignment-3"
    file_manager = FileManager(folder, "students.csv")

    if not file_manager.check_file():
        print('Stopping program.')
        return

    file_manager.check_output_folder()

    dl = DataLoader(folder, "students.csv")
    dl.load()
    dl.preview_data()

    analyser = DataAnalyzer(dl.students)
    analyser.analyze()
    analyser.print_results()

    saver = ResultSaver(analyser.result, folder, 'output/result.json')
    saver.save_json()


if __name__ == "__main__":
    main()

