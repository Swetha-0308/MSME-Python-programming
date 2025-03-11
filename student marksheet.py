class Student:
    def __init__(self, name, roll_number):
        self.name = name
        self.roll_number = roll_number
        self.marks = {}

    def add_marks(self, subject, mark):
        self.marks[subject] = mark

    def display_marks(self):
        print(f"Name: {self.name}")
        print(f"Roll Number: {self.roll_number}")
        print("Marks:")
        for subject, mark in self.marks.items():
            print(f"{subject}: {mark}")

    def calculate_total(self):
        return sum(self.marks.values())

    def calculate_percentage(self):
        total_marks = self.calculate_total()
        percentage = (total_marks / (len(self.marks) * 100)) * 100
        return percentage

    def display_result(self):
        print(f"Name: {self.name}")
        print(f"Roll Number: {self.roll_number}")
        print("Marks:")
        for subject, mark in self.marks.items():
            print(f"{subject}: {mark}")
        print(f"Total: {self.calculate_total()}")
        print(f"Percentage: {self.calculate_percentage():.2f}%")

def main():
    name = input("Enter student's name: ")
    roll_number = input("Enter student's roll number: ")

    student = Student(name, roll_number)

    num_subjects = int(input("Enter number of subjects: "))

    for i in range(num_subjects):
        subject = input(f"Enter subject {i+1} name: ")
        mark = float(input(f"Enter mark for {subject}: "))
        student.add_marks(subject, mark)

    student.display_result()

if __name__ == "__main__":
    main()


