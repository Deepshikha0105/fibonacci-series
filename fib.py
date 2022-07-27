n=int(input("how many terms do you want: "))
n1, n2 = 0, 1
sum=0

if n<0:
    print("enter a positive number")
elif n==1:
    print("the sum is 0")

else:
    for i in range(n):
        print(n1)
        sum = sum + n1
        nth= n1+ n2
        n1= n2
        n2= nth

    print("the sum is" + str(sum))
