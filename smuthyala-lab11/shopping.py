'''
Python file : shopping.py
Python program to test Restaurant and GroceryStore class
Author : Sanjay Reddy Muthyala
'''

from restaurant import Restaurant
from grocery_store import GroceryStore      
      
def main():
   print("-----------Restaurant test case-----------------")
   store1 = Restaurant("Mandys","31Street", "open", 8.75 , 100, 15)
   print("Restaurant %s is %s" %(store1.getName(),store1.getStatus()))
   noof_people = int(input("Enter num of people to be served: "))
   print(store1.seat_patrons(noof_people))
   print("Number of people served: %d "%store1.serve_patrons(noof_people))
   print("Total sales tax: $%.2f" %(float(store1.calculate_total_sales_tax())))
   noof_people = int(input("Enter num of people to be served: "))
   print(store1.seat_patrons(noof_people))
   print("--------------End of restaurant test------------------\n")
   print("-------------Grocery test case--------------------")
   store2 = GroceryStore("Kim's Convenience","32W madison Street", "open", 6.50, "independent")
   print("%s is %s" %(store2.getName(),store2.getStatus()))
   print("Total revenue of store after selling 6 eggs @1.50 $%.2f" %(store2.sell_item(6, 1.50)))
   print("Total revenue of store after selling 20 cheese @1.25 $%.2f" %(store2.sell_item(20, 1.25)))
   print("Total revenue of store after selling 50 tomato @0,90 $%.2f" %(store2.sell_item(50, 0.90)))
   print("Total sales tax: $%.2f" %(store2.calculate_total_sales_tax()))
   store2.setStatus("closed")
   print("%s is %s" %(store2.getName(),store2.getStatus()))
   print("------------End of Grocery test--------------------")
  
#call the main function  
main()  
