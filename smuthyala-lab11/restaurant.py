'''
Python file : restaurant.py
Python code to create Restaurant class
Author : Sanjay Reddy Muthyala
'''

from store import Store
      

class Restaurant(Store):
          
   # constructor      
   def __init__(self, name, address, status, sales_tax_perc, max_occ, price_per_person):
      
       Store.__init__(self, name, address, status, sales_tax_perc)
       self.max_occ = max_occ
       self.noof_served = 0
       self.curr_occ = 0
       self.price_per_person = price_per_person
  
   # function to take no of people to be seated as input and returns true if the people can be seated else false
   def seat_patrons(self, noof_people):
       #condition to check if curr_occ + num_people <= max_occ and add noof_people to curr_occ
       if((self.curr_occ + noof_people) <= self.max_occ):
           self.curr_occ += noof_people
           return ("Welcome to %s" %(self.getName()))
       else: # noof_people cannot be seated
           return ("We are at capacity, we appreciate your patience")
  
   # function to take number of people to serve and returns the number of people served
   def serve_patrons(self, noof_people):
       self.noof_served += noof_people 
       return self.noof_served
  
   # function to take number of people leaving the restaurant and returns the current occupancy
   def checkout_patrons(self, noof_people):
       self.curr_occ -= noof_people 
       return self.curr_occ # return the updated current occupancy
      
   # mutator  
   def set_price_per_person(self, price_per_person):
       self.price_per_person = price_per_person
  
   # accessor
   def get_price_per_person(self):
       return self.price_per_person
  
   # calculate and return the total sales tax
   def calculate_total_sales_tax(self):
       return float(self.noof_served*self.price_per_person*self.get_sales_tax_perc())/100
