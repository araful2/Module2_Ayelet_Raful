"""
Ayelet Raful
This project will display the menu for the campus cafe, and allow people to submit
their order, and receive their total due payment in the form of a receipt.


Pseudocode:
1.Import system so that my try and except can exit gracefully
2.Name the variables that I will need in my program
3.Create a function that will print the menu for the user
4.Create a user input function so that the user can input the amounts he wants. Include a try and except so that it will catch any inappropriate values.
5.Create function that will calculate the subtotal
6.Create a function that will calculate the tax, tip total and total
7.Create function that will format all my numbers with a dollar sign and round it to 2 decimal places
8.Create function that will print the receipt
9.Create a main that will run all the functions in the proper order and make sure to include a line that calculates the subtotal before implementing the compute_totals function.
"""


import sys

"""variables"""
coffee_price  = 2.25
muffin_price  = 2.75
tax_rate = .08875


def print_menu():
    print(f"              Campus Cafe")
    print(f"Coffee: ${coffee_price}")
    print(f"Muffin: ${muffin_price}")

    
    
def user_input():
    try:    
        coffee_qty = int(input(f"How many coffees? "))
        muffin_qty = int(input(f"How many muffins? "))
        """tip percent is the only value that can be a float"""
        tip_percent = float(input(f"Enter tip percent (e.g., 10 for 10%:) "))

        """using try and except to catch any inappropriate values"""

        if coffee_qty < 0 or muffin_qty < 0 or tip_percent < 0:
            raise ValueError

    except ValueError:
        print(f"Number of coffees and muffins must be integers > 0. Tip percent must be > 0. Program will exit")
        """ending system instead of looping or returning defaults"""
        sys.exit(1)


    return coffee_qty, muffin_qty, tip_percent

    

def line_totals(coffee_price, muffin_price, coffee_qty, muffin_qty):
    """coffee_price: float, muffin_price: float, coffee_qty: int, muffin_qty: int"""
    """multiplying price and qty for each item to receive its line total"""

    coffee_line_total = coffee_price * coffee_qty
    muffin_line_total = muffin_price * muffin_qty
    subtotal = coffee_line_total + muffin_line_total

    return coffee_line_total, muffin_line_total, subtotal


def compute_totals(subtotal, tax_rate, tip_percent):
    """subtotal: float, tax_rate: float, tip_percent: float"""
    """calculating the tip by converting user input to decimal form and then multiplying by the subtotal"""
    tip = tip_percent * .01 * subtotal 
    tax = subtotal * tax_rate 
    total = subtotal + tip + tax 

    return tax, tip, total


def format_currency(final_format):
    """Numbers will be floats with 2 decimal places, no trailing zeros."""
    return f"${final_format:.2f}"
    
    

def print_receipt():
    
    print(f"                    ---Receipt---")
    print(f"{coffee_qty} x coffee @ {coffee_price} = " + format_currency(coffee_line_total))
    print(f"{muffin_qty} x muffin @ {muffin_price} = " + format_currency(muffin_line_total))
    print(f"Subtotal:                       " + format_currency(subtotal))
    print(f"Tax (8.875%):                   " + format_currency(tax))
    print(f"Tip ({tip_percent}%):                    " + format_currency(tip))
    print(f"TOTAL:                          " + format_currency(total))
    print(f"Thank you!")

    

if __name__ == "__main__":

    print_menu()
    
    coffee_qty, muffin_qty, tip_percent = user_input()

    coffee_line_total, muffin_line_total, subtotal = line_totals(coffee_price, muffin_price, coffee_qty, muffin_qty)
    
    tax, tip, total = compute_totals(subtotal, tax_rate, tip_percent)

    print_receipt()

'''
    
SAMPLE RUN OF MY CODE:
              Campus Cafe
Coffee: $2.25
Muffin: $2.75
How many coffees? 1
How many muffins? 2
Enter tip percent (e.g., 10 for 10%:) 20
                    ---Receipt---
1 x coffee @ 2.25 = $2.25
2 x muffin @ 2.75 = $5.50
Subtotal:                       $7.75
Tax (8.875%):                   $0.69
Tip (20.0%):                    $1.55
TOTAL:                          $9.99
Thank you!

Process finished with exit code 0

'''



        

    



    
    

