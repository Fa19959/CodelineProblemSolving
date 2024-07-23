
def DtoBinary(num):
    if num > 1:

        DtoBinary(num//2)

    print(num%2 ,end ="")




number=int(input("Input: "))


print("Output: ",end = "")

DtoBinary(number)
