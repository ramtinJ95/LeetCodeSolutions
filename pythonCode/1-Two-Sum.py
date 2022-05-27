lista = [1,2,3,4,5]
target = 7


def method(lista, target):
    hashmap = {}
    for i, l in enumerate(lista):
        complement = target - l
        if complement in hashmap:
            return [hashmap[complement], i]
        hashmap[l] = i
        
