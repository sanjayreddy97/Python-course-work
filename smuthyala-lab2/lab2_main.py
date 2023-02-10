from lab2 import *

print("Program to convert from Degrees to Radians/ Radians to Degrees & to calculate retail price")
def main():
    while(True):
        print("1.Degrees to Radians\n2.Radians to Degrees")
        option = input("Enter the options from above(1 or 2):")
        if(option != '1' and option != '2'):
            print("Incorrect value entered, Try again")
            continue
        else:
            break
    if(int(option) == 1):
        degrees = float(input("Enter the value in degrees:"))
        radians = float(deg_to_rad(degrees))
        print("Value in Radians:", format(radians, ".4f"))
        print("\n")
    else:
        radians = float(input("Enter the value in radians:"))
        degrees = float(rad_to_deg(radians))
        print("Value in degrees:", format(degrees, ".4f"))
        print("\n")
    print("Program to calculate retail price")
    while(True):
        mark_up = input("Enter the deisred mark up percentage or press 'd' to continue to use default percentage: ")
        def is_integer(mark_up):
            try:
                int(mark_up)
            except ValueError:
                return False
            else:
                return isinstance(int(mark_up), int)

        def is_float(mark_up):
            try:
                float(mark_up)
            except ValueError:
                return False
            else:
                return isinstance(float(mark_up), float)
                       
        if(mark_up != 'd' and mark_up != 'D' and is_integer(mark_up) == False and is_float(mark_up) == False): 
            print("Incorrect value, Please try again")
            continue
        else:
            break
    if(mark_up == 'd' or mark_up =='D'):                
        cal_retail()
    else:
        cal_retail(float(mark_up))
        
main()
        
        
