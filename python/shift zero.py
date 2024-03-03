import random
import time
import copy

def ShiftZerosToEnd(arr):
    shifted_zeros = [el for el in arr if el != 0]
    return shifted_zeros + [0] * (len(arr) - len(shifted_zeros))

def ShiftZerosToEnd2(arr: list):
    cloned_arr = copy.deepcopy(arr)
    for i in range(len(cloned_arr)):
        if cloned_arr[i] == 0:
            cloned_arr.remove(cloned_arr[i])
            cloned_arr.append(0)
    return cloned_arr

def ShiftZerosToEnd3(arr: list):
    cloned_arr = copy.deepcopy(arr)
    i: int = 0
    first_shifted_zero: int = -1
    while i < len(cloned_arr):
        if i == first_shifted_zero:
            break
        elif not bool(cloned_arr[i]):
            cloned_arr.append(cloned_arr.pop(i))
            first_shifted_zero = first_shifted_zero - 1 if first_shifted_zero != -1 else len(cloned_arr) - 1
        else:
            i += 1
        
    return cloned_arr

n = 2000000000
arr = [random.randint(0, 100) for i in range(n)]
print("starting")
start = time.time()
x = ShiftZerosToEnd3(arr)
end = time.time()
print(end - start)