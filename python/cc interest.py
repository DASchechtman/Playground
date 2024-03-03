import math
def CalcInterest(balance): 
    apr = .3
    dpr = apr / 365
    days = 30
    adb = sum([balance] * days) / days
    return adb * dpr * days


b = 300
for i in range(2):
    b = round(b+CalcInterest(b), 2)
    print(b)
