'''Python program to calculate currency
Author: Sanjay Reddy Muthyala
'''

from tkinter import *
from coin import Coin


def userInput(entry):

    try:

        #Get the user input

        inputValue=int(entry.get())

        return inputValue

    except:

        return None


def compute():

    dollars_output['text']= ''

    halfdollars_output['text'] = ''

    quarters_output['text']= ''

    dimes_output['text'] = ''

    nickels_output['text'] = ''

    pennies_output['text'] = ''

    totalOutput['text'] = ''

    dollars=userInput(dollarsInput)
    d = Coin("Dollars", dollars, 1.00)
    if d.check_input()== True:
        errorField['text'] = 'Invalid input for(dollars)'
        return

    halfdollars=userInput(halfdollarsInput)
    hd = Coin("Half-Dollars", halfdollars, 0.50)
    if hd.check_input() == True:
        errorField['text'] = 'Invalid input for(halfdollars)'
        return

    quarters=userInput(quartersInput)
    q = Coin("Quaters", quarters, 0.25)
    if q.check_input() == True:
        errorField['text'] = 'Invalid input for(quarters)'
        return
    
    dimes = userInput(dimesInput)
    dim = Coin("Dimes", dimes, 0.10)
    if dim.check_input() == True:
        errorField['text'] = 'Invalid input for(dimes)'
        return
    
    nickels = userInput(nickelsInput)
    n = Coin("Nickels", nickels, 0.05)
    if n.check_input() == True:
        errorField['text'] = 'Invalid input for(nickels)'
        return

    pennies = userInput(penniesInput)
    p = Coin("Pennies", pennies, 0.01)
    if p.check_input() == True:
        errorField['text'] = 'Invalid input for(pennies)'
        return

    dollars_output['text']= '${:.2f}'.format(d.cal_total())

    halfdollars_output['text'] = '${:.2f}'.format(hd.cal_total())

    quarters_output['text']='${:.2f}'.format(q.cal_total())

    dimes_output['text'] = '${:.2f}'.format(dim.cal_total())

    nickels_output['text'] = '${:.2f}'.format(n.cal_total())

    pennies_output['text'] = '${:.2f}'.format(p.cal_total())

    #calculate the total

    total=(d.cal_total())+(hd.cal_total())+(q.cal_total())+(dim.cal_total())+(n.cal_total())+(p.cal_total())

    totalOutput['text'] = '${:.2f}'.format(total)

    errorField['text'] = ''



#creating a tkinter window

win=Tk()

#setting title for window as Change Counter

win.title('Coins Counter')

#configuring all columns in GUI,

#so that maintains are all in uniform length

win.grid_columnconfigure(0, weight=1, uniform="abc")

win.grid_columnconfigure(1, weight=1, uniform="abc")

win.grid_columnconfigure(2, weight=1, uniform="abc")

win.grid_columnconfigure(3, weight=1, uniform="abc")


#creating all label, adding to the first row, the first column,

#with column span of 4 cells for the GUI

Label(win,text='Enter the number of coin types and click Calculate').grid(row=0,column=0,columnspan=4)

Label(win,text='Dollars:').grid(row=1,column=0)

dollarsInput=Entry(win)

dollarsInput.grid(row=1,column=1)

Label(win,text='Dollar value:').grid(row=1,column=2)

dollars_output=Label(win)

dollars_output.grid(row=1,column=3)

Label(win,text='Half-Dollars:').grid(row=2,column=0)

halfdollarsInput=Entry(win)

halfdollarsInput.grid(row=2,column=1)

Label(win,text='Half-Dollar value:').grid(row=2,column=2)

halfdollars_output=Label(win)

halfdollars_output.grid(row=2,column=3)

Label(win,text='Quarters:').grid(row=3,column=0)

quartersInput=Entry(win)

quartersInput.grid(row=3,column=1)

Label(win,text='Quarter value:').grid(row=3,column=2)

quarters_output=Label(win)

quarters_output.grid(row=3,column=3)


Label(win,text='Dimes:').grid(row=4,column=0)

dimesInput=Entry(win)

dimesInput.grid(row=4,column=1)

Label(win,text='Dime value:').grid(row=4,column=2)

dimes_output=Label(win)

dimes_output.grid(row=4,column=3)

Label(win,text='Nickels:').grid(row=5,column=0)

nickelsInput=Entry(win)

nickelsInput.grid(row=5,column=1)

Label(win,text='Nickel value:').grid(row=5,column=2)

nickels_output=Label(win)

nickels_output.grid(row=5,column=3)

Label(win,text='Pennies:').grid(row=6,column=0)

penniesInput=Entry(win)

penniesInput.grid(row=6,column=1)

Label(win,text='Penny value:').grid(row=6,column=2)

pennies_output=Label(win)

pennies_output.grid(row=6,column=3)

Button(win,text='Calculate',command=lambda : compute()).grid(row=7,column=0,columnspan=2)

Label(win,text='Total Change value:').grid(row=7,column=2)

                 

totalOutput=Label(win)

totalOutput.grid(row=7,column=3)

                 

#a label for showing errors

errorField=Label(win)

errorField.grid(row=8,column=0)

win.mainloop()
