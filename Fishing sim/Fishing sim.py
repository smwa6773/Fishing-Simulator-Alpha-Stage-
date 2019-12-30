import random
import time
run = True
cash = 10
Health = 100
Hunger = 100
FoodBackpack = []
CrateBackpack = []
ItemBackpack = []
FishBackpack = []
catchChance = 0
Equipped = ""
SurvivalMode = False
ShopDiscountCard = False
LakeFishingLicence = False
RiverFishingLicence = False
OceanFishingLicence = False
def wait_animation(character,loops,cooldown):
    for i in range(loops):
        print(character)
        time.sleep(cooldown)
saved = False
Choice = input("(WIP)Do you want to open a savefile?") 
try:
    if Choice == "yes":
        SaveFile = open("SaveFile.txt”, “r")
        data = SaveFile.readline()
        count = 0
        if data.count("#") != 0:
            data = data.split("#")
        for i in range(data[count]):
            FishBackpack.append(data[1+count])
            count += 1
        for i in range(data[count]):
            ItemBackpack.append(data[1+count])
            count += 1
        

except Exception:
    pass
while run:
    print("Welcome to The Fishing simulator")
    Play = input("Do you want to play?\n1: Yes\n2: No")
    if Play == "1":
        print("Enjoy the game")
        run = False
        gamemode = True
        FoodBackpack.append("Sandwich")
        FoodBackpack.append("Sandwich")
    else:
        pass

while gamemode:
    print("Welcome to The Fishing simulator")
    Play = input("What game mode do you want??\n1: Casual(no hunger)\n2: Survival(has hunger)")
    if Play == "2":
        SurvivalMode = True
        gamemode = False
    else:
        pass
        gamemode = False
while True:
    Fishing = input("Where do you want to Fish?\n1: pond\n2: lake\n3: river\n4: ocean")
    wait_animation("waiting",5,0.5)
    num = random.randint(1,100)
    if Fishing == "1":
        if num <= 10: # + catchChance:
          FishBackpack.append("Channel Catfish")
          print("You have captured a Channel Catfish")
        elif num <= 15: # + catchChance:
            FishBackpack.append("Bluegill")
            print("You have captured a Bluegill")
        elif num <= 20: # + catchChance:
            FishBackpack.append("Carp")
            print("You have captured a Carp")
        elif num <= 57: # + catchChance:
            FishBackpack.append("Hybrid Sunfish")
            print("You have captured a Hybrid Sunfish")
        elif num <= 60: #+ catchChance:
            CrateBackpack.append("Wooden Crate")
            print("You Got a Wooden Crate")
        elif num <= 80: # + catchChance:
            FishBackpack.append("Redear Sunfish")
            print("You have captured a Redear Sunfish")
        elif num <= 100: #+ catchChance:
            print("You Got Nothing")
            

    if Fishing == "2" and LakeFishingLicence == True:
        if num <= 10:
            FishBackpack.append("Sturgeon")
            print("You have captured a Sturgeon")
        elif num <= 15:
            FishBackpack.append("Smelt")
            print("You have captured a Smelt")
        elif num <= 20:
            FishBackpack.append("Muskellunge")
            print("You have captured a Muskellunge")
        elif num <= 57:
            FishBackpack.append("Perch")
            print("You have captured a Perch")
        elif num <= 80:
            FishBackpack.append("Bass")
            print("You have captured a Bass")
        elif num <= 90:
            FishBackpack.append("Burbots")
            print("You have captured a Burbots")
        elif num <= 100:
            print("You Got Nothing")
    if Fishing == "2" and LakeFishingLicence == False:
        print("You don't have Lake Fishing Licence")


    if Fishing == "3" and RiverFishingLicence == True:
        if num <= 10:
            FishBackpack.append("Pumpkinseed sunfish")
            print("You have captured a Pumpkinseed sunfish")
        elif num <= 15:
            FishBackpack.append("Walleye")
            print("You have captured a Walleye")
        elif num <= 20:
            FishBackpack.append("trout")
            print("You have captured a trout")
        elif num <= 57:
            FishBackpack.append("Largemouth bass")
            print("You have captured a Largemouth bass")
        elif num <= 80:
            FishBackpack.append("Black Bullhead")
            print("You have captured a Black Bullhead")
        elif num <= 90:
            FishBackpack.append("Northern Pike")
            print("You have captured a Northern Pike")
        elif num <= 100:
            print("You Got Nothing")
    if Fishing == "3" and RiverFishingLicence == False:
        print("You don't have River Fishing Licence")

    if Fishing == "4" and OceanFishingLicence == True:
        if num <= 10:
            FishBackpack.append("Angelfish")
            print("You have captured a Sturgeon")
        elif num <= 15:
            FishBackpack.append("Fang Tooth")
            print("You have captured a Smelt")
        elif num <= 20:
            FishBackpack.append("Blue Tang")
            print("You have captured a Blue Tang")
        elif num <= 57:
            FishBackpack.append("Wolffish")
            print("You have captured a Perch")
        elif num <= 80:
            FishBackpack.append("Trumpetfish")
            print("You have captured a Trumpetfish")
        elif num <= 90:
            FishBackpack.append("Tuna")
            print("You have captured a Tuna")
        elif num <= 100:
            print("You Got Nothing")
    if Fishing == "4" and OceanFishingLicence == False:
            print("You don't have Ocean Fishing Licence")
    if SurvivalMode == True:
            Hunger -= 25
            print("Hunger: " + str(Hunger))
            print("Health: " + str(Health))

    if SurvivalMode == True:
        if Hunger <= 0:
            Health -= 25
        
    shopping = True
    while shopping:
            print("Cash: " + str(cash))      
            choice = input("(WIP)\n1: Bambo Fishing Rod\n2: Plastic Fishing Rod\n3: Lake Fishing Licence\n4: River Fishing Licence\n5: Ocean Fishing Licence\n6: Sandwich\n7: Exit")
            if choice == "1" and cash >= 20:
                if ShopDiscountCard == True:
                    ItemBackpack.append("Bambo Fishing Rod")
                    cash -= 10
                    print("Cash: " + str(cash))
                else:
                    ItemBackpack.append("Bambo Fishing Rod")
                    cash -= 20
            elif choice == "2" and cash >= 60:
                if ShopDiscountCard == True:
                    ItemBackpack.append("Plastic Fishing Rod")
                    cash -= 30
                    print("Cash: " + str(cash))
                else:
                    ItemBackpack.append("Plastic Fishing Rod")
                    cash -= 60
                    print("Cash: " + str(cash))
            elif choice == "3" and cash >= 100:
                cash -= 100
                LakeFishingLicence = True
                print("Cash: " + str(cash))
            elif choice == "4" and cash >= 200:
                cash -= 200
                RiverFishingLicence = True
                print("Cash: " + str(cash))
            elif choice == "4" and cash >= 300:
                cash -= 300
                OceanFishingLicence = True
                print("Cash: " + str(cash))
            elif choice == "6" and cash >= 5:
                cash -= 5
                FoodBackpack.append("Sandwich")
                print("Cash: " + str(cash))
            else:
                shopping = False

    Choice =  input("Do you want to an equip and item(WIP)")
    if Choice == "yes" and len(ItemBackpack) != 0:
        for item in ItemBackpack:
            print(item)
        Choice = input("What do you want to equip??")
        if Choice in ItemBackpack:
                if Equipped == "Bambo Fishing Rod":
                    catchChance -= 5
                if Equipped == "Plastic Fishing Rod":
                    catchChance -= 15
                Equipped = Choice
                if Equipped == "Bambo Fishing Rod":
                    catchChance += 5
                if Equipped == "Plastic Fishing Rod":
                    catchChance += 15

    selling = True
    while selling:
        Choice = input("Do you want to sell an Fish?(WIP)")
        if Choice == "yes":
                print("Cash: " + str(cash))
                for item in FishBackpack:
                    print(item)
                Choice = input("What do you want to sell?")
                if FishBackpack.count(Choice) != 0:
                    if Choice == "Hybrid Sunfish":
                        FishBackpack.pop(FishBackpack.index("Hybrid Sunfish"))
                        cash += 1.50
                    elif Choice == "Redear Sunfish":
                        FishBackpack.pop(FishBackpack.index("Redear Sunfish"))
                        cash += 1.00
                    elif Choice == "Carp":
                        FishBackpack.pop(FishBackpack.index("Carp"))
                        cash += 2.00
                    elif Choice == "Bluegill":
                        FishBackpack.pop(FishBackpack.index("Bluegill"))
                        cash += 3.50
                    elif Choice == "Channel Catfish":
                        FishBackpack.pop(FishBackpack.index("Channel Catfish"))
                        cash += 4.00
                    elif Choice == "Burbots":
                        FishBackpack.pop(FishBackpack.index("Burbots"))
                        cash += 3.00
                    elif Choice == "Bass":
                        FishBackpack.pop(FishBackpack.index("Bass"))
                        cash += 3.50
                    elif Choice == "Perch":
                        FishBackpack.pop(FishBackpack.index("Perch"))
                        cash += 4.00
                    elif Choice == "Muskellunge":
                        FishBackpack.pop(FishBackpack.index("Muskellunge"))
                        cash += 4.50
                    elif Choice == "Smelt":
                        FishBackpack.pop(FishBackpack.index("Smelt"))
                        cash += 6.00
                    elif Choice == "Sturgeon":
                        FishBackpack.pop(FishBackpack.index("Sturgeon"))
                        cash += 6.50
                    elif Choice == "Northern Pike":
                        FishBackpack.pop(FishBackpack.index("Northern Pike"))
                        cash += 5.00
                    elif Choice == "Black Bullhead":
                        FishBackpack.pop(FishBackpack.index("Black Bullhead"))
                        cash += 5.50
                    elif Choice == "Largemouth bass":
                        FishBackpack.pop(FishBackpack.index("Largemouth bass"))
                        cash += 6.00
                    elif Choice == "trout":
                        FishBackpack.pop(FishBackpack.index("trout"))
                        cash += 6.50
                    elif Choice == "Walleye":
                        FishBackpack.pop(FishBackpack.index("Walleye"))
                        cash += 7.00
                    elif Choice == "Pumpkinseed sunfish":
                        FishBackpack.pop(FishBackpack.index("Pumpkinseed sunfish"))
                        cash += 7.50
                    elif Choice == "Tuna":
                        FishBackpack.pop(FishBackpack.index("Tuna"))
                        cash += 7.00
                    elif Choice == "Trumpetfish":
                        FishBackpack.pop(FishBackpack.index("Trumpetfish"))
                        cash += 7.50
                    elif Choice == "Wolffish":
                        FishBackpack.pop(FishBackpack.index("Wolffish"))
                        cash += 8.00
                    elif Choice == "Blue Tang":
                        FishBackpack.pop(FishBackpack.index("Blue Tang"))
                        cash += 8.50
                    elif Choice == "Fang Tooth":
                        FishBackpack.pop(FishBackpack.index("Fang Tooth"))
                        cash += 9.00
                    elif Choice == "Angelfish":
                        FishBackpack.pop(FishBackpack.index("Angelfish"))
                        cash += 9.50
        else:
            selling = False
            print("Cash: " + str(cash))



    crates = True
    num = random.randint(1,100)
    while crates:
        Choice = input("Do you want to open a crate?(WIP)")
        if Choice == "yes":
                for item in CrateBackpack:
                    print(item)
                Choice = input("What do you want to open?")
                if CrateBackpack.count(Choice) != 0:
                    num = random.randint(1,100)
                    if Choice == "Wooden Crate":
                        CrateBackpack.pop(CrateBackpack.index("Wooden Crate"))
                        if num <= 100 and ShopDiscountCard == False:
                            print("You have got a Shop Discount Card")
                            ShopDiscountCard = True
                    if Choice == "Iron Crate":
                        CrateBackpack.pop(CrateBackpack.index("Iron Crate"))
                        if num <= 100 and ShopDiscountCard == False:
                            print("You have got a Shop Discount Card")
                            ShopDiscountCard = True
                    if Choice == "Platinum Crate":
                        CrateBackpack.pop(CrateBackpack.index("Platinum Crate"))
                        if num <= 100 and ShopDiscountCard == False:
                            print("You have got a Shop Discount Card")
                            ShopDiscountCard = True
                    if Choice == "Plastic Crate":
                        CrateBackpack.pop(CrateBackpack.index("Plastic Crate"))
                        if num <= 100 and ShopDiscountCard == False:
                            print("You have got a Shop Discount Card")
                            ShopDiscountCard = True
        else:
            crates = False



    if SurvivalMode == True:
        feeding = True
        while feeding:
            Choice = input("Do you want to Eat")
            if Choice == "yes" and Hunger <= 100:
                    for item in FoodBackpack:
                        print(item)
                        if Choice == "Sandwich":
                                    FoodBackpack.pop(FoodBackpack.index("Sandwich"))
                                    Hunger += 50
            elif Choice == "yes" and Hunger >= 100:
                    for item in FishBackpack:
                        print("Your Full")
            else:
                feeding = False
                    
                        
                


    Choice = input("(WIP)Do you want to save?\n1: Yes?\n2: No?")
    if Choice == "1":
            data = "#"
            data += str(len(FishBackpack)) + "#"
            for item in FishBackpack:
                    data += item + "//"
            data += str(len(ItemBackpack)) + "#"
            for item in ItemBackpack:
                    data += item + "//"
            
            SaveFile = open("SaveFile.txt", "w")
            SaveFile.write(data)
            SaveFile.close()
        
        
    
                
