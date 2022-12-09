'''

NAME:   KADEN KRIDER

DATE:   SEPTEMBER 23, 2022

ASSN:   ASSIGNMENT A5

DESC:   THE FOLLOWING PYTHON MODULE PRINTS OUT A RECEIPT FROM FAMOUS
        RESTAURANT, YOUR OWN. THE USER WILL ENTER THE PRICE OF THEIR
        APPETIZER, THEIR ENTREE, AND THEIR DESSERT.  THEY WILL ALSO
        ENTER THE AMOUNT OF THEIR TIP, 0%, 10%, 15%, OR 20%.
        
        YOUR CODE WILL SHOW ALL THE ITEMS AND THEIR PRICES, THE FINAL
        SUBTOTAL, A 10% TAX (ON THE SUBTOTAL), THE TIP AMOUNT, AND THE
        FINAL AMOUNT TO BE CHARGED.
        
'''

# ASK THE USER FOR THE PRICE OF THEIR APPETIZER AND STORE THE FLOATING
# POINT VALUE IN THE OBJECT, appetizer.  THEY CAN ENTER 0.00 IF THEY
# DID NOT ORDER AN APPETIZER
appetizer = float(input("Please enter the price of your appetizer(0.00 if you did not order):  "))


#ASK THE USER FOR THE PRICE OF THEIR ENTREE AND STORE THE FLOATING
# POINT VALUE IN THE OBJECT, entree.  THEY CAN ENTER 0.00 IF THEY
# DID NOT ORDER AN ENTREE.
entree= float(input(" Please enter the price of your entree(0.00 if you did not order):  "))

# ASK THE USER FOR THE PRICE OF THEIR DESSERT AND STORE THE FLOATING
# POINT VALUE IN THE OBJECT, dessert.  THEY CAN ENTER 0.00 IF THEY
# DID NOT ORDER AN DESSERT.
dessert= float(input(" Please enter the price of your dessert(0.00 if you did not order):  "))


# ASK THE USER FOR THEIR TIP AMOUNT, 0, 10, 15, OR 20 AND STORE THE
# INTEGER VALUE IN THE OBJECT, tip_percent.  THEY CAN ENTER 0 IF THEY
# DID NOT GIVE A TIP.
tip_percent = int(input("Please enter the your tip percentage, e.g. 0, 10, 15, or 20:  " ))


# CALCULATE THE SUBTOTAL AND STORE IT AS A FLOATING POINT VALUE IN
# THE OBJECT, subtotal.
subtotal = appetizer + entree + dessert


# CALCULATE THE TAX AMOUNT AS A FLOATING POINT OBJECT, tax_amount.
tax_percent= 10 / 100 * subtotal 

# CALCULATE THE TIP AMOUNT AS A FLOATING POINT OBJECT, tip_amount, BY
# MULTIPLYING THE SUBTOTAL BY THE TIP PERCENT BY 0.01.
tip_percent = 0.01 * subtotal * tip_percent


# CALCULATE THE TOTAL AMOUNT BY ADDING THE SUBTOTAL, THE TAX AMOUNT, AND
# THE TIP AMOUNT, AND STORE THIS FLOATING POINT VALUE IN AN OBJECT NAMED
# total
total = subtotal + tax_percent + tip_percent


# PRINT THE RECEIPT SHOWING EACH ITEM NAME AND AMOUNT PROPERLY FORMATTED
# SHOWING 2 DIGITS FOR THE DECIMAL PORTION (SINCE THIS IS A MONETARY AMOUNT)
prices = { "Appetizer": appetizer, "Entree" : entree, "Dessert": dessert,  "Subtotal": subtotal, "Tax": tax_percent, "Tip_amount": tip_percent}

print()
for key, value in prices.items():
    print("{0.20}:  ${1: .2f}". format(key, value))
    print('------------------------------')

###############
### THE END ###
###############


