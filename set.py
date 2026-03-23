data = (10, 20, 30, 40)

print(data)
print(type(data))
data_list = (list(data))
print(type(data_list))
data_list.append(50)
print(data_list)
print(data_list[3])

data_set = set(data_list)
print(type(data_set))   
print(data_set)
data_set.add(50)