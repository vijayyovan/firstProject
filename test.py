student_height = input().split()



for n in range(0, len(student_height)):
    s = int(student_height[n])

largest = student_height[0]

for i in range(0, len(student_height)):
    if student_height[i] > largest:
        largest = student_height[i]
print(largest)





