'''
Python file : store.py
Author: Sanjay Reddy Muthyala
'''
class Store:
    #Initialisation constructor 
    def __init__(self, name, address, status, sales_tax_perc):
        self.name = name
        self.address = address
        self.status = status
        self.sales_tax_perc = sales_tax_perc

    def getName(self):
        return self.name
    
    def setName(self, name):
        self.name = name

    def getAddress(self):
        return self.address
    
    def setAddress(self,address):
        self.address = address

    def getStatus(self):
        return self.status
    
    def setStatus(self, status):
        self.status = status

    def set_sales_tax_perc(self, sales_tax_perc):
       self.sales_tax_perc = sales_tax_perc
    
    def get_sales_tax_perc(self):
       return self.sales_tax_perc

    #Function returns true if store is open and false is store is closed
    def is_store_open(self):
       if(status.lower() == "open"):
           return True
          
       return False
    
    #Abstract function
    def calculate_total_sales_tax(self):
        pass

    #Abstract function
    def calculate_total_sales(self):
        pass
