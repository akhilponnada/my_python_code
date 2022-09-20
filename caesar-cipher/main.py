alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z' ]

from art import logo
print(logo)

cont = True

def caesar(start_text, shift_number, message_direction):
  end_text = ""
  for letter in start_text:
    if letter in alphabet:
      position = alphabet.index(letter)
      
      if direction == "encode":
        position = alphabet.index(letter)
        new_position = position + shift
        new_letter = alphabet[new_position]
        end_text += new_letter
        
      elif direction == "decode":
        position = alphabet.index(letter)
        new_position = position - shift
        end_text += alphabet[new_position]
        
    else:
      end_text += letter
  print(f"the {direction}d text is {end_text}")    


while cont:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  
  shift = shift % 26
  
  caesar(start_text = text, shift_number = shift, message_direction = direction)

  to_cont = input("do you want to restart? type 'yes' or 'no' ")
  if to_cont == "yes":
    cont = True
  elif to_cont == "no":
    cont = False
    print("goodbye")
  

