# 21 - Make a program in Python such that given as data the enrolment and 5 grades of a student; Print the enrolment, the average and the word "approved" if the student has an average greater than or equal to 6, and the word "not approved" otherwise. Data: MAT, CAL1, CAL2, CAL3, CAL4, CAL5 Where: MAT is an integer variable that represents the student's enrolment. CAL1, CAL2, CAL3, CAL4 and CAL5 are real-type variables representing the student's 5 grades.

import sys

AVERAGE_PASSED = 6
TOTAL_COUNT = 5

def calculate_enrollment(enrolment_number):

   grades_list = []
   for i in range(1, TOTAL_COUNT + 1):
      grade = float(input(f"Please enter CAL{i}:"))
      grades_list.append(grade)
   
   max_grade = max(grades_list)

   average = sum(grades_list) / len(grades_list)

   enroll_status = "not approved"
   if average >= AVERAGE_PASSED:
      enroll_status = "approved"
   
   print(f"Enrolment number: {enrolment_number}")
   print(f"Maximum grade: {max_grade}")
   print(f"Average grade: {average:.2f}")
   print(f"Status: {enroll_status}")


def main():

   enrolment_number = input("Please Enter the enrolment number:")
   print(f"Please enter the grades between CAL1 and CAL{TOTAL_COUNT}")
   calculate_enrollment(enrolment_number)

   return 0


if __name__ == '__main__':
  sys.exit(main())