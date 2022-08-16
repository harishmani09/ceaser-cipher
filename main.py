# import math
# test_h = int(input('height of wall'))
# test_w = int(input('width of wall'))
# coverage = 5
#
#
# def calc_paint(height, width, cover):
#   area = height * width
#   cans = math.ceil(area / cover)
#   print(f'you will need {cans} cans')
#
#
#
# calc_paint(height = test_h, width = test_w, cover = coverage)


# def prime_calc(number):
#   is_prime = True
#   for i in range( 2, number):
#     if number % i == 0:
#       is_prime = False
#   if is_prime:
#     print('number is prime')
#   else:
#     print('number is not prime')
#
#
# prime_calc(7)

from art import logo
print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']




# def encrypt(plain_text, shift_amount):
#   cipher_text = ''
#   for letter in plain_text:
#     position = alphabet.index(letter)
#     new_position = position+shift_amount
#     cipher_text += alphabet[new_position]
#
#   print(f"The encoded text is {cipher_text}")
#
#
#
#
# def decrypt(cipher_text, shift_amount):
#   word = ''
#   for letter in cipher_text:
#     position = alphabet.index(letter)
#     new_position = position - shift_amount
#     new_letter = alphabet[new_position]
#     word += new_letter
#   print(f" then decoded word is {word}")
#
#
# if direction == 'encode':
#     encrypt(plain_text=text, shift_amount=shift)
# else:
#     decrypt(cipher_text=text, shift_amount=shift)


def caeser(start_text, shift_amount, cipher_direction):
  word = ''

  if cipher_direction == 'decode':
    shift_amount *= -1


  for char in start_text:
    if char in alphabet:
      position = alphabet.index(char)
      new_position = position + shift_amount
      word += alphabet[new_position]
    else:
      word += char
  print(f"The {cipher_direction}d text is {word}")

should_continue = True
while should_continue:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))

  shift = shift % 26
  caeser(start_text=text, shift_amount=shift, cipher_direction=direction)

  decision = input("Type 'yes' if you wish to continue. Else type 'no' \n")
  if decision == 'no':
    should_continue = False
    print('Good Bye!')

