student_name = input("enter student name:")
python_marks  = int(input("enter python marks:"))
sql_marks = int(input("enter sql marks:"))

Total_marks  = python_marks + sql_marks

average_marks = Total_marks / 2
Result = ""
if average_marks >= 80:
  Result = "Excellent"
elif average_marks >= 60:
  Result = "Good"
elif average_marks >= 40:
  Result = "Pass"
else:
  Result = "Fail"

print("Name:", student_name)
print("Total marks:", Total_marks)
print("Average marks:", average_marks)
print("Result:", Result)
