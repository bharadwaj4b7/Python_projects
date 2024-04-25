#from alphabets import alphabet
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type encode for enyrypt the message or type decrypt to decode the message \n")
text=input("enter the message \n").lower()
shift=int(input("Enter the shift vealue \n"))

def ceser (direction, text, shift):
    end_message=' '

    for letter in text:
        if letter == ' ':
            end_message+= ' '
        else:
            position = alphabet.index(letter)

            if direction == "encode":
                new_position= (position+shift) % len(alphabet)
            else:
                new_position= (position-shift) % len(alphabet)
            new_code = alphabet[new_position]
            end_message += new_code            
            

    print(f"The {direction}d message is:{end_message}")

ceser(direction, text, shift)    

