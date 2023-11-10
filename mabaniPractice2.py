student_id = input("Enter your id please: ")
entrance_year = int(student_id[:3])
print(entrance_year)
years_spent = entrance_year - 400
output = "You are a {} years student"
print(output.format(years_spent)) 