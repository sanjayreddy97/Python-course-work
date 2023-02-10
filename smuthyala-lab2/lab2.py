import math as m
import sys

def rad_to_deg(rad):
    degrees = float(rad * (180.0 / m.pi))
    return degrees

def deg_to_rad(deg):
    radians= float(deg * (m.pi / 180.0))
    return radians

''' This below method calculates retail prices.
'''
def cal_retail(mark_up = 2.5):
    another = 'y' # Variable to control the loop.
    # Process one or more items.
    while (another == 'y' or another == 'Y'):
        # Get the item's wholesale cost.
        wholesale = float(input("Enter the item's wholesale cost: "))
        validate(wholesale,mark_up)

def validate(wholesale, mark_up):
    # Validate the wholesale cost.
    while wholesale < 0:
        print('ERROR: the cost cannot be negative.')
        wholesale = float(input('Enter the correct wholesale cost:'))
    # Calculate the retail price.
    retail = wholesale * mark_up
    show_retail(retail,mark_up)

def show_retail(retail,mark_up):
    # Display the retail price.
    print('Retail price: $', format(retail, ',.2f'))
    # Do this again?
    another = input('Do you have another item? (Enter y for yes): ')
    if(another != 'y' and another != 'Y'):
        print("The End, Thank you")
        sys.exit(0)
    else:
        cal_retail(mark_up)

        
