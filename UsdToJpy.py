"""
The program calculates conversions between United States Dollars and Japanese Yen
"""

def usd_yen():
    """
    Allows the user to convert from USD to JPY or vice versa
    """
    print("This program converts between US Dollars and Japanese Yen.")
    while True:
        answer = input("Which currency are you starting with? (USD or JPY): ").lower().strip()
        if answer == "usd":
            while True:
                try:
                    amount = float(input("How much USD do you have? ").strip())
                    print(f"{str(amount)} USD is equivalent to {str(int(round(amount * 158.34)))} JPY")
                    break
                except ValueError:
                    print("Please enter an appropriate value.")
            break
        elif answer == "jpy":
            while True:
                try:
                    amount = int(input("How much JPY do you have? ").strip())
                    print(f"{str(amount)} JPY is equivalent to {str(round(amount/158.34,2))} USD")
                    break
                except ValueError:
                    print("Please enter an appropriate value.")
            break
        else:
            print("Please provide an appropriate answer.")

#start program
usd_yen()