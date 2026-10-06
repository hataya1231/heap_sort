def max_heap(lists):
    max = [0,0] #key , num整数のみ
    i = 0
    for i in range(len(lists)-1):
        if max[1] < lists[i]:
            max[0] = i
            max[1] = lists[i]
    lists.insert(0,lists.pop(max[0]))

    print(lists)

    oya = 1
    while len(lists) - 1 >= (oya*2+1 or oya*2+2): #子がいなくなる親がきたら終了
        ko1 = int(oya*2+1)
        ko2 = int(oya*2+2)
        print(oya,ko1,ko2)
        if lists[oya] < (lists[ko1] or lists[ko2]):
            if lists[ko1] > lists[ko2]:
                lists.insert(oya,lists.pop(ko1))
            else:
                lists.insert(oya,lists.pop(ko2))
        oya += 1
    return lists

def heap_sort(lists):
    last_index = len(lists)

    lists.insert(last_index-1,lists.pop(0))
    last_index -= 1

    irekae = [lists.pop(0),lists.pop(last_index-1)]
    lists.insert(0,irekae[1])
    lists.insert(last_index-1,irekae[0])

    oya = 0
    while last_index - 1 >= (oya*2+1 or oya*2+2):
        ko1 = int(oya*2+1)
        ko2 = int(oya*2+2)
        print(oya,ko1,ko2)
        if lists[oya] < (lists[ko1] or lists[ko2]):
            if lists[ko1] > lists[ko2]:
                lists.insert(oya,lists.pop(ko1))
            else:
                lists.insert(oya,lists.pop(ko2))
        oya += 1

            
myList = [4,5,7,3,6,9,10,8,11]

'''
1,2,3,4,5,6,7,8
0,1,1,2,2,3,3,4
'''
max_heaped_list = max_heap(myList)
print(max_heaped_list)

'''
sorted_list = heap_sort(max_heaped_list)
print(sorted_list)
'''