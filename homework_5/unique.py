def unique_list(l):
    unique = set(l)
    l = list(unique)
    return l

my_list = [1,1,2,3,4,5,1]
print(unique_list(my_list))
