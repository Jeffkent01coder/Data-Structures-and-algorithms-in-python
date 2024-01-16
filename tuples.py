#single element tuple
#tuple is faster than a list
#protects data from modification
tuple1 = (2,)

tuple2 = (1,2,3,4,5,6,7,8,9,10)
print(tuple2)

#covernting list to tuple
list = [1,2,3,4,5]
tuple3 = tuple(list)
print("list to tuple", tuple3)

#string to tuple
string = "Jeff kent"
tuple4 = tuple(string)
print("string to tuple", tuple4)

#Accessing Values in Tuples(slicing)
print(tuple2[1:4])

#Creating a Tuple From dict
my_dict = {'apple': 1, 'banana': 2, 'cherry': 3}
my_tuple = tuple(my_dict.items())
print(my_tuple)

#LENGHT
print(len(tuple2))

print(max(tuple2))
print(min(tuple2))
print(sum(tuple2))

#sort
sorted_tuple = tuple(sorted(tuple2))
print(sorted_tuple)


#sort
sorted_tuple = tuple(sorted(tuple2, reverse=True))
print(sorted_tuple)

print(tuple2.count(2))