fuel_petrol_rate = 105.50
fuel_disel_rate  = 92.00
fuel_cng_rate = 91.52

import sys
import _petrolPump as pp
def runner():
        ch = input("Enter Your Choice = ")
        ch = ch.lower()
        if ch == "petrol" or ch == "1":
            print("*************** Petrol ***************")
            pp.petrol()


        elif ch == "diesel" or ch == "2":
            print("*************** Diesel ***************")
            pp.diesel()
                

        elif ch == "cng" or ch == "3":
            print("*************** CNG ***************")
            pp.cng()
                

        elif ch == "exit" or "4":
            print("Thank You For Visiting !!")
            sys.exit()