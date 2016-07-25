import sys
customerName = input("Hi! Welcome to Malik's Bistro.\nWhat is your name?\n")
print ("Welcome %s!" %(customerName))
print ("We have 4 options on the menu today.")
print ("Press 1 for Pepper Steak")
print ("Press 2 for Jerk Chicken")
print ("Press 3 for Fried Tilapia")
print ("Press 4 for Green Curry")
menuNumber = input("What would you like to eat?\n")
menuItem = "Menu Item"
if menuNumber == "1":
    menuItem = "Pepper Steak"
elif menuNumber == "2":
    menuItem = "Jerk Chicken"
elif menuNumber == "3":
    menuItem = "Fried Tilapia"
elif menuNumber == "4":
    menuItem = "Green Curry"
else:
    print("Sorry. That's not a valid menu option!")
    sys.exit()
print("%s, you have ordered %s. Your order should be ready in 15 minutes!"
      %(customerName, menuItem))
