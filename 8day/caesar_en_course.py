import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

user = True

def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  shift_positive = shift_amount
  if cipher_direction == "decode":
    shift_amount *= -1
  for char in start_text:
    if char == " " : 
      end_text += " "
    else :
      position = alphabet.index(char) 
      if (shift_positive + position) >= len(alphabet) :       
        new_position = (shift_amount + position) % len(alphabet)
      else : 
        new_position = position + shift_amount
      
      end_text += alphabet[new_position]
    
  print(f"Here's the {cipher_direction}d result: {end_text}")

print(art.logo)

while user :
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  

  caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
  user = input("Type 'yes' if you want to go again. Otherwise type 'no'." )
  if user == "no" : 
    user = False