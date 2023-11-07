input_a = int(input())
input_b = int(input())

i = 0
for number in range(input_a,input_b + 1):
    i += number
    if i % 3 == 0:
        print("fizz")
    elif i % 5 == 0:
        print("buzz")
    elif (( i % 3 == 0) &  (i % 5 == 0)):
        print("fizzbuzz")
    else:
        print(number)

