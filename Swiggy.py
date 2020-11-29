import time

# This is the main class where it is working for multiple purpose

print("#"*35,"WELCOME TO SWIGGY!!!","#"*35)
print("\n")
print("We believe in giving you the best service and good taste!")
print("#"*35,"Best food ordering app :)","#"*35) 
print("\n"*2)    #Design for Main Menu
        

class Restaurant:
    def __init__(self, menu, price):
        
        self.menu = menu
        self.price = price
    
    def display(self):  # This method is used to display the menu items
    
        for i, j in zip(self.menu, self.price):
            print(i, ':', j)

    def priceamount(self):  # This method will shows the amount to be paidprint("\n")
    
        amount = 0
        ordered = []
        count = 0

        print("YOU ORDERED LIMIT IS 3")
        print()

        while True:
            if count == 3:
                break
            else:
                select = input("If you want to place your oder please press Y or N for not. :")
                if select == "Y" or "y":
                    dish = input("Select your dish: ")
                    if dish in self.menu:
                        ordered.append(dish)
                        a = self.menu.index(dish)
                        b = self.price[a]
                        amount += b
                        count += 1
                    else:
                        print("Your food is not in menu ")
                elif select == "N" or "n":
                    break
                else:
                    print("Print a valid statement ")
        print()
        print()

        print("YOUR ORDERED ITEMS ARE: ")  # It tracks the ordered food
        print()
        for i in ordered:
            print(i)

        print()
        print()

        print("YOUR TOTAL AMOUNT: ", amount)  # Total amount is displayed

    @staticmethod
    def timetaken(processing_time):
        # Every Restaurant has seprate processing time
        
        print("YOUR FOOD IS PREPARING........")
        time.sleep(processing_time)
        print("YOUR FOOD IS PREPARED :)")
        print("YOUR FOOD IS OUT FOR DELIVERY...")


    def compare(self, choose2, choose3):
        # This method use to compare with all 3 Restaurants
        # Minimmum price is chosen for a particular item

        display1 = [self.menu, choose2.menu, choose3.menu]
        display2 = []

        for i in display1:
            for j in i:
                if j not in display2:
                    display2.append(j)

        for i in display2:
            print(i)

        a = input("Enter your dish:")
        # Only Single dish can be selected due to edge cases

        if a in self.menu:
            b1 = self.menu.index(a)
            b2 = self.price[b1]
        else:
            b2 = 100000
        if a in choose2.menu:
            c1 = choose2.menu.index(a)
            c2 = choose2.price[c1]
        else:
            c2 = 100000

        if a in choose3.menu:
            d1 = choose3.menu.index(a)
            d2 = choose3.price[d1]
        else:
            d2 = 100000

        minimmum = min(b2, c2, d2)

        if minimmum == b2:
            print("Restaurant1 has the lowest price:", b2)
            x = input("Select Y for order and N for cancel:")
            if x == "Y":
                print("YOUR FOOD IS BEING PREPARED......")
                time.sleep(10)
                print("YOUR FOOD IS PREPARED")
                print("YOUR FOOD IS OUT FOR DELIVERY")
            elif x == "N":
                print("YOUR ORDER IS CANCELLED")
            else:
                print("YOUR SELECTION IS INVALID")

        elif minimmum == c2:
            print("Restaurant2 has the lowest price:", c2)
            x = input("Select Y for order and N for cancel:")
            if x == "Y":
                print("YOUR FOOD IS BEING PREPARED......")
                time.sleep(10)
                print("YOUR FOOD IS PREPARED")
                print("YOUR FOOD IS OUT FOR DELIVERY")
            elif x == "N":
                print("YOUR ORDER IS CANCELLED")
            else:
                print("YOUR SELECTION IS INVALID")

        elif minimmum == d2:
            print("Restaurant3 has the lowest price:", d2)
            x = input("Select Y for order and N for cancel:")
            if x == "Y":
                print("YOUR FOOD IS BEING PREPARED......")
                time.sleep(10)
                print("YOUR FOOD IS PREPARED")
                print("YOUR FOOD IS OUT FOR DELIVERY")
            elif x == "N":
                print("YOUR ORDER IS CANCELLED")
            else:
                print("YOUR SELECTION IS INVALID")
        else:
            print("INVALID SYNTAX")


if __name__ == "__main__":

    menu1 = ["Paneer", "Dal Makhni", "Naan", "Amritsari Kulcha", "Matar Mushroom"]
    price1 = [140, 120, 45, 45, 140]
    processing_time1 = 15

    menu2 = ["Rice", "Noodles", "Tandoori", "Shawarma", "ChillyChicken"]
    price2 = [150, 150, 200, 120, 120]
    processing_time2 = 15

    menu3 = ["Lasagna", "Sphagetti", "Chilly Mushroom", "Pizza", "Pasta"]
    price3 = [150, 160, 190, 225, 200]
    processing_time3 = 15

    flag = True
    input1 = int(input("1.OPEN THE APP   2.CLOSE THE APP:"))
    if input1 == 1:
        while True:

            input2 = int(input("1.TO ORDER FOOD   2.UPDATE MENU:"))
            if input2 == 1:
                print("*"*20,"1.SELECT BY RESTAURANT","*"*20)
                print("*"*20,"2.SELECT BY LOWEST PRICE","*"*20)
                print()
                Method = int(input("Select your method:"))

                if Method == 1:
                    print("*"*20,"1. Taj Hotel","*"*20)
                    print("*"*20,"2. Al Taj","*"*20)
                    print("*"*20,"3. Diggin","*"*20)

                    select = int(input("Select your Restaurant:"))
                    if select == 1:
                        choose = Restaurant(menu1, price1)
                        print()
                        choose.display()
                        print()
                        choose.priceamount()
                        choose.timetaken(processing_time1)
                    elif select == 2:
                        choose = Restaurant(menu2, price2)
                        print()
                        choose.display()
                        print()
                        choose.priceamount()
                        choose.timetaken(processing_time2)
                    elif select == 3:
                        choose = Restaurant(menu3, price3)
                        print()
                        choose.display()
                        print()
                        choose.priceamount()
                        choose.timetaken(processing_time3)
                elif Method == 2:
                    choose1 = Restaurant(menu1, price1)
                    choose2 = Restaurant(menu2, price2)
                    choose3 = Restaurant(menu3, price3)
                    choose1.compare(choose2, choose3)
            elif input2 == 2:
                print("1. Taj Hotel  2. Al Taj  3. Diggin")
                user1 = int(input("SELECT YOUR RESTAURANT:"))
                if user1 == 1:
                    menu1.append(input("Enter the dish name:"))
                    price1.append(int(input("Enter the cost for dish:")))
                elif user1 == 2:
                    menu2.append(input("Enter the dish name:"))
                    price2.append(int(input("Enter the cost for dish:")))
                elif user1 == 3:
                    menu3.append(input("Enter the dish name:"))
                    price3.append(int(input("Enter the cost for dish:")))
            input3 = int(input("1.TO ORDER FOOD OR UPDATE MENU  2.CLOSE THE APP:"))
            if input3 == 2:
                break
            elif input3 == 1:
                continue
