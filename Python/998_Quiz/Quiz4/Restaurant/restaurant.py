import random

rsts = ["Giorno's Pizzeria", "Mama's Sweets", "Zeke's Barbecue"]
Piz_menu = ["Large Pepperoni Pizza", "Small Pepperoni Pizza", "Olvive Pizza" "Spaghetti", "Tortellini"]
Mom_menu = ["Cream Donut", "Cake Pop", "Chocolate Chip Cookie", "M&M Cookie"]
BBQ_menu = ["BBQ Ribs", "Grilled Cheese Sandwich", "Hamburger", "Fried Chicken"]

choice = input("Which restaurant would you like to go to? " + str(rsts) + ": ")

if(choice == "Giorno's Pizzeria"):
    print("Here is the menu: " + str(Piz_menu))
    print("Suggested item: " + str(Piz_menu[random.randrange(len(Piz_menu))]))
    
elif(choice == "Mama's Sweets"):
    print("Here is the menu: " + str(Mom_menu))
    print("Suggested item: " + str(Mom_menu[random.randrange(len(Mom_menu))]))
    
elif(choice == "Zeke's Barbecue"):
    print("Here is the menu: " + str(BBQ_menu))
    print("Suggested item: " + str(BBQ_menu[random.randrange(len(BBQ_menu))]))
