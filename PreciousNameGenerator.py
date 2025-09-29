print(r'''
       __________________
    .-'  \ _.-''-._ /  '-.
  .-/\   .'.      .'.   /\-.
 _'/  \.'   '.  .'   './  \'_
:======:======::======:======:  
 '. '.  \     ''     /  .' .'
   '. .  \   :  :   /  . .'
     '.'  \  '  '  /  '.'
       ':  \:    :/  :'
         '. \    / .'
           '.\  /.'    
             '\/'  
   _ __   __ _ _ __ ___   ___ 
  | '_ \ / _` | '_ ` _ \ / _ \
  | | | | (_| | | | | | |  __/
  |_| |_|\__,_|_| |_| |_|\___|
      ''')

print("Hello, dearest friend. Let's find out your precious stone name! For that I'll need some answers...")

name = input("What's your first name?\n")
three_name = name[0:3].lower()
monthbirth = input("What month were you born?\n")
three_months = monthbirth[0:3].lower()
color = input("What is your favorite color\n")

stone_base = three_months + three_name
if stone_base.endswith('i'):
    stone_name = f"{color} {stone_base}te"
else:
    stone_name = f"{color} {stone_base}ite"

print(f"Your magical stone name is {stone_name}!")

