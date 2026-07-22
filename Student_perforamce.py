import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


student_data = pd.read_csv("student_performance_dataset.csv")


# student details fucnction

def student_details(data):
    student_id = int(input("Enter your Student ID: "))

    result = data[data["student_id"] == student_id]

    if result.empty:
        print("Student ID not found!")
        return

    student = result.iloc[0]

    print("\n========== Student Details ==========")
    print(f"Student ID: {student['student_id']}")
    print(f"Parental Education: {student['parental_education']}")
    print(f"Study Time: {student['study_time_hours']}")
    print(f"Attendance Percentage: {student['attendance_percent']}")
    print(f"Sleep Hours: {student['sleep_hours']}")
    print(f"Part-Time Job: {student['part_time_job']}")
    print(f"Previous Grade: {student['previous_grade']}")
    print(f"Final Exam Score: {student['final_exam_score']}")
    print(f"Final Grade: {student['final_grade']}")
  

#score summary function

def Score_summary(data):
                print("\n========== Score Summary ==========")
                print(f"Total Student   : {len(data)}\n")
                print(f"final Exam Score ")
                print(f"-----------------------")
                print(f"Average Score : { data["final_exam_score"].mean()}")
                print(f"Highest Score : { data["final_exam_score"].max()}")
                print(f"Lowest Score  : { data["final_exam_score"].min()}")
                print(f"\nPrevious Grade ")
                print(f"-----------------------")
                print(f"Average Score : { data["previous_grade"].mean()}")
                print(f"\nAttendence")
                print(f"-----------------------")
                print(f"Average : { data["attendance_percent"].mean()}")
                print(f"Highest : { data["attendance_percent"].max()}")
                print(f"Lowest  : { data["attendance_percent"].min()}")

                print(f"\nStudy Hours")
                print(f"-----------------------")
                print(f"Average  : { data["study_time_hours"].mean()}")
                print(f"Maximum  : { data["study_time_hours"].max()}")
                print(f"Minimum  : { data["study_time_hours"].min()}")
                print(f"\nSleep Hours")
                print(f"-----------------------")
                print(f"Average : { data["sleep_hours"].mean()}")
                print(f"\nGrade Distribution")
                print(f"-----------------------")
                print(f"Grade A : {data[data['final_grade']=='A'].shape[0]}")
                print(f"Grade B : {data[data['final_grade']=='B'].shape[0]}")
                print(f"Grade C : {data[data['final_grade']=='C'].shape[0]}")
                print(f"Grade D : {data[data['final_grade']=='D'].shape[0]}")
                print(f"Grade F : {data[data['final_grade']=='F'].shape[0]}")
               
# Performance Report Function
def Performance(data):
     student_id = int(input("Enter your Student ID: "))

     result = data[data["student_id"] == student_id]

     if result.empty:
          print("Student ID not found!")
          return
     

     student = result.iloc[0]
     print("\n==========PERFORMANCE EVALUATION ==========")
     print(f"Student ID: {student['student_id']}")
     print(f"Previous Grade: {student['previous_grade']}")
     print(f"Final Exam Score: {student['final_exam_score']}")
     print(f"Final Grade: {student['final_grade']}")
     print(f"Study Time: {student['study_time_hours']}")
     print(f"Attendance Percentage: {student['attendance_percent']}")
     print(f"Sleep Hours: {student['sleep_hours']}")

    #to check the final score
     if student['final_exam_score'] >= 90:
         print("Exam performace : Excellent  ")
     elif student['final_exam_score'] >= 75:
        print("Exam performace :  Good  ")
     elif student['final_exam_score'] >= 60:
         print("Exam performace :  Average ")
     else :
         print("Need Improment")

    # to check the attends
     if student['attendance_percent'] >= 90:
         print("\n\nAttendence: Excellent  ")
     elif student['attendance_percent'] >= 75:
        print("Attendence:  Good  ")
     elif student['attendance_percent'] >= 60:
         print("Attendence:  Average ")
     else :
         print("Need Improment")

     #to check the sleep 
     if student['attendance_percent'] >= 7:
         print("Sleep Quality  :  Healthy  ")
     else :
         print("Sleep Quality : Need Improment")
     
     if student['final_exam_score'] > student['previous_grade']:
         print("Academic Progress : Improved ")  
     elif student['final_exam_score'] == student['previous_grade'] :
         print("Academic Progress : Stable ")
        
     else:
        print("Academic Progress : Declind")


     print("\n========== Recommendation ==========")

# Final Exam Score
     if student["final_exam_score"] < 50:
         print("• Increase daily study time.")
         print("• Practice previous year question papers.")

     elif student["final_exam_score"] < 75:
       print("• Revise difficult topics regularly.")
       print("• Solve more mock tests.")

     else:
       print("• Excellent academic performance. Keep it up!")

# Attendance
     if student["attendance_percent"] < 75:
       print("• Improve your attendance for better understanding of subjects.")

# Study Hours
     if student["study_time_hours"] < 4:
        print("• Try to study at least 4-6 hours every day.")

# Sleep Hours
     if student["sleep_hours"] < 7:
       print("• Get at least 7-8 hours of sleep for better concentration.")

# Previous Grade Comparison
     if student["final_exam_score"] > student["previous_grade"]:
        print("• Great! Your performance has improved.")

     elif student["final_exam_score"] < student["previous_grade"]:
       print("• Your performance has dropped. Focus on revision.")
  
     else:
       print("• Your performance is consistent. Aim for a higher score next time.")




def plotting_graphs(data):

    while True:

        print("\n========== Charts & Graphs ==========")
        print("1. Final Grade Distribution")
        print("2. Study Hours vs Final Exam Score")
        print("3. Attendance vs Final Exam Score")
        print("4. Back")

        graph_choice = input("Enter your choice: ")

        # 1. Final Grade Distribution
        if graph_choice == "1":

            grade_count = data["final_grade"].value_counts().sort_index()

            plt.figure(figsize=(8, 5))

            plt.bar(
                grade_count.index,
                grade_count.values
            )

            plt.title("Final Grade Distribution")
            plt.xlabel("Final Grade")
            plt.ylabel("Number of Students")
            plt.grid(axis="y")
            plt.tight_layout()
            plt.show()

        # 2. Study Hours vs Final Score
        elif graph_choice == "2":

            plt.figure(figsize=(8, 5))

            plt.scatter(
                data["study_time_hours"],
                data["final_exam_score"]
            )

            plt.title("Study Hours vs Final Exam Score")
            plt.xlabel("Study Time Hours")
            plt.ylabel("Final Exam Score")
            plt.grid()
            plt.tight_layout()
            plt.show()

        # 3. Attendance vs Final Score
        elif graph_choice == "3":

            plt.figure(figsize=(8, 5))

            plt.scatter(
                data["attendance_percent"],
                data["final_exam_score"]
            )

            plt.title("Attendance vs Final Exam Score")
            plt.xlabel("Attendance Percentage")
            plt.ylabel("Final Exam Score")
            plt.grid()
            plt.tight_layout()
            plt.show()

        # 4. Back
        elif graph_choice == "4":

            print("Returning to previous menu...")
            break

        else:
            print("Invalid choice. Please enter between 1 and 4.")




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
               student_details(high_school)


            elif choice == "2":
                Score_summary(high_school)
           

            elif choice == "3":
                 Performance(high_school)

            elif choice == "4":
                plotting_graphs(high_school)

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
                 student_details(bachelors)

            elif choice == "2":
                Score_summary(bachelors)

            elif choice == "3":
                Performance(bachelors)

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
                 student_details(masters)  


            elif choice == "2":
               Score_summary(masters)

            elif choice == "3":
                Performance(masters)

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
                student_details(phd) 

            elif choice == "2":
                 Score_summary(phd)

            elif choice == "3":
               Performance(phd)

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
                 print(f'Parntal_eduaction : {student['Parental_eduaction']}')
                 student_details(student_data)

            elif choice == "2":
                Score_summary(student_data)

            elif choice == "3":
                Performance(student_data) 

            elif choice == "4":
                pass

            else:
                print("Invalid Choice")

    else:
        print("Invalid Choice. Please try again.")