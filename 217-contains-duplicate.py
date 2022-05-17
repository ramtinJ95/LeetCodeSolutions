list1 = [1,2,3,4,5]
list2 = [1,2,3,4,2]
list3 = [0,1,2,0]
list4 = [-1, -1, -1]

def checker(list1):
    hashmap = dict()
    zeroCounter = 0
    for l in list1:
        if (l == 0):
            zeroCounter += 1
        if(zeroCounter ==2):
            print("duplicate")
            return
        print(l)
        if (hashmap.get(l)):
            print("duplicate")
            return
        hashmap[l] = l
    print("no duplicaate")

def checker2(list1): # this one is slightly faster but uses the same amount of memory
    hashmap = {}
    for l in list1:
        if (hashmap[l] > 0):
            return True
        else: hashmap[l] = 1
        return False

checker(list1)
checker(list2)
checker(list3)
checker(list4)
