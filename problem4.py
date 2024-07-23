ListString =input('Enter the list of integers: ')
userList=ListString.split(",")
#print('list string',userList)

for i in range(len(userList)):
    userList[i]=int(userList[i])

#print(userList)
even=[]
for num in userList:

    if num % 2 == 0:
         even.append(num)


#print(even)

square=[]

for i in even:

    square.append(i**2)

print("List of squares of even numbers: ",square)

index1 =int(input('Enter start index: '))
index2=int(input('Enter end index: '))

print('Sublist :',end="")
print(userList[index1:index2])
