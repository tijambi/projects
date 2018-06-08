#output the daffodils between 100 and 999
for i in range(100,1000):
    num=str(i) #read the number as string
    num1=int(num[0]) #access each of the digit by using index and change back to integer
    num2=int(num[1])
    num3=int(num[2])
    sum=num1**3+num2**3+num3**3 #calculate the summation to check whether daffodil or not
    if(i==sum): #check the number if it is a daffodil
        print(sum) #if yes, print the number, else do nothing
