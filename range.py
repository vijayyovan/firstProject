# print(fruit)
# print(fruit +" pie")

input_a = int(input())
print("enter intial range",input_a)

input_b = int(input())
print("enter second range", input_b)

sum = 0
for number in range(input_a, input_b + 1):
    if number % 2 == 0:
        sum = sum + number
        print(sum)

