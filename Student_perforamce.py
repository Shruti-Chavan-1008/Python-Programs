import pandas as pd
import numpy as np

student_data = pd.read_csv("student_performance_dataset.csv")


# student details fucnction

def student_deatils(data):
    if data.empty:
        print("No student records found.")
        try:
         student_id = int(input("Enter Student ID: "))
        except ValueError:
          print("Please enter a valid numeric Student ID.")
          return
        
        result = data[data["student_id"] == student_id]
        student_id=int(input("enter your student_id : "))
        result = data[data["student_id"] == student_id]
        student = result.iloc[0]
        if result.empty:
                    print("Student ID not found!")
        else:
                     print(f"\nStudy Time: {student['study_time_hours']}")
                     print(f"Attendance Percentage: {student['attendance_percent']}")
                     print(f"Sleep Hours: {student['sleep_hours']}")
                     print(f"Part-Time Job: {student['part_time_job']}")
                     print(f"Previous Grade: {student['previous_grade']}")
                     print(f"Final Exam Score: {student['final_exam_score']}")
                     print(f"Final grade is : {student['final_grade']}")
    pass

while True:
    print("\n===== Select Parental Education =====")
    print("1. High School")
    print("2. Bachelors")
    print("3. Masters")
    print("4. PhD")
    print("5. Analyze All Categories")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "6":
        print("Exiting program. Goodbye!")
        break

    # ---------------- HIGH SCHOOL ----------------
    elif choice == "1":

        high_school = student_data[
            student_data["parental_education"] == "High School"
        ]

        while True:

            print("\n===== High School Students =====")
            print("1. Student Details")
            print("2. Score Summary")
            print("3. Performance Report")
            print("4. Charts & Graphs")
            print("5. Back")

            choice = input("Enter your choice: ")

            if choice == "5":
                  print("Exiting program. Goodbye!")
                  break

            elif choice == "1":
                student_deatils(high_school)


            elif choice == "2":

                print("\n========== Score Summary ==========")
                print(f"Total Student   : {len(high_school)}\n")
                print(f"final Exam Score ")
                print(f"-----------------------")
                print(f"Average Score : { high_school["final_exam_score"].mean()}")
                print(f"Highest Score : { high_school["final_exam_score"].max()}")
                print(f"Lowest Score  : { high_school["final_exam_score"].min()}")
                print(f"\nPrevious Grade ")
                print(f"-----------------------")
                print(f"Average Score : { high_school["previous_grade"].mean()}")
                print(f"\nAttendence")
                print(f"-----------------------")
                print(f"Average : { high_school["attendance_percent"].mean()}")
                print(f"Highest : { high_school["attendance_percent"].max()}")
                print(f"Lowest  : { high_school["attendance_percent"].min()}")

                print(f"\nStudy Hours")
                print(f"-----------------------")
                print(f"Average  : { high_school["study_time_hours"].mean()}")
                print(f"Maximum  : { high_school["study_time_hours"].max()}")
                print(f"Minimum  : { high_school["study_time_hours"].min()}")
                print(f"\nSleep Hours")
                print(f"-----------------------")
                print(f"Average : { high_school["sleep_hours"].mean()}")
                print(f"\nGrade Distribution")
                print(f"-----------------------")
                print(f"Grade A : {high_school[high_school['final_grade']=='A'].shape[0]}")
                print(f"Grade B : {high_school[high_school['final_grade']=='B'].shape[0]}")
                print(f"Grade C : {high_school[high_school['final_grade']=='C'].shape[0]}")
                print(f"Grade D : {high_school[high_school['final_grade']=='D'].shape[0]}")
                print(f"Grade F : {high_school[high_school['final_grade']=='F'].shape[0]}")
               
            elif choice == "3":
                pass

            elif choice == "4":
                pass

            else:
                print("Invalid Choice")

    # ---------------- BACHELORS ----------------
    elif choice == "2":

        bachelors = student_data[
            student_data["parental_education"] == "Bachelors"
        ]

        while True:

            print("\n===== Bachelors Students =====")
            print("1. Student Details")
            print("2. Score Summary")
            print("3. Performance Report")
            print("4. Charts & Graphs")
            print("5. Back")

            choice = input("Enter your choice: ")

            if choice == "5":
                  print("Exiting program. Goodbye!")
                  break

            elif choice == "1":
                 
                student_id=int(input("enter your student_id : "))
                result = bachelors[bachelors["student_id"] == student_id]
                student = result.iloc[0]
                if result.empty:
                    print("Student ID not found!")
                else:
                     print(f"\nStudy Time: {student['study_time_hours']}")
                     print(f"Attendance Percentage: {student['attendance_percent']}")
                     print(f"Sleep Hours: {student['sleep_hours']}")
                     print(f"Part-Time Job: {student['part_time_job']}")
                     print(f"Previous Grade: {student['previous_grade']}")
                     print(f"Final Exam Score: {student['final_exam_score']}")
                     print(f"Final grade is : {student['final_grade']}")     

            elif choice == "2":
                pass

            elif choice == "3":
                pass

            elif choice == "4":
                pass

            else:
                print("Invalid Choice")

    # ---------------- MASTERS ----------------
    elif choice == "3":

        masters = student_data[
            student_data["parental_education"] == "Masters"
        ]

        while True:

            print("\n===== Masters Students =====")
            print("1. Student Details")
            print("2. Score Summary")
            print("3. Performance Report")
            print("4. Charts & Graphs")
            print("5. Back")

            choice = input("Enter your choice: ")

            if choice == "5":
                print("Exiting program. Goodbye!")
                break

            elif choice == "1":
                 
                student_id=int(input("enter your student_id : "))
                result =masters[masters["student_id"] == student_id]
                student = result.iloc[0]
                if result.empty:
                    print("Student ID not found!")
                else:
                     print(f"\nStudy Time: {student['study_time_hours']}")
                     print(f"Attendance Percentage: {student['attendance_percent']}")
                     print(f"Sleep Hours: {student['sleep_hours']}")
                     print(f"Part-Time Job: {student['part_time_job']}")
                     print(f"Previous Grade: {student['previous_grade']}")
                     print(f"Final Exam Score: {student['final_exam_score']}")
                     print(f"Final grade is : {student['final_grade']}")     


            elif choice == "2":
                pass

            elif choice == "3":
                pass

            elif choice == "4":
                pass

            else:
                print("Invalid Choice")

    # ---------------- PHD ----------------
    elif choice == "4":

        phd = student_data[
            student_data["parental_education"] == "PhD"
        ]

        while True:

            print("\n===== PhD Students =====")
            print("1. Student Details")
            print("2. Score Summary")
            print("3. Performance Report")
            print("4. Charts & Graphs")
            print("5. Back")

            choice = input("Enter your choice: ")

            if choice == "5":
                print("Exiting program. Goodbye!")
                break

            elif choice == "1":
                 
                student_id=int(input("enter your student_id : "))
                result = phd[phd["student_id"] == student_id]
                student = result.iloc[0]
                if result.empty:
                    print("Student ID not found!")
                else:
                     print(f"\nStudy Time: {student['study_time_hours']}")
                     print(f"Attendance Percentage: {student['attendance_percent']}")
                     print(f"Sleep Hours: {student['sleep_hours']}")
                     print(f"Part-Time Job: {student['part_time_job']}")
                     print(f"Previous Grade: {student['previous_grade']}")
                     print(f"Final Exam Score: {student['final_exam_score']}")
                     print(f"Final grade is : {student['final_grade']}")     

            elif choice == "2":
                pass

            elif choice == "3":
                pass

            elif choice == "4":
                pass

            else:
                print("Invalid Choice")

    # ---------------- ALL CATEGORIES ----------------
    elif choice == "5":

        while True:

            print("\n===== Analyze All Categories =====")
            print("1. Student Details")
            print("2. Score Summary")
            print("3. Performance Report")
            print("4. Charts & Graphs")
            print("5. Back")

            choice = input("Enter your choice: ")

            if choice == "5":
                print("Exiting program. Goodbye!")
                break

            elif choice == "1":
                 
                student_id=int(input("enter your student_id : "))
                result = student_data[student_data["student_id"] == student_id]
                student = result.iloc[0]
                if result.empty:
                    print("Student ID not found!")
                else:
                     print(f'Parntal_eduaction : {student['Parental_eduaction']}')
                     print(f"\nStudy Time: {student['study_time_hours']}")
                     print(f"Attendance Percentage: {student['attendance_percent']}")
                     print(f"Sleep Hours: {student['sleep_hours']}")
                     print(f"Part-Time Job: {student['part_time_job']}")
                     print(f"Previous Grade: {student['previous_grade']}")
                     print(f"Final Exam Score: {student['final_exam_score']}")
                     print(f"Final grade is : {student['final_grade']}") 

            elif choice == "2":
                pass

            elif choice == "3":
                pass

            elif choice == "4":
                pass

            else:
                print("Invalid Choice")

    else:
        print("Invalid Choice. Please try again.")