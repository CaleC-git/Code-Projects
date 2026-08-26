# return code

def ReLU(number):
    if number > 0:
        return number
    elif number <= 0:
        return 0

print(ReLU(6))
print(ReLU(0))
print(ReLU(-6))