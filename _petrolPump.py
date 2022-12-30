'''
Auther - Sudeep Kulakarni
Decription - Fuel Rate 

'''

'''
import _fuel_rates as fr
ch = input("Enter Fuel Type : \n1]Petrol\n2]Diesel\n3]CNG = ")
if ch == "1":
    print("Petrol")
    print(f"Rate = {fr.fuel_petrol_rate}")

elif ch == "2":
    print("Diesel")
    print(f"Rate = {fr.fuel_disel_rate}")

elif ch == "3":
    print("CNG")
    print(f"Rate = {fr.fuel_cng_rate}")

else:
    print("Enter Vaild Choice !!")
'''


'''
Auther - Swapnil Bondar
Decription - Fuel Rate Code

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

    quantity = 0.0

    ch = int(input("Enter Your Choice [1/2/3/4] = "))

    if ch in (1, 2, 3, 4):
        if ch == 1:
            print("*************** Petrol ***************")

            #fuel_type = input("Enter Fuel Type = ")
            amount = float(input("Enter Amount = "))
            quantity = amount / fr.fuel_petrol_rate
            #print("%.2f" % quantity)
            print(f"Hi You Got {'%.2f' % quantity} litres Petrol of Rs. {amount}\n")

        elif ch == 2:
            print("*************** Diesel ***************")
            amount = float(input("Enter Amount = "))
            quantity = amount / fr.fuel_disel_rate
            print(f"Hi You Got {'%.2f' % quantity} litres Diesel of Rs. {amount}\n ")

        elif ch == 3:
            print("*************** CNG ***************")
            amount = float(input("Enter Amount = "))
            kg = amount / fr.fuel_cng_rate
            print(f"Hi You Got {'%.2f' % kg} Kg of Rs. {amount}\n")

        elif ch == 4:
            print("Thank You For Wisiting !!")
            sys.exit()

    else:
        print("Enter the amount = ")




