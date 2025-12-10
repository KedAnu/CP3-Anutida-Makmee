def vatCalculate(totalPrice):
    result=totalPrice*1.07
    return(result)
totalPrice=float(input())
print(vatCalculate(totalPrice))