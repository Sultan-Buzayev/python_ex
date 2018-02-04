

First = [1,3,5,11,25,111,23,8]

Second = [1,11,5,8,111,100,77,75]

Third = [5,111,77,88,44,8,112,11,8]

#common components

result1 = list(set(First) & set(Second) & set(Third))

#different components

result2 = list(set(First) - set(Second) - set(Third))

#sorting the order

sorted(result1)

sorted(result2)

result1.sort()

result2.sort()

#display 2 sets

print ("List_1= ", result1)
print ("List_2= ", result2)