print(r"""
              .  _    .-..
             ( `' ;  .( ; ;
            .-`()'.;(_.{}:'
            `..'`,' / ' ;.)
              `-'\ /  `-'
                  X
                 _U_
                 \ /
                 | |
                 | |
                /   \
               |    ;|
               |    ;|
               |   ;;|
               |..;;;|
               |;;;;;|   
               `;;;;;'
                `''`
      """)

print("Hello, dearest friend. Let's find out the percentage of essential oil in your " \
"magickal blend! " \
"But, first be aware of wich kind of Essencial Oil you are using for each type of blend!"\
"Some EO can be toxic if used inappropriately.\n")

oil_blend = float(input("What is the quantity (in ml) of your essential oil blend?\n"))
quantity_of_essencialoils = int(input("How many different essential oils are in your blend?\n"))

topical_oil = input("Is your essential blend for topical use? (yes/no)\n").lower()

if topical_oil == "yes":
    topical_percentage = 2.5
    oil_quantity = (topical_percentage / 100) * oil_blend
    oil_quantity_per_essencialoil = oil_quantity / quantity_of_essencialoils
    quantity_by_drop = oil_quantity_per_essencialoil * 20
    print(f"For a topical essential oil blend of {oil_blend}ml, you should add {oil_quantity_per_essencialoil:.2f}ml or {quantity_by_drop:.2f}gtt of each essential oil.")
elif topical_oil == "no":
    facial_oil = input("Is your essential blend for facial use? (yes/no)\n").lower()
    if facial_oil == "yes":
        facial_oil_percentage = 0.75
        oil_quantity = (facial_oil_percentage / 100) * oil_blend
        oil_quantity_per_essencialoil = oil_quantity / quantity_of_essencialoils
        quantity_by_drop = oil_quantity_per_essencialoil * 20
        print(f"For a facial essential oil blend of {oil_blend}ml, you should add {oil_quantity_per_essencialoil:.2f}ml or {quantity_by_drop:.2f}gtt of each essential oil.")
    elif facial_oil == "no":
        aromatic_oil = input("Is your essential blend for aromatic use? (yes/no)\n").lower()
        if aromatic_oil == "yes":
            aromatic_oil_percentage = 5
            oil_quantity = (aromatic_oil_percentage / 100) * oil_blend
            oil_quantity_per_essencialoil = oil_quantity / quantity_of_essencialoils
            quantity_by_drop = oil_quantity_per_essencialoil * 20
            print(f"For an aromatic essential oil blend of {oil_blend}ml, you should add {oil_quantity_per_essencialoil:.2f}ml or {quantity_by_drop:.2f}gtt of each essential oil.")
        else:
            print("We don't have information for that type of essential oil blend. Please consult a specialist.")

