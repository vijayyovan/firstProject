student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}

student_performance = {}

for key,value in student_scores.items():
    if value >= 90:
        student_performance[key] = "outperformance"
    elif value >= 80:
        student_performance[key] = "excellent"
    else:
        student_performance[key] = "fail"
print(student_performance)
