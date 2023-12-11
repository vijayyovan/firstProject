import os
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# def encrypt(text, shift):

userinput = input("enter a single character en for encryption or de for decryption\n")

text = str(input("Enter the string?"))
shift = int(input("enter shift number"))

shift = shift % 26
def caesar(start_text, shift_amount, cipher_direction):
    result =""
    if cipher_direction == "decode":
        shift_amount *= -1
    for letter in start_text:
      if letter in alphabet:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        result += alphabet[new_position]
      else:
        result += letter
    print(result)

caesar(start_text=text,shift_amount=shift,cipher_direction=userinput)









