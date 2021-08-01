# Using Map with lambda function generate a third list with a single map statement that sums the integer elements of the same index of two given lists.

lst1=[100, 200, 300, 400, 500]
lst2=[1,10,100,1000,10000]
lst3 = list(map(lambda x,y:x+y, lst1,lst2))
print(lst3)