print("--- GAMER+ ENGINE v1.0 ---")
name = input("Type your player name: ")
print("Welcome, " + name + "!")

gamer_coins = 100
phone_open = False

# Tracks if you own these items
has_gaming_chair = False
has_big_tv = False

print("\nYou are walking around... 🚶")
open_input = input("Type 'phone' to open: ")

if "phone" in open_input.lower():
    phone_open = True

while phone_open == True:
    print("\n--- 📱 GAMERPHONE ---")
    print("💰 Wallet: " + str(gamer_coins) + " Coins")
    print("---------------------")
    print("1 - Arena (Earn +50) 🎮")
    print("2 - My House 🏠")
    print("3 - Furniture Shop 🛒")
    print("4 - Secret Cheat Code 🔑")
    print("5 - Close Phone ❌")
    
    choice = input("Select number: ")
    
    if choice == "1":
        print("Jumping to ARENA... 🎮")
        gamer_coins = gamer_coins + 50
        print("You won! +50 Coins! 💰")
        
    elif choice == "2":
        print("\n--- 🏠 MY HOUSE ---")
        if has_gaming_chair == False and has_big_tv == False:
            print("Your house is empty! Go buy furniture.")
        if has_gaming_chair == True:
            print("💺 A cool neon Gaming Chair is in the corner!")
        if has_big_tv == True:
            print("📺 A giant Big Screen TV is on the wall!")
            
    elif choice == "3":
        print("\n--- 🛒 FURNITURE SHOP ---")
        print("1 - Gaming Chair (Cost: 500 Coins)")
        print("2 - Big Screen TV (Cost: 2000 Coins)")
        shop_choice = input("What do you want to buy? (1 or 2): ")
        
        if shop_choice == "1":
            if gamer_coins >= 500:
                gamer_coins = gamer_coins - 500
                has_gaming_chair = True
                print("Purchased a Gaming Chair! 💺")
            else:
                print("Not enough coins!")
        elif shop_choice == "2":
            if gamer_coins >= 2000:
                gamer_coins = gamer_coins - 2000
                has_big_tv = True
                print("Purchased a Big Screen TV! 📺")
            else:
                print("Not enough coins!")
                
    elif choice == "4":
        code = input("Enter Cheat Code: ")
        if code.lower() == "gamerplus":
            print("CHEAT UNLOCKED! 🎉")
            gamer_coins = gamer_coins + 10000
            print("+10,000 Coins added!")
        else:
            print("Wrong code!")
            
    elif choice == "5":
        print("Closing phone...")
        phone_open = False
    else:
        print("Invalid number!")
