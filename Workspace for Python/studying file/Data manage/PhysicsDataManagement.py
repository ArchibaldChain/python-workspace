import math
Data1 = [70,64,69,72,62,71,54,68,65,77] # use this to input data
Data2 = [79.98, 80.04, 80.02, 80.03, 80.03, 80.04, 80.04,79.97, 80.05, 80.03, 80.02, 80, 80.02]
Data = [80.02, 79.94, 79.97, 79.98, 79.97, 80.03, 79.95, 79.97]

def averge(Data):
    sum = 0
    for i in Data:
        sum += i

    ave = sum / len(Data)
    return ave

def deviation(Data):
    sum = 0
    ave = averge(Data)
    for i in Data:
        sum += (i - ave) ** 2
    dev = math.sqrt(sum / (len(Data) - 1))
    return dev

def uncertainty(Data):
    sum = 0
    ave = averge(Data)
    length = len(Data)
    for i in Data:
        sum += (i - ave) ** 2
    uncer = math.sqrt(sum / (length * (length - 1)))
    return uncer

print("The average is ", averge(Data))
print("The deviation is ", deviation(Data))
print("The uncertainty is", uncertainty(Data))
