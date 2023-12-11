import random
word_list = ["ardvark", "baboon", "camel"]

chose_word = random.choice(word_list)
print(f"psst, the solution is {chose_word}")
s = list(chose_word)
print(s)
# print(range(len(s)))
display = []

end_of_game = False

while not end_of_game:
    name = input("Enter a word ").lower()
    for i in s:
              # print(i)
         if i == name:
              display.append(i)
         else:
              display.append("_")
    print(display)


# for i in range(len(s)):
#      display.append(chose_word[i])
#      if chose_word[i]
# print(display)

# guess = str(input()).lower()
# print(guess)
# count = 0
# for chosen_word in word_list:
#     print(chosen_word)
#     for i in chosen_word:
#         if i in guess:
#             count +=1
#             print("match")
#         else:
#             print("no match")
#


