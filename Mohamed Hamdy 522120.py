txt = "Hello python"
print(txt[-1::-1])
#-----------------------
name = "Hello Python"
string = list(name)
string.reverse()
txt1 = "".join(string)
print(txt1)
#---------------------------------------------
string = "hello doctor"
print(string.title())

#---------------------------------------------
def shift_string(string):
    new_string = ''
    for letter in string:
      next_letter = letter
      if letter.islower():
        next_letter = chr(ord(letter) + 1)
        if next_letter == 'z' :
          next_letter = 'a'
      elif letter.isupper():
        next_letter = chr(ord(letter) + 1)
        if next_letter == 'Z' :
            next_letter = 'A'
      new_string += next_letter
    return new_string

print(shift_string("fjhubHBJSCKLnfvoi"))
#---------------------------------------------
import re

def rem_vowel(string):
    vowel_to_number = {"a": "5", "e": "9", "i": "8", "o": "0", "u": "2", "A": "7", "E": "9", "I": "3", "O": "4", "U": "5"}
    return re.sub("[aeiouAEIOU]", lambda x: vowel_to_number[x.group()], string)

string = "Mohamed Hamdy Mohamed Salah Hefni Ellaban"
print(rem_vowel(string))