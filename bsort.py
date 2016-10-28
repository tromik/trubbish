

def string_to_array(list):
    array = []
    print len(list)
    for i in range(0, len(list)):
        array.insert(i, list[i])
    return array

def array_to_string(array, list):
    list = ''
    for i in range(0, len(array)):
        list = list + str(array[i])
    return list

def swap(list, x, y, pos, posplus):
    array = string_to_array(list)
    print "pos: " + str(pos) + " | posplus: " + str(posplus)
    array[pos] = y
    if posplus != len(array):
        array[posplus] = x
    list = array_to_string(array, list)
    print "list: " + list
    return list

def bsort_one_iter(list):
    counter = 0
    for n in range(0, len(list) - 1):
        if (counter + 1) < len(list):
            y = int(list[counter+1])
        x = int(list[counter])
        print "x: " + str(x) + " | y: " + str(y) + " | counter: " + str(counter)
        list = swap(list, x, y, counter, counter+1)
        counter = counter + 1
    print list
    return list

def bsort(lst):
    if not len(lst):
        return []
    if len(lst) == 1:
        return lst
    for i in range(0, len(lst)-1):
        if lst[i] >= lst[i+1]:
            temp = lst[i]
            lst[i] = lst[i+1]
            lst[i+1] = temp
    lst = bsort(lst[:len(lst)-1]) + [lst[len(lst)-1]]
    return lst

print bsort([])
print bsort([0,0,0])
print bsort(['a', 'c', 'b'])
print bsort([3,3,-1,99, 3])

# 5,4,3,2,1,6
# 4,3,2,1,5,6
#
