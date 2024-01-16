dictionaty1 = dict()

#dictionay fuunctiions

my_dict = {'1': 'Jeff', '2': 'Win', '3': 'Kent'} 
my_dict.clear() 
print(my_dict)

d = {'Name': 'Jeff', 'Age': '19', 'Country': 'Kenya'} 
print(d.get('Name')) 
print(d.get('Gender'))

d = {'Name': 'Sean', 'Age': '19', 'Country': 'Kenya'} 
print(list(d.items())[1][0]) 
print(list(d.items())[1][1])

#The keys() method in Python returns a view object with dictionary keys, allowing efficient access and iteration.
d = {'Name': 'Ram', 'Age': '19', 'Country': 'India'} 
print(list(d.keys()))


#The values() method in Python returns a view object containing all dictionary values, which can be accessed and iterated through efficiently.
d = {'Name': 'Jeff', 'Age': '19', 'Country': 'Ke'} 
print(list(d.values()))

#Python’s update() method is a built-in dictionary function that updates the key-value pairs of a dictionary using elements from another dictionary or an iterable of key-value pairs. With this method, you can include new data or merge it with existing dictionary entries.
d1 = {'Name': 'Ram', 'Age': '19', 'Country': 'India'} 
d2 = {'Name': 'Neha', 'Age': '22'} 

d1.update(d2) 
print(d1)

#pop() method is a pre-existing dictionary method that removes and retrieves the value linked with a given key from a dictionary. If the key is not present in the dictionary, you can set an optional default value to be returned.
d = {'Name': 'Ram', 'Age': '19', 'Country': 'India'} 
d.pop('Age') 
print(d)

#popitem() method is a dictionary function that eliminates and returns a random (key, value) pair from the dictionary.
d = {'Name': 'Ram', 'Age': '19', 'Country': 'India'} 
d.popitem() 
print(d) 

d.popitem() 
print(d)




