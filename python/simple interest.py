I = 0.2707/365
p = 485.1
R = 33.09

TOTAL_INTEREST_PAID = 0

days_passed = 0
interest = 0

for i in range(547):
    interest += p * I
    days_passed += 1

    if days_passed == 30:
        r = R - interest
        TOTAL_INTEREST_PAID += interest
        p -= r
        days_passed = 0
        interest = 0

print(TOTAL_INTEREST_PAID)