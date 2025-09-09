x=int(input("enter the number:"))
i=1
fact=1
while(i<=x):
	fact=fact*i
	i=i+1
	print("{})!={}".format(x,fact))