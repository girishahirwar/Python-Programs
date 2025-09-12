#creat
list1=["rajvi","sunny","kirtan","girish"]
print(list1)
print(type(list1))
print(len(list1))

#read

for i in range(len(list1)):
	print(i)
	print(list1[i])

	for j in list1:
		print(j)

#update
#adding an element at last index
list1.append("bhoomika")
print(list1)
#adding an element at specific index
list1.insert(2,"ADARSH")
print(list1)
