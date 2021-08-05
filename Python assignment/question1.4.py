def rotateLeft(array_list, num_rotate):
    temp=[]
    for i in range(1, len(array_list)):
        if i<=num_rotate:
            temp.append(i)
    pos=0
    while num_rotate<len(array_list):
        array_list[pos] = array_list[num_rotate]
        pos = pos+1
        num_rotate=num_rotate+1
    array_list=array_list[:pos]+temp
    return array_list

print(rotateLeft([1,2,3,4,5],2))

