n = 1
while n <= 3:
    print(f"User number {n}: ")
    name = input("Enter your name: ")
    lastname = input("Enter your lastname: ")
    age = input("Enter your age: ")
    info_list = list((name, lastname, age))
    if n == 1:
        user1 = info_list.copy()
    elif n == 2:
        user2 = info_list.copy()
    else:
        user3 = info_list.copy()
    n += 1

costumer_info = []
costumer_info.append(user1)
costumer_info.append(user2)
costumer_info.append(user3)

costumer_index = int(input("Enter index of costumer (from 1 to 3): "))
costumer_index = costumer_index - 1
print(f"Name: {costumer_info[costumer_index][0]}")
print(f"Lastname: {costumer_info[costumer_index][1]}")
print(f"Age: {costumer_info[costumer_index][2]}")
