import math

def paint_calc(height,width,coverage):
    number_of_cans = (height * width)/cover
    round_up_cans = math.ceil(number_of_cans)
    print(f"you'll need {round_up_cans} cans of paint")

test_h = int(input())
test_w = int(input())
coverage = 5
cover =int(coverage)

paint_calc(height=test_h,width=test_w,cover=coverage)