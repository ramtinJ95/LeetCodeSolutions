input1 = [1, 2]
input2 = [1, 2, 3, 4, 5]
input3 = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]


def uniqueOccurrences(arr) -> bool:
    db = {}
    for e in arr:
        if e not in db:
            db[e] = 0
        db[e] += 1

    return len(db) == len(set(db.values()))


print(uniqueOccurrences(input1))
print(uniqueOccurrences(input2))
print(uniqueOccurrences(input3))
