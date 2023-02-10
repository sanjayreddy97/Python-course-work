'''
Python file : grocery_store.py
Python code to create GroceryStore class
Author : Sanjay Reddy Muthyala
'''
from store import Store
      
class GroceryStore(Store):
  
   # constructor
   def __init__(self, name, address, status, sales_tax_perc, store_type):
       Store.__init__(self, name, address, status, sales_tax_perc)
       self.total_revenue = 0
       self.store_type = store_type
  
   # function that takes the quantity and price of item to sell and returns the total revenue after selling
   def sell_item(self, quantity, price_item):
       self.total_revenue += float(quantity)*price_item # add the revenue of selling the item to total_revenue
       return self.total_revenue # return the updated total_revenue
  
   # mutator
   def set_store_type(self, store_type):
       self.store_type = store_type
  
   # accessor
   def get_store_type(self):
       return self.store_type
  
   # calculate and return total sales tax
   def calculate_total_sales_tax(self):
       return float(self.total_revenue*self.get_sales_tax_perc())/100
