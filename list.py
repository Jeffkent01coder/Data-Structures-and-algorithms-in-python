list = [1,2,3,4,5, [1,2], [1,2],[1,2], "hey", "jeff"]
list2 =[10,9,8,7,6,5,4,3,2,1]

print(list)
print(list[2])

list.append(10)
print(list)

list.copy()
print(list)

list.extend(list2)
print(list)

list.insert(3, "mawia")
print(list)

print(list.count(10))

print(len(list))

# print(min(list))
# print(max(list))

list.pop()
print(list)

list2.sort()
print(list2)

list2.sort(reverse=True)
print(list2)

list2.reverse()
print(list2)

list2.remove(1)
print(list2)

del list2[3]
print(list2)