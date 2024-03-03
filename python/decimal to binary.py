def DecToBinary(dec: float) -> [int, float]:
    x = dec * 2
    whole, fac = str(x).split('.')
    bin_num = 0
    if int(whole) >= 1:
        bin_num = 1
    return [bin_num, float('0.' + fac)]


dec = 0.33
bin = []

a, b = [1, 2]
print(f"a: {a}, b: {b}")

for i in range(1000):
    bin_num, dec = DecToBinary(dec)
    if dec >= 0 and dec <= 0:
        break
    bin.append(bin_num)
    

print(''.join([str(i) for i in bin]), dec)