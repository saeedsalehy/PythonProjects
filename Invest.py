"""My--Code"""

"""invest"""


def invest(amount, rate, years):
    for i in range(1, years + 1):
        amount = amount * (1 + rate)
        print(f"years {i} : ${amount:,.2f}")


amount = float(input("amount :"))
rate = float(input("rate : "))
years = int(input("years : "))
invest(amount, rate, years)
