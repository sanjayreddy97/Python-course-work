'''
Program for Troubleshooting chart for Diesel Engine
Name: Sanjay Reddy Muthyala
'''
import sys
print("Troubleshooting chart for Diesel engine")
while(True):
    while(True):
        status_light = input("Check status lights(Green, Amber, Red):")
        if(status_light != "green" and status_light != "amber" and status_light != "red"):
            print("Wrong value entered. Try again")
            continue
        else:
            break
    if (status_light.lower() == "green"):
        print("Do restart procedure")
        while(True):
            retest = input("Do you want to test again? (Yes/No): ")
            if((retest.lower() != "yes") and (retest.lower() != "no")):
                print("Invalid Entry. Try again")
                continue
            else:
                break
        if(retest.lower() == "yes"):
            continue
        else:
            break
    elif (status_light.lower() == "amber"):
        print("Check fuel line service routine")
        while(True):
            retest = input("Do you want to test again? (Yes/No): ")
            if((retest.lower() != "yes") and (retest.lower() != "no")):
                print("Invalid Entry. Try again")
                continue
            else:
                break
        if(retest.lower() == "yes"):
            continue
        else:
            break
    else: 
        while(True):
            meter = int(input("Shut-off all input lines and check readings in meter #3:"))
            try:
                check_meter = int(meter)
            except:
                print("Invalid entry")
                continue
            break
        if(int(meter) < 50):
            pressure = input("check main line for test pressure(low, normal, high):")
            while(True):
                if(pressure.lower() != "normal" and pressure.lower() != "high" and pressure.lower() != "low"):
                    print("Invalid entry. Try again")
                    continue
                else:
                    break
            if(pressure.lower() == "normal"): 
                print("Refer to motor service manual")
                while(True):
                    retest = input("Do you want to test again? (Yes/No): ")
                    if((retest.lower() != "yes") and (retest.lower() != "no")):
                        print("Invalid Entry. Try again")
                        continue
                    else:
                        break
                if(retest.lower() == "yes"):
                    continue
                else:
                    break
            elif(pressure.lower() == "high" or pressure.lower() == "low"):
                print("Refer to main line manual")
                while(True):
                    retest = input("Do you want to test again? (Yes/No): ")
                    if((retest.lower() != "yes") and (retest.lower() != "no")):
                        print("Invalid Entry. Try again")
                        continue
                    else:
                        break
                if(retest.lower() == "yes"):
                    continue
                else:
                    break
        elif (int(meter) >= 50):
            velocity = input("Measure flow velocity at inlet 2-B(low, normal, high):")
            while(True):
                if(velocity.lower() != "normal" and velocity.lower() != "high" and velocity.lower() != "low"):
                    print("Invalid entry. Try again")
                    continue
                else:
                    break
            if (velocity.lower() == "normal"):
                print("Refer to inlet service manual")
                while(True):
                    retest = input("Do you want to test again? (Yes/No): ")
                    if((retest.lower() != "yes") and (retest.lower() != "no")):
                        print("Invalid Entry. Try again")
                        continue
                    else:
                        break
                if(retest.lower() == "yes"):
                    continue
                else:
                    break
            elif (velocity.lower() == "high" or velocity.lower() == "low"):
                print("Refer unit for factory service")
                while(True):
                    retest = input("Do you want to test again? (Yes/No): ")
                    if((retest.lower() != "yes") and (retest.lower() != "no")):
                        print("Invalid Entry. Try again")
                        continue
                    else:
                        break
                if(retest.lower() == "yes"):
                    continue
                else:
                    break
print("The End, Thank you!")
sys.exit(0)


        
    
