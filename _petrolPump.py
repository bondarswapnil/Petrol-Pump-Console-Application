
def petrol():
    amount = float(input("Enter Amount = "))
    quantity = amount / fr.fuel_petrol_rate
    print(f"Hi You Got {'%.2f' % quantity} litres Petrol of Rs. {amount}\n")
    sys.exit()

def diesel():
    amount = float(input("Enter Amount = "))
    quantity = amount / fr.fuel_disel_rate
    print(f"Hi You Got {'%.2f' % quantity} litres Diesel of Rs. {amount}\n ")
    sys.exit()

def cng():
    amount = float(input("Enter Amount = "))
    kg = amount / fr.fuel_cng_rate
    print(f"Hi You Got {'%.2f' % kg} Kg of Rs. {amount}\n")
    sys.exit()


import _fuel_rates as fr
import _petrolPump as pp
import sys
try:
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

        quantity = 0.0

        ch = input("Enter Your Choice = ")
        ch = ch.lower()
        if ch == "petrol" or ch == "1":
            print("*************** Petrol ***************")
            petrol()
            


        elif ch == "diesel" or ch == "2":
            print("*************** Diesel ***************")
            diesel()
            
                

        elif ch == "cng" or ch == "3":
            print("*************** CNG ***************")
            cng()
            
                

        elif ch == "exit" or "4":
            print("Thank You For Visiting !!")
            sys.exit()

        else:
            print("Enter a Valid Choice")
            print("**********************\n")
            fr.runner()
    

 
except BaseException as ex:
    print(f"")