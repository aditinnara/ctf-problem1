import time
import random

# flag = "b42930292c46c1b210106a5527f60e93394ed9664297fe93d4cd0fba49c6ccad"


# Read the flag from flag.txt
with open('flag.txt', 'r') as f:
    flag = f.read().strip()

cheese_textfile = "cheese_list.txt"

welcome =  """
*******************************************
***             Part 1                  ***
***    The Mystery of the CLONED RAT    ***
*******************************************
"""


mouse_standing = """
         _   _
        (q\_/p)
         /. .\        
  ,__   =\_t_/=   
     )   /   \      
    (   ((   ))   
     \  /\) (/\    
      `-\  Y  /    
         nn^nn        
                          
"""
mouse_angry = """
         _   _
        (q\_/p)
         /.V.\        
  ,__   =\_t_/=   
     )   /   \      
    (   ((   ))   
     \  /\) (/\    
      `-\  Y  /    
         nn^nn        
                          
"""
mouse_sitting = """
   _   _
  (q\_/p)
   /. .\.-.....-.     ___,
  =\_t_/=     /  `\  (
    )\ ))__ __\   |___)
   (/-(/`  `nn---'
"""

mouse_with_cheese = """
         _   _
        (q\_/p)
         /. .\         __
  ,__   =\_t_/=      .'o O'-.
     )   /   \      / O o_.-`|   
    (   ((   ))    /O_.-'  O |  
     \  /\) (/\    | o   o  o|   
      `-\  Y  /    |o   o O.-`  
         nn^nn     | O _.-'      
                   '--`         
"""
mouse_with_cheese_bite1 = """
         _   _
        (q\_/p)
         /. .\         __
  ,__   =\_t_/=      .'o O'-.
     )   /   \      / O o_.-`|   
    (   ((   ))      ).-'  O |  
     \  /\) (/\      )   o  o|   
      `-\  Y  /    |o   o O.-`  
         nn^nn     | O _.-'      
                   '--`         
"""
mouse_with_cheese_bite2 = """
         _   _
        (q\_/p)
         /. .\         __
  ,__   =\_t_/=      .'o O'-.
     )   /   \      / O o_.-`|   
    (   ((   ))        )'  O |  
     \  /\) (/\          )  o|   
      `-\  Y  /         ) O.-`  
         nn^nn        ) _.-'      
                   '--`         
"""

def munch_cheese():
    print(mouse_with_cheese)
    print("munch...")
    time.sleep(1)
    print(mouse_with_cheese_bite1)
    print("munch...")
    time.sleep(1)
    print(mouse_with_cheese_bite2)
    print("MUNCH.............\n")
    time.sleep(1)

# turn txtfile of cheeses into a list
def parse_cheeses_txt():
    with open(cheese_textfile, 'r', encoding='utf-8') as file:
        cheeses = [line.strip().lower() for line in file]  
    return cheeses


# mod m inverse of a ==> a*x(mod m) = 1
def mod_inverse(a, m):
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    return None  

# affine encrypt the cheese string
def affine_encrypt(plaintext, a, b):
    m = 26
    ciphertext = ''
    
    # for each char in the given cheese
    for char in plaintext.upper():
        # convert to int and shift s.t. A = 0
        x = ord(char) - ord('A')
        # E(x) = (a * x + b) mod 26
        encrypted_char = (a * x + b) % m
        # turn back into characters
        ciphertext += chr(encrypted_char + ord('A'))
    return ciphertext


def main():
    # parse list of cheeses
    list_of_cheeses = parse_cheeses_txt()

    # set up affine cipher
    # a must be coprime with m
    a = random.choice([1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25])
    # b must be btwn 0 and 25
    b = random.randint(0, 25)

    # choose and encrypt the cheese we want player to guess
    actual_cheese = random.choice(list_of_cheeses).lower()
    encrypted_cheese = affine_encrypt(actual_cheese, a, b)

    # draw out scene
    print(welcome)
    print("The super evil Dr. Lacktoes Inn Tolerant told me he kidnapped my best friend, Squeexy, and replaced him with an evil clone! You look JUST LIKE SQUEEXY, but I'm not sure if you're him or THE CLONE. I've devised a plan to find out if YOU'RE the REAL SQUEEXY! If you're Squeexy, I'll give you the key to the cloning room so you can maul the imposter...\n")
    print("Here's my secret cheese -- if you're Squeexy, you'll be able to guess it: ", encrypted_cheese)

    for i in range(3):
        print("Commands: (g)uess my cheese, (e)ncrypt a cheese, or (h)int")
        choice = input("What would you like to do?\n")
        print()
        if choice == 'g':
            print(mouse_sitting)
            print("SQUEAK SQUEAK SQUEAK")
            time.sleep(1)
            print(mouse_standing)
            print("Is that you, Squeexy? Are you ready to GUESS...MY...CHEEEEEEESE?")
            time.sleep(1)
            print("Remember, this is my encrypted cheese: ", encrypted_cheese)
            guessed_cheese = input("So...what's my cheese?\n").lower()
            munch_cheese()
            if guessed_cheese == actual_cheese:
                print("YUM! MMMMmmmmMMMMmmmMMM!!! Yes...yesssss! That's my cheese!")
                print("Here's the password to the cloning room: ", flag)
                break
            else:
                print(mouse_angry)
                print("BLEHHHHH yuck. THAT'S not my cheese. GET OUT CLONE!!!1111!!!1!!!\n")
                break
        elif choice == 'e':
            cheese_to_encrypt = input("What cheese would you like to encrypt? ").lower()
            if cheese_to_encrypt in list_of_cheeses:
                encrypted_cheese = affine_encrypt(cheese_to_encrypt, a, b)
                print("Here's your encrypted cheese: ", encrypted_cheese)
                print("Not sure why you want it though...*squeak* - oh well!\n")
            else:
                print("I'm sorry I haven't had that cheese before, so I can't encrypt it!\n")
        elif choice == 'h':
            print("Remember that cipher we devised together Squeexy? The one that incorporates your *affinity* for *linear equations*???\n")
        else:
            print("I'm not sure what you mean *squeeeeak*\n")
        print("I don't wanna talk to you too much if you're some suspicious character and not my BFF Squeexy!")
        print("You have " + str(2-i) + " more chances to prove yourself to me!\n")
        

if __name__ == "__main__":
    main()




