#grade calculator
#assign a letter grade based on a students score: A(90-100), B(80-89), C (70-79),
# D(60-69), F (Below 60)

score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"      
print("Grade:",  grade)            