alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(text, shift) : 
    text_list = list(text)
    for i in range(len(text_list)) : 
      index_of = alphabet.index(text_list[i])
      index_shifted = index_of + shift
      
      if index_shifted > len(alphabet) - 1 :
        errorIs = len(alphabet) - index_shifted
        text_list[i] = alphabet[errorIs]
      else : 
        text_list[i] = alphabet[index_shifted]

    print(f"The encoded text is {''.join(text_list)}")
def decrypt(text, shift) : 
    text_list = list(text)
    for i in range(len(text_list)) : 
        index_of = alphabet.index(text_list[i])
        index_shifted = index_of - shift
        text_list[i] = alphabet[index_shifted]

    print(f"The decoded text is {''.join(text_list)}")
  
if direction == "encode" : 
    encrypt(text, shift)
elif direction == "decode" : 
    decrypt(text, shift)
else : 
    print("Wrong direction.")    
