import time

def PC_components():

    print("Welcome to CBUM_Store_2")
    print("You are in the PC components section")
    print("PAGE_1")
    print("\n")
    print('''
    1) Intel Core i5-13600K - ₹30,000
    2) NVIDIA GeForce RTX 3060 Ti - ₹45,000
    3) ASUS ROG STRIX B660 - ₹20,000
    4) Corsair Vengeance RGB Pro 32GB (2x16GB) DDR4 - ₹12,000
    5) Samsung 980 Pro 1TB NVMe SSD - ₹18,000''')
    print("\n")

    while True:
        choice = int(input("""
    1) for next page
    2) to purchase
    3) to exit
        enter option: """))

        if choice == 1:
            print("PAGE_2")
            print("\n")
            print('''
    1) AMD Ryzen 7 5800X - ₹35,000
    2) AMD Radeon RX 6700 XT - ₹35,000
    3) MSI MEG Z690 Unify - ₹30,000
    4) Kingston Fury Beast 16GB (2x8GB) DDR5 - ₹15,000
    5) Seagate BarraCuda 2TB HDD - ₹8,000''')
            print("\n")

            while True:
                choice2 = int(input("""
    1)to return to page 1
    2) to purchase
    3) to exit
        enter option: """))
                if choice2 in (1, 2, 3):
                    break
                else:
                    print("Invalid selection. Please enter 1, 2, or 3.")

            if choice2 == 1:
                PC_components()

            elif choice2 == 2:
                select = int(input("Enter the s.no of the component you want to purchase: "))
                while select not in range(1, 6):
                    print("Invalid selection. Please enter a number between 1 and 5.")
                    select = int(input("Enter the s.no of the component you want to purchase: "))

                card_number = input("Enter your credit card number: ")
                while len(card_number) != 16:
                    print("Invalid card number. Please enter a 16-digit number.")
                    card_number = input("Enter your credit card number: ")

                cvv = input("Enter your CVV code: ")
                while len(cvv) != 4:
                    print("Invalid CVV code. Please enter a 4-digit number.")
                    cvv = input("Enter your CVV code: ")

                print("Processing payment")
                for _ in range(3):
                    print(".", end="")
                    time.sleep(1)
                print(" Payment successful!")
            elif choice2 == 3:
                return
            
        elif choice == 2:
            select = int(input("Enter the s.no of the component you want to purchase: "))
            while select not in range(1, 6):
                print("Invalid selection. Please enter a number between 1 and 5.")
                select = int(input("Enter the s.no of the component you want to purchase: "))

            card_number = input("Enter your credit card number: ")
            while len(card_number) != 16:
                print("Invalid card number. Please enter a 16-digit number.")
                card_number = input("Enter your credit card number: ")

            cvv = input("Enter your CVV code: ")
            while len(cvv) != 4:
                print("Invalid CVV code. Please enter a 4-digit number.")
                cvv = input("Enter your CVV code: ")

            print("Processing payment")
            for _ in range(3):
                print(".", end="")
                time.sleep(1)
            print(" Payment successful!")
        elif choice == 3:
            return

PC_components()




