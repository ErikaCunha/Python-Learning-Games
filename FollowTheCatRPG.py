print(r'''
                   |\___/|                      
                   )     (    
                  =\     /=   
                    )===(    
                   /     \     
                   |     |        
                  /       \         
                  \       /         
           _/\_/\_/\_   _/_/\_/\_/\_
      ''')
followthecat = input("Hello, magical being. Do you wish to find out which type of witch you are? (yes/no)\n").lower()

nature = 0
cosmic = 0
knowledge = 0
shadow = 0

if followthecat == "yes":
    print("Perrrrfect! Follow me...")
    path = input('You follow the cat through...'
                     '1. a quiet forest\n'
                     '2. Beneath the starry sky\n'
                     '3. an ancient library\n'
                     '4. a ritual with candles and mirrors\n'
                     'Type the number of your choice:\n')
    if path == "1":
        nature += 1
    elif path == "2":
        cosmic += 1
    elif path == "3":
        knowledge += 1
    elif path == "4":
        shadow += 1

    print("You continue following the cat and reach a crossroads...a magical object is floating in the air.\n")
    object = input('which magical object do you see?\n'
                      '1. Rose quartz crystal\n'
                      '2. Astrological chart\n'
                      '3. Leather-bound grimoire\n'
                      '4. Obsidian mirror'
                      'Type the number of your choice:\n')
    if object == "1":
        nature += 1
    elif object == "2":
        cosmic += 1
    elif object == "3":
        knowledge += 1
    elif object == "4":
        shadow += 1

    print("The object floats down and you pick it up.\n")
    energy = input('What kind of energy do you feel?\n'
                      '1. Healing and caring\n' 
                      '2. Sensing and foreseeing\n' 
                      '3. Learning and teaching\n' 
                      '4. Transforming and rebirthing\n'
                      'Type the number of your choice:\n')
    if energy == "1":
        nature += 1 
    elif energy == "2":
        cosmic += 1
    elif energy == "3":
        knowledge += 1
    elif energy == "4":
        shadow += 1

    print("The cat meows, making you realise that a shadow is approching you\n")
    shadow_figure = input('which color is the shadow?\n'
                      '1. Moss green\n'
                      '2. Deep blue\n'
                      '3. Dark purple\n'
                      '4. Velvet black\n'
                      'Type the number of your choice:\n')
    if shadow_figure == "1":
        nature += 1
    elif shadow_figure == "2":
        cosmic += 1
    elif shadow_figure == "3":
        knowledge += 1
    elif shadow_figure == "4":
        shadow += 1

    print("The shadow reveals itself to be a mystical creature.\n")
    creature = input('which mystical creature is it?\n'
                      '1. A wise owl\n'
                      '2. A glowing phoenix\n'
                      '3. A clever fox\n'
                      '4. A mysterious black raven\n'
                      'Type the number of your choice:\n')
    if creature == "1":
        nature += 1
    elif creature == "2":
        cosmic += 1
    elif creature == "3":
        knowledge += 1
    elif creature == "4":
        shadow += 1

    print("The cat and the creature talked a little and then the cat looks at you and meows.\n ")

    print("The cat looks at you and says: 'It's time to discover your witch type!✨'\n")

    if nature >= max(cosmic, knowledge, shadow):
        print("🧙‍♀️ Nature Witch - You are deeply connected to the Earth and its rhythms.")
    elif cosmic >= max(nature, knowledge, shadow):
        print("🌌 Cosmic Witch - You channel the stars and universal energy.")
    elif knowledge >= max(nature, cosmic, shadow):
        print("📜 Knowledge Witch - You wield wisdom and ancient magical texts.")
    elif shadow >= max(nature, cosmic, knowledge):
        print("🕯️ Shadow Witch - You embrace mystery and transformation through the unseen.")

else:
    print("... You're not ready for a magical life. Goodbye.")

