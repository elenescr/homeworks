def set_to_tuple(set_1, set_2):
    set_3 = set_1.union(set_2)
    print(set_3)
    return tuple(set_3)


myset = {"apple", "banana", "cherry"}
thisset = {"apple", 1, True, "mango", 5, 2}

print(set_to_tuple(myset, thisset))
