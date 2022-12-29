# petrol_pump_project

'''
Auther - Swapnil Bondar
Decription - Fuel Rate Code
Date - 29-12-2022

'''
print(__doc__)

    import _fuel_rates as fr
    import sys

    flag = True
    while(flag):

        title = "Sai Petrol Pump"
        print(title.center(50, "*"))
        print(" ")

        print("*************** Fuel Type ***************")
        print("1] Petrol")
        print("2] Diesel")
        print("3] CNG")
        print("4] Exit")

        petrol = fr.fuel_petrol_rate
        diesel = fr.fuel_disel_rate
        cng = fr.fuel_cng_rate
        quantity = 0.0

        ch = int(input("Enter Your Choice [1/2/3/4] = "))

        if ch in (1, 2, 3, 4):
            if ch == 1:
                print("*************** Petrol ***************")

                #fuel_type = input("Enter Fuel Type = ")
                amount = float(input("Enter Amount = "))
                quantity = amount / petrol
                #print("%.2f" % quantity)
                print(f"Hi You Got {'%.2f' % quantity} litres Petrol of Rs. {amount}\n")

            elif ch == 2:
                print("*************** Diesel ***************")
                amount = float(input("Enter Amount = "))
                quantity = amount / diesel
                print(f"Hi You Got {'%.2f' % quantity} litres Diesel of Rs. {amount}\n ")

            elif ch == 3:
                print("*************** CNG ***************")
                amount = float(input("Enter Amount = "))
                kg = amount / cng
                print(f"Hi You Got {kg} litres of Rs. {amount}\n")

            elif ch == 4:
                print("Thank You For Wisiting !!")
                sys.exit()

        else:
            print("Enter the amount = ")
