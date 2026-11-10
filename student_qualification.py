# Author: Oluwanifemi Abiona
# File Name: student_qualification.py
# Description: This application accepts student names and GPAs, 
# testing whether each student qualifies for the Dean's List or Honor Roll.
# Processing stops when the user enters 'ZZZ' as the last name.

def main():
    print("--- Student Qualification Checker ---")
    print("Enter 'ZZZ' as the last name to exit.\n")
    
    while True:
        # Ask for and accept a student's last name
        last_name = input("Enter student's last name: ")
        
        # Quit processing if the last name is 'ZZZ' (case-insensitive check)
        if last_name.upper() == 'ZZZ':
            print("\nExiting program. Goodbye!")
            break
            
        # Ask for and accept a student's first name
        first_name = input("Enter student's first name: ")
        
        # Ask for and accept the student's GPA as a float
        try:
            gpa = float(input("Enter student's GPA: "))
        except ValueError:
            print("Invalid GPA input. Please enter a numerical value.\n")
            continue
            
        # Test if the student qualifies for the Dean's List (3.5 or greater)
        if gpa >= 3.5:
            print(f"{first_name} {last_name} has made the Dean's List!\n")
            
        # Test if the student qualifies for the Honor Roll (3.25 or greater)
        elif gpa >= 3.25:
            print(f"{first_name} {last_name} has made the Honor Roll!\n")
            
        else:
            print(f"{first_name} {last_name} did not qualify for the Dean's List or Honor Roll.\n")

if __name__ == "__main__":
    main()