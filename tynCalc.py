#python 3 tin, tray, case weight calculator
#tyncalc 1.2.1
#removed redundant variable declaration
from math import ceil

print("TYNCALC WEIGHT CALCULATOR - tynCalc v1.2.1")

def calproc():
    print("##### NEW TYNCALC MEASURMENT #####")
    print("----------------------------------")
    print("        ")
    try:
        trayct = int(input("enter number of trays: "))
        tinct = int(input("enter number of sample tins: "))
        rawwt = float((trayct * 1.25) + (tinct * 0.20))
        print("    ")
        print("raw weight is: ",rawwt," lbs.")
        print("    ")
        print("    ")
        print("translated weight:")
        print("    ")
        print("order weighs ",int(rawwt)," lbs. and ",round(float(16*(rawwt - int(rawwt))), 2)," oz. (UPS ",ceil(rawwt)," lbs.)")
        print("    ")
        print("    ")
        print("    ")
        print("    ")
        print("                 <end measurment>")
        print("    ")
        calproc()
    except ValueError:
        print('   ')
        print('not a recognized number. please type an integer using 0-9!')
        calproc()

calproc()
